# LinkTool

LinkTool is a Python script that takes a markdown file with a list of URLs and generates an output markdown file containing `<a href>` tags, each with the title of the corresponding webpage.

## Requirements

This script requires Python 3.7 or later. Before running the script, you need to install the following Python packages:

- aiohttp
- aiofiles
- beautifulsoup4

You can install these packages using pip:

```bash
pip install aiohttp aiofiles beautifulsoup4
```

## Usage

To use LinkTool, run the Python script with the name of your markdown file as an argument:

```bash
python linktool.py your_markdown_file.md
```

Replace `your_markdown_file.md` with the name of your markdown file.

The script will fetch each URL in the input file, extract the title of the webpage, and create an `<a href>` tag with the URL and title. If the webpage cannot be reached or does not have a title, the URL is used as the title.

The output is a markdown file named `processed_links.md`, which contains the generated `<a href>` tags. This file is saved in the same directory as the input file.

If an error occurs while fetching a URL, the URL is printed to the console.

## Note

Some websites may block access from scripts or bots. If the script is unable to access a webpage and returns a 403 Forbidden HTTP status code, try running the script again later or check the website's terms of service. The script includes a User-Agent header to mimic a regular web browser, but this may not be sufficient for all websites.