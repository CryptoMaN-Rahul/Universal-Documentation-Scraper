# Upstox API Documentation Scraper

This project is a web scraper designed to extract and compile the Upstox API documentation into a single Markdown file. It focuses on capturing Node.js related code snippets while excluding code examples in other languages.

## Features

- Recursively scrapes the Upstox API documentation
- Extracts main content from each page
- Identifies and preserves Node.js code snippets
- Compiles all content into a single Markdown file
- Handles pagination and relative links

## Requirements

- Python 3.7+
- aiohttp
- beautifulsoup4
- html2text

## Installation

1. Clone this repository:

2. Install the required packages:
   pip install -r requirements.txt

## Usage

Run the script with default settings:

python main.py

You can customize the behavior with command-line arguments:

python main.py --url "https://upstox.com/developer/api-documentation" --max-pages 150 --timeout 60

- `--url`: The base URL of the API documentation (default: "https://upstox.com/developer/api-documentation")
- `--max-pages`: Maximum number of pages to scrape (default: 100)
- `--timeout`: Timeout for requests in seconds (default: 30)

## Output

The script will create a Markdown file named `market_data_feed_documentation.md` in the `market_data_feed_docs` directory. This file will contain the compiled documentation with Node.js code snippets.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
And here's the content for the requirements.txt file:
aiohttp==3.8.4
beautifulsoup4==4.10.0
html2text==2020.1.16
To use these files:
Save the README.md content to a file named
README.md
in your project's root directory.
Save the requirements.txt content to a file named
requirements.txt
in your project's root directory.
