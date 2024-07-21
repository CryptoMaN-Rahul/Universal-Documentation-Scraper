import argparse
import asyncio
import logging
import os
from typing import Dict, List, Set

import aiohttp
from bs4 import BeautifulSoup, Tag
import jsbeautifier

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

class MarketDataFeedDocScraper:
    def __init__(self, urls: List[str], output_dir: str, timeout: int = 30):
        self.urls = urls
        self.output_dir = output_dir
        self.timeout = timeout
        self.visited_urls: Set[str] = set()
        self.content_list: List[Dict[str, str]] = []
        self.js_beautifier = jsbeautifier.beautify

    async def scrape_documentation(self):
        async with aiohttp.ClientSession() as session:
            tasks = [self.process_url(url, session) for url in self.urls]
            await asyncio.gather(*tasks)
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
        except Exception as e:
            logger.error(f"Failed to process {url}: {str(e)}")

    async def extract_content(self, url: str, soup: BeautifulSoup):
        main_content = soup.find("div", class_="theme-doc-markdown")
        if main_content:
            title = main_content.find("h1")
            title_text = title.text.strip() if title else "Untitled"
            content_markdown = f"# {title_text}\n\n"

            sections = main_content.find_all(["h2", "h3"], class_="anchor")
            for section in sections:
                section_title = section.text.strip()
                header_level = "#" * (2 if section.name == "h2" else 3)
                content_markdown += f"{header_level} {section_title}\n\n"

                next_element = section.find_next_sibling()
                while next_element and next_element.name not in ["h2", "h3"]:
                    if next_element.name == "div" and "tabs-container" in next_element.get("class", []):
                        nodejs_code = self.extract_nodejs_code(next_element)
                        if nodejs_code:
                            content_markdown += f"```javascript\n{nodejs_code}\n```\n\n"
                    next_element = next_element.find_next_sibling()

            self.content_list.append({
                "url": url,
                "title": title_text,
                "content": content_markdown
            })
        else:
            logger.warning(f"Main content not found on {url}")

    def extract_nodejs_code(self, tabs_container: Tag) -> str:
        nodejs_tab = tabs_container.find("li", string="Node.js")
        if nodejs_tab:
            tab_index = list(nodejs_tab.parent.children).index(nodejs_tab)
            tab_content = tabs_container.find_all("div", class_="tabItem_Ymn6")[tab_index]
            code_block = tab_content.find("pre")
            if code_block:
                # Format the code using jsbeautifier
                formatted_code = self.js_beautifier(code_block.text.strip())
                return formatted_code
        return ""

    async def generate_markdown(self):
        markdown_content = "# Market Data Feed Documentation\n\n"
        for item in self.content_list:
            markdown_content += item["content"]
            markdown_content += f"[Link to documentation]({item['url']})\n\n"
            markdown_content += "---\n\n"
        markdown_path = os.path.join(self.output_dir, "market_data_feed_documentation.md")
        with open(markdown_path, "w", encoding="utf-8") as md_file:
            md_file.write(markdown_content)
        logger.info(f"Markdown file saved to: {markdown_path}")

# The main function remains the same




async def main():
    parser = argparse.ArgumentParser(description="Scrape Market Data Feed API documentation and convert to Markdown")
    parser.add_argument("--timeout", type=int, default=30, help="Timeout for requests in seconds")
    args = parser.parse_args()

    output_dir = "market_data_feed_docs"
    os.makedirs(output_dir, exist_ok=True)

    urls = [
        "https://upstox.com/developer/api-documentation/example-code/login/get-token",
        "https://upstox.com/developer/api-documentation/example-code/login/logout",
        "https://upstox.com/developer/api-documentation/example-code/user/get-profile",
        "https://upstox.com/developer/api-documentation/example-code/user/get-fund-and-margin",
        "https://upstox.com/developer/api-documentation/example-code/charges/brokerage-details",
        "https://upstox.com/developer/api-documentation/example-code/orders/place-order",
        "https://upstox.com/developer/api-documentation/example-code/orders/modify-order",
        "https://upstox.com/developer/api-documentation/example-code/orders/cancel-order",
        "https://upstox.com/developer/api-documentation/example-code/orders/get-trades",
        "https://upstox.com/developer/api-documentation/example-code/portfolio/get-positions",
        "https://upstox.com/developer/api-documentation/example-code/historical-data/historical-candle-data",
        "https://upstox.com/developer/api-documentation/example-code/historical-data/intra-day-candle-data",
        "https://upstox.com/developer/api-documentation/example-code/market-quote/full-market-quotes",
        "https://upstox.com/developer/api-documentation/example-code/market-quote/ltp-quotes",
        "https://upstox.com/developer/api-documentation/example-code/market-quote/ohlc-quotes",
        "https://upstox.com/developer/api-documentation/example-code/option-chain/option-contracts",
        "https://upstox.com/developer/api-documentation/example-code/option-chain/put-call-option-chain"
    ]

    scraper = MarketDataFeedDocScraper(urls, output_dir, timeout=args.timeout)
    await scraper.scrape_documentation()
    logger.info(f"Total pages scraped: {len(scraper.visited_urls)}")

if __name__ == "__main__":
    asyncio.run(main())
