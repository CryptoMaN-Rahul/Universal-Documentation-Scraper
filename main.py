import argparse
import asyncio
import logging
import os
from typing import List, Set, Dict
from urllib.parse import urljoin, urlparse

import aiohttp
from bs4 import BeautifulSoup, Tag
import html2text

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

class DocumentationScraper:
    def __init__(self, base_url: str, output_dir: str, max_pages: int = 100, timeout: int = 30):
        self.base_url = base_url
        self.output_dir = output_dir
        self.max_pages = max_pages
        self.timeout = timeout

        self.visited_urls: Set[str] = set()
        self.content_list: List[Dict[str, str]] = []
        self.to_scrape: List[str] = [base_url]  # Start with the base URL

        self.html_converter = html2text.HTML2Text()
        self.html_converter.ignore_links = False
        self.html_converter.ignore_images = False
        self.html_converter.ignore_tables = False
        self.html_converter.body_width = 0  # Don't wrap lines

    async def scrape_documentation(self):
        async with aiohttp.ClientSession() as session:
            while self.to_scrape and len(self.visited_urls) < self.max_pages:
                url = self.to_scrape.pop(0)
                if url not in self.visited_urls:
                    await self.process_url(url, session)

        # Generate the final Markdown file
        await self.generate_markdown()

    async def process_url(self, url: str, session: aiohttp.ClientSession):
        if url in self.visited_urls:
            return

        self.visited_urls.add(url)
        logger.info(f"Processing: {url}")

        try:
            async with session.get(url, timeout=self.timeout) as response:
                content = await response.text()
            
            soup = BeautifulSoup(content, "html.parser")
            await self.extract_content(url, soup)
            await self.find_links(url, soup)
        except Exception as e:
            logger.error(f"Failed to process {url}: {str(e)}")

    async def extract_content(self, url: str, soup: BeautifulSoup):
        # Find the main content area (adjust selectors as needed)
        main_content = soup.find("main") or soup.find("article") or soup.find("div", class_="content")
        
        if not main_content:
            main_content = soup.find("body")

        if main_content:
            title = soup.find("title")
            title_text = title.text if title else "Untitled"
            
            # Process code blocks
            self.process_code_blocks(main_content)
            
            # Convert HTML to Markdown
            content_markdown = self.html_converter.handle(str(main_content))
            
            self.content_list.append({
                "url": url,
                "title": title_text,
                "content": content_markdown
            })
        else:
            logger.warning(f"Main content not found on {url}")

    def process_code_blocks(self, content: Tag):
        code_blocks = content.find_all(['pre', 'code'])
        for block in code_blocks:
            # Try to identify the language
            language = self.identify_language(block)
            
            # Add a label with the identified language
            block.insert(0, BeautifulSoup(f'<p><strong>{language} Code:</strong></p>', 'html.parser'))
            
            # Ensure the code block is properly formatted for Markdown
            if block.name == 'code' and block.parent.name != 'pre':
                block.wrap(soup.new_tag('pre'))
            
            block['class'] = block.get('class', []) + ['language-' + language]

    def identify_language(self, block: Tag) -> str:
        # This is a simple heuristic and might need to be expanded based on the documentation structure
        classes = block.get('class', [])
        text = block.get_text().lower()
        
        if any('language-' in c for c in classes):
            return next(c.replace('language-', '') for c in classes if 'language-' in c)
        elif 'python' in classes or 'import' in text or 'def ' in text:
            return 'python'
        elif 'javascript' in classes or 'function' in text or 'var ' in text or 'let ' in text or 'const ' in text:
            return 'javascript'
        elif 'java' in classes or 'public class' in text or 'private' in text:
            return 'java'
        elif 'bash' in classes or text.startswith('$') or text.startswith('#!'):
            return 'bash'
        else:
            return 'unknown'

    async def find_links(self, url: str, soup: BeautifulSoup):
        links = soup.find_all("a", href=True)
        for link in links:
            full_url = urljoin(url, link["href"])
            if self.is_valid_doc_url(full_url) and full_url not in self.visited_urls and full_url not in self.to_scrape:
                self.to_scrape.append(full_url)

    def is_valid_doc_url(self, url: str) -> bool:
        parsed = urlparse(url)
        base_parsed = urlparse(self.base_url)
        return (
            bool(parsed.netloc)
            and bool(parsed.scheme)
            and parsed.netloc == base_parsed.netloc
            and parsed.path.startswith(base_parsed.path)
        )

    async def generate_markdown(self):
        markdown_content = f"# Documentation for {self.base_url}\n\n"
        
        for item in self.content_list:
            markdown_content += f"## [{item['title']}]({item['url']})\n\n"
            markdown_content += item['content']
            markdown_content += "\n\n---\n\n"

        markdown_path = os.path.join(self.output_dir, "documentation.md")
        with open(markdown_path, "w", encoding="utf-8") as md_file:
            md_file.write(markdown_content)

        logger.info(f"Markdown file saved to: {markdown_path}")

async def main():
    parser = argparse.ArgumentParser(
        description="Scrape documentation and convert to Markdown"
    )
    parser.add_argument(
        "--url",
        required=True,
        help="Base URL of the documentation",
    )
    parser.add_argument(
        "--max-pages", type=int, default=100, help="Maximum number of pages to scrape"
    )
    parser.add_argument(
        "--timeout", type=int, default=30, help="Timeout for requests in seconds"
    )

    args = parser.parse_args()

    output_dir = "documentation_output"
    os.makedirs(output_dir, exist_ok=True)

    scraper = DocumentationScraper(
        args.url, output_dir, max_pages=args.max_pages, timeout=args.timeout
    )

    await scraper.scrape_documentation()

    logger.info(f"Total pages scraped: {len(scraper.visited_urls)}")

if __name__ == "__main__":
    asyncio.run(main())
