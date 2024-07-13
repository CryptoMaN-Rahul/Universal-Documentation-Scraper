

# Universal Documentation Scraper

This project is a versatile web scraper designed to extract and compile documentation from any given URL into a single Markdown file. It's particularly useful for creating offline copies of online documentation or for aggregating information from multiple pages into a single document.

## Features

- Recursively scrapes documentation from a given base URL
- Extracts main content from each page
- Identifies and preserves code snippets, attempting to detect the programming language
- Compiles all content into a single, well-structured Markdown file
- Handles pagination and relative links
- Configurable maximum page limit and request timeout

## Requirements

- Python 3.7+
- aiohttp
- beautifulsoup4
- html2text

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/CryptoMaN-Rahul/Universal-Documentation-Scraper
   cd Universal-Documentation-Scraper
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the script with a target documentation URL:

```
python main.py --url "https://docs.example.com"
```

You can customize the behavior with additional command-line arguments:

```
python main.py --url "https://docs.example.com" --max-pages 200 --timeout 60
```

Arguments:
- `--url`: The base URL of the documentation (required)
- `--max-pages`: Maximum number of pages to scrape (default: 100)
- `--timeout`: Timeout for requests in seconds (default: 30)

## Output

The script will create a Markdown file named `documentation.md` in the `documentation_output` directory. This file will contain the compiled documentation with preserved structure and code snippets.

## How It Works

1. The scraper starts from the provided base URL and extracts all links on the page.
2. It then visits each link that is within the same domain and path as the base URL.
3. For each page, it extracts the main content, preserving the structure.
4. Code blocks are identified, and the script attempts to determine the programming language.
5. All content is converted to Markdown format.
6. The process continues recursively until all discovered pages are scraped or the maximum page limit is reached.
7. Finally, all collected content is compiled into a single Markdown file.

## Limitations

- The script may not capture dynamically loaded content that requires JavaScript execution.
- Language detection for code snippets is based on simple heuristics and may not always be accurate.
- The effectiveness of content extraction may vary depending on the structure of the target website.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Now, here's the content for the requirements.txt file:

```
aiohttp==3.8.4
beautifulsoup4==4.10.0
html2text==2020.1.16
```

