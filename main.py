import argparse
import asyncio
import logging
import os
from typing import Dict, List, Set
from urllib.parse import urljoin, urlparse

import aiohttp
import html2text
from bs4 import BeautifulSoup, Tag

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class MarketDataFeedDocScraper:
    """ """

    def __init__(
        self, base_url: str, output_dir: str, max_pages: int = 100, timeout: int = 30
    ):
        self.base_url = base_url
        self.output_dir = output_dir
        self.max_pages = max_pages
        self.timeout = timeout

        self.visited_urls: Set[str] = set()
        self.content_list: List[Dict[str, str]] = []
        self.to_scrape: List[str] = []

        self.html_converter = html2text.HTML2Text()
        self.html_converter.ignore_links = False
        self.html_converter.ignore_images = False
        self.html_converter.ignore_tables = False
        self.html_converter.body_width = 0  # Don't wrap lines

    async def scrape_documentation(self):
        async with aiohttp.ClientSession() as session:
            # Get initial links
            await self.get_initial_links(session)

            # Recursively scrape each link
            while self.to_scrape:
                url = self.to_scrape.pop(0)
                await self.process_url(url, session)

        # Generate the final Markdown file
        await self.generate_markdown()

    async def get_initial_links(self, session: aiohttp.ClientSession):
        logger.info(f"Getting initial links from: {self.base_url}")
        async with session.get(self.base_url, timeout=self.timeout) as response:
            content = await response.text()

        soup = BeautifulSoup(content, "html.parser")
        links = soup.find_all("a", href=True)

        for link in links:
            full_url = urljoin(self.base_url, link["href"])
            if self.is_valid_doc_url(full_url) and full_url not in self.visited_urls:
                self.to_scrape.append(full_url)

        logger.info(f"Found {len(self.to_scrape)} initial links to scrape")

    async def process_url(self, url: str, session: aiohttp.ClientSession):
        if url in self.visited_urls or len(self.visited_urls) >= self.max_pages:
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
        main_content = (
            soup.find("main")
            or soup.find("article")
            or soup.find("div", class_="content")
        )

        if not main_content:
            main_content = soup.find("body")

        if main_content:
            title = soup.find("title")
            title_text = title.text if title else "Untitled"

            # Process code blocks to keep only Node.js related code
            self.process_code_blocks(main_content)

            # Convert HTML to Markdown
            content_markdown = self.html_converter.handle(str(main_content))

            self.content_list.append(
                {"url": url, "title": title_text, "content": content_markdown}
            )
        else:
            logger.warning(f"Main content not found on {url}")

    def process_code_blocks(self, content: Tag):
        """

        :param content: Tag:

        """
        code_blocks = content.find_all(["pre", "code"])
        for block in code_blocks:
            # Check if the code block is Node.js related
            if self.is_nodejs_code(block):
                # If it's Node.js, we keep it and add a label
                block.insert(
                    0,
                    BeautifulSoup(
                        "<p><strong>Node.js Code:</strong></p>", "html.parser"
                    ),
                )
            else:
                # If it's not Node.js, we remove the block
                block.decompose()

    def is_nodejs_code(self, block: Tag) -> bool:
        """

        :param block: Tag:

        """
        # This method checks if a code block is Node.js related
        # You may need to adjust this based on the specific structure of the documentation
        text = block.get_text().lower()
        nodejs_indicators = [
            "node",
            "npm",
            "require(",
            "module.exports",
            "async/await",
            "promise",
        ]
        return any(indicator in text for indicator in nodejs_indicators)

    async def find_links(self, url: str, soup: BeautifulSoup):
        links = soup.find_all("a", href=True)
        for link in links:
            full_url = urljoin(url, link["href"])
            if (
                self.is_valid_doc_url(full_url)
                and full_url not in self.visited_urls
                and full_url not in self.to_scrape
            ):
                self.to_scrape.append(full_url)

    def is_valid_doc_url(self, url: str) -> bool:
        """

        :param url: str:

        """
        parsed = urlparse(url)
        base_parsed = urlparse(self.base_url)
        return (
            bool(parsed.netloc)
            and bool(parsed.scheme)
            and parsed.netloc == base_parsed.netloc
            and parsed.path.startswith(base_parsed.path)
        )

    async def generate_markdown(self):
        markdown_content = "# Market Data Feed Documentation\n\n"

        for item in self.content_list:
            markdown_content += f"## [{item['title']}]({item['url']})\n\n"
            markdown_content += item["content"]
            markdown_content += "\n\n---\n\n"

        markdown_path = os.path.join(
            self.output_dir, "market_data_feed_documentation.md"
        )
        with open(markdown_path, "w", encoding="utf-8") as md_file:
            md_file.write(markdown_content)

        logger.info(f"Markdown file saved to: {markdown_path}")


async def main():
    parser = argparse.ArgumentParser(
        description="Scrape Market Data Feed API documentation and convert to Markdown"
    )
    parser.add_argument(
        "--url",
        default="https://upstox.com/developer/api-documentation",
        help="Base URL of the Market Data Feed API documentation",
    )
    parser.add_argument(
        "--max-pages", type=int, default=100, help="Maximum number of pages to scrape"
    )
    parser.add_argument(
        "--timeout", type=int, default=30, help="Timeout for requests in seconds"
    )

    args = parser.parse_args()

    output_dir = "market_data_feed_docs"
    os.makedirs(output_dir, exist_ok=True)

    scraper = MarketDataFeedDocScraper(
        args.url, output_dir, max_pages=args.max_pages, timeout=args.timeout
    )

    await scraper.scrape_documentation()

    logger.info(f"Total pages scraped: {len(scraper.visited_urls)}")


if __name__ == "__main__":
    asyncio.run(main())
