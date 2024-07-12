import os
import time
import argparse
from urllib.parse import urljoin, urlparse

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from bs4 import BeautifulSoup
from xhtml2pdf import pisa
import base64
import requests
import logging
import random

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class DocDownloader:
    def __init__(self, base_url, output_dir, max_pages=100, timeout=60, max_retries=3):
        self.base_url = base_url
        self.output_dir = output_dir
        self.max_pages = max_pages
        self.timeout = timeout
        self.max_retries = max_retries
        
        self.visited_urls = set()
        self.html_content = []

        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(options=chrome_options)

    def download_documentation(self):
        self.process_url(self.base_url)
        self.driver.quit()
        self.generate_pdf()

    def process_url(self, url):
        if url in self.visited_urls or len(self.visited_urls) >= self.max_pages:
            return

        self.visited_urls.add(url)
        logger.info(f"Processing: {url}")

        for attempt in range(self.max_retries):
            try:
                self.driver.get(url)
                WebDriverWait(self.driver, self.timeout).until(
                    EC.presence_of_element_located((By.TAG_NAME, "body"))
                )
                # Wait for the content to load
                time.sleep(5)  # Add a small delay
                
                soup = BeautifulSoup(self.driver.page_source, 'html.parser')
                self.extract_content(url, soup)
                self.find_links(url, soup)
                break
            except TimeoutException:
                logger.error(f"Timeout while loading {url} (Attempt {attempt + 1}/{self.max_retries})")
                if attempt == self.max_retries - 1:
                    logger.error(f"Failed to load {url} after {self.max_retries} attempts")
                    return
            except Exception as e:
                logger.error(f"Failed to fetch {url}: {str(e)} (Attempt {attempt + 1}/{self.max_retries})")
                if attempt == self.max_retries - 1:
                    logger.error(f"Failed to process {url} after {self.max_retries} attempts")
                    return
            time.sleep(random.uniform(1, 3))  # Random delay between retries

    def extract_content(self, url, soup):
        # Find the main content area
        main_content = soup.find('div', class_='api-content') or soup.find('main') or soup.find('body')
        if main_content:
            # Process images
            for img in main_content.find_all('img'):
                self.process_image(img, url)

            # Ensure code snippets are preserved
            for pre in main_content.find_all('pre'):
                pre['style'] = 'white-space: pre-wrap; word-wrap: break-word;'

            # Add the processed HTML to our content list
            self.html_content.append(f"<h1>{soup.title.string if soup.title else 'Untitled Page'}</h1>")
            self.html_content.append(str(main_content))
        else:
            logger.warning(f"Main content not found on {url}")

    def process_image(self, img, base_url):
        src = img.get('src')
        if src:
            if src.startswith('data:image'):
                return
            
            img_url = urljoin(base_url, src)
            
            try:
                response = requests.get(img_url, timeout=self.timeout)
                response.raise_for_status()
                img_data = base64.b64encode(response.content).decode('utf-8')
                img['src'] = f"data:image/png;base64,{img_data}"
            except Exception as e:
                logger.error(f"Failed to process image {img_url}: {str(e)}")
                img['src'] = ''

    def find_links(self, url, soup):
        for a in soup.find_all('a', href=True):
            href = a['href']
            full_url = urljoin(url, href)
            if self.is_valid_doc_url(full_url):
                self.process_url(full_url)

    def is_valid_doc_url(self, url):
        parsed = urlparse(url)
        base_parsed = urlparse(self.base_url)
        return (bool(parsed.netloc) and bool(parsed.scheme) and
                parsed.netloc == base_parsed.netloc and
                parsed.path.startswith(base_parsed.path))

    def generate_pdf(self):
        pdf_path = os.path.join(self.output_dir, "documentation.pdf")
        
        full_html = f"""
        <html>
        <head>
            <meta charset="UTF-8">
            <style>
                body {{ font-family: Arial, sans-serif; }}
                img {{ max-width: 100%; height: auto; }}
                pre {{ white-space: pre-wrap; word-wrap: break-word; background-color: #f0f0f0; padding: 10px; }}
                table {{ border-collapse: collapse; width: 100%; }}
                th, td {{ border: 1px solid #ddd; padding: 8px; }}
                th {{ background-color: #f2f2f2; }}
            </style>
        </head>
        <body>
            {"<hr>".join(self.html_content)}
        </body>
        </html>
        """
        
        with open(pdf_path, "wb") as pdf_file:
            pisa_status = pisa.CreatePDF(full_html, dest=pdf_file)
        
        if pisa_status.err:
            logger.error('Error creating PDF')
        else:
            logger.info(f"PDF saved to: {pdf_path}")

def main():
    parser = argparse.ArgumentParser(description="Download API documentation and convert to PDF")
    parser.add_argument("url", help="Base URL of the API documentation")
    parser.add_argument("--max-pages", type=int, default=100, help="Maximum number of pages to download")
    parser.add_argument("--timeout", type=int, default=60, help="Timeout for requests in seconds")
    parser.add_argument("--max-retries", type=int, default=3, help="Maximum number of retries for each page")

    args = parser.parse_args()

    output_dir = "api_docs"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    downloader = DocDownloader(
        args.url,
        output_dir,
        max_pages=args.max_pages,
        timeout=args.timeout,
        max_retries=args.max_retries
    )

    start_time = time.time()
    downloader.download_documentation()
    end_time = time.time()

    logger.info(f"Download completed in {end_time - start_time:.2f} seconds")
    logger.info(f"Total pages downloaded: {len(downloader.visited_urls)}")

if __name__ == "__main__":
    main()
