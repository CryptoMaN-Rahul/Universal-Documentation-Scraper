import argparse
import base64
import logging
import os
import time
from urllib.parse import urljoin
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from xhtml2pdf import pisa

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


class MarketDataFeedDocDownloader:
    """ """

    def __init__(self, base_url, output_dir, max_pages=100, timeout=30):
        self.base_url = base_url
        self.output_dir = output_dir
        self.max_pages = max_pages
        self.timeout = timeout

        self.visited_urls = set()
        self.html_content = []

        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(options=chrome_options)

    def download_documentation(self):
        """ """
        self.process_url(self.base_url)
        self.driver.quit()
        self.generate_pdf()

    def process_url(self, url):
        """

        :param url:

        """
        if url in self.visited_urls or len(
                self.visited_urls) >= self.max_pages:
            return

        self.visited_urls.add(url)
        logger.info(f"Processing: {url}")

        try:
            self.driver.get(url)
            WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.TAG_NAME, "body")))
        except TimeoutException:
            logger.error(f"Timeout while loading {url}")
            return
        except Exception as e:
            logger.error(f"Failed to fetch {url}: {str(e)}")
            return

        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        self.extract_content(url, soup)
        self.find_links(url, soup)

    def extract_content(self, url, soup):
        """

        :param url:
        :param soup:

        """
        # Remove script elements
        for script in soup(["script"]):
            script.decompose()

        # Find the main content area
        main_content = soup.find("main")
        if main_content:
            # Process images
            for img in main_content.find_all("img"):
                self.process_image(img, url)

            # Ensure code snippets are preserved
            for pre in main_content.find_all("pre"):
                pre["style"] = "white-space: pre-wrap; word-wrap: break-word;"

            # Add the processed HTML to our content list
            self.html_content.append(str(main_content))
        else:
            logger.warning(f"Main content not found on {url}")

    def process_image(self, img, base_url):
        """

        :param img:
        :param base_url:

        """
        src = img.get("src")
        if src:
            if src.startswith("data:image"):
                # The image is already a data URL, no need to modify
                return

            # Convert relative URLs to absolute URLs
            img_url = urljoin(base_url, src)

            try:
                response = requests.get(img_url, timeout=self.timeout)
                response.raise_for_status()
                img_data = base64.b64encode(response.content).decode("utf-8")
                img["src"] = f"data:image/png;base64,{img_data}"
            except Exception as e:
                logger.error(f"Failed to process image {img_url}: {str(e)}")
                # Remove the src attribute if we can't process the image
                img["src"] = ""

    def find_links(self, url, soup):
        """

        :param url:
        :param soup:

        """
        links = soup.find_all("a", href=True)
        for link in links:
            href = link["href"]
            full_url = urljoin(url, href)
            if self.is_valid_doc_url(full_url):
                self.process_url(full_url)

    def is_valid_doc_url(self, url):
        """

        :param url:

        """
        parsed = urlparse(url)
        return (bool(parsed.netloc) and bool(parsed.scheme)
                and parsed.netloc == urlparse(self.base_url).netloc
                and "/developer/api-documentation/get-market-data-feed"
                in parsed.path)

    def generate_pdf(self):
        """ """
        pdf_path = os.path.join(self.output_dir,
                                "market_data_feed_documentation.pdf")

        # Combine all HTML content
        full_html = f"""
        <html>
        <head>
            <meta charset="UTF-8">
            <style>
                body {{ font-family: Arial, sans-serif; }}
                img {{ max-width: 100%; height: auto; }}
                pre {{ white-space: pre-wrap; word-wrap: break-word; background-color: #f0f0f0; padding: 10px; }}
            </style>
        </head>
        <body>
            {"<hr>".join(self.html_content)}
        </body>
        </html>
        """

        # Convert HTML to PDF
        with open(pdf_path, "wb") as pdf_file:
            pisa_status = pisa.CreatePDF(full_html, dest=pdf_file)

        if pisa_status.err:
            logger.error("Error creating PDF")
        else:
            logger.info(f"PDF saved to: {pdf_path}")


def main():
    """ """
    parser = argparse.ArgumentParser(
        description=
        "Download Market Data Feed API documentation and convert to PDF")
    parser.add_argument(
        "--url",
        default=
        "https://upstox.com/developer/api-documentation/get-market-data-feed/",
        help="Base URL of the Market Data Feed API documentation",
    )
    parser.add_argument("--max-pages",
                        type=int,
                        default=100,
                        help="Maximum number of pages to download")
    parser.add_argument("--timeout",
                        type=int,
                        default=30,
                        help="Timeout for requests in seconds")

    args = parser.parse_args()

    output_dir = "market_data_feed_docs"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    downloader = MarketDataFeedDocDownloader(args.url,
                                             output_dir,
                                             max_pages=args.max_pages,
                                             timeout=args.timeout)

    start_time = time.time()
    downloader.download_documentation()
    end_time = time.time()

    logger.info(f"Download completed in {end_time - start_time:.2f} seconds")
    logger.info(f"Total pages downloaded: {len(downloader.visited_urls)}")


if __name__ == "__main__":
    main()
