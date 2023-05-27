import asyncio
import aiohttp
import aiofiles
import argparse
from bs4 import BeautifulSoup
import os

async def fetch(session, url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    try:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                return await response.text()
            else:
                print(f"Error occurred when fetching {url}. HTTP Status: {response.status}")
                return None
    except Exception as e:
        print(f"Error occurred when fetching {url}. Exception: {str(e)}")
        return None


async def get_title(session, url):
    page_content = await fetch(session, url)
    if page_content is not None:
        soup = BeautifulSoup(page_content, 'html.parser')
        title = soup.title.string.replace('\n', '') if soup.title else url
        return title
    else:
        return url


async def create_href_list(filename):
    async with aiofiles.open(filename, mode='r') as f:
        urls = [url.strip() for url in await f.readlines()]

    async with aiohttp.ClientSession() as session:
        tasks = [get_title(session, url) for url in urls]
        titles = await asyncio.gather(*tasks)

    href_list = [f'<a href="{url}">{title}</a>' for url, title in zip(urls, titles)]
    return href_list

async def write_to_file(directory, href_list):
    async with aiofiles.open(os.path.join(directory, 'processed_links.md'), mode='w') as f:
        await f.write('\n'.join(href_list))

def main():
    parser = argparse.ArgumentParser(description="Generate list of href tags from URLs in a markdown file.")
    parser.add_argument('mdfile', help="Markdown file with URLs")
    args = parser.parse_args()

    directory = os.path.dirname(args.mdfile)
    href_list = asyncio.run(create_href_list(args.mdfile))
    asyncio.run(write_to_file(directory, href_list))

if __name__ == "__main__":
    main()
