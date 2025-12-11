import asyncio
import aiohttp
from bs4 import BeautifulSoup
import argparse
from urllib.parse import urljoin, urlparse
import re

internal_urls = set()
found_emails = set()
domain_name = ""

def is_valid_url(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

async def get_all_emails_from_url(session, url):
    urls = set()
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
        async with session.get(url, ssl=False, headers=headers) as response:
            if response.status != 200:
                return urls
            text = await response.text()
            soup = BeautifulSoup(text, "html.parser")
            
            # Extract emails
            emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
            if emails:
                for email in emails:
                    if email not in found_emails:
                        print(f"[+] Found email: {email}")
                        found_emails.add(email)

    except Exception as e:
        return urls

    for a_tag in soup.find_all("a"):
        href = a_tag.attrs.get("href")
        if href == "" or href is None:
            continue
        href = urljoin(url, href)
        parsed_href = urlparse(href)
        href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
        if not is_valid_url(href):
            continue
        if href in internal_urls:
            continue
        if not parsed_href.netloc.endswith(domain_name):
            continue
        urls.add(href)
        internal_urls.add(href)
    if urls:
        print(f"[+] Found {len(urls)} links on {url}")
    return urls

async def crawl(url):
    global domain_name
    domain_name = urlparse(url).netloc

    urls_to_visit = {url}
    crawled_urls = set()

    async with aiohttp.ClientSession() as session:
        while urls_to_visit:
            
            crawl_batch = set()
            while urls_to_visit:
                url_to_add = urls_to_visit.pop()
                if url_to_add not in crawled_urls:
                    crawl_batch.add(url_to_add)

            if not crawl_batch:
                break

            tasks = {asyncio.create_task(get_all_emails_from_url(session, u)) for u in crawl_batch}
            crawled_urls.update(crawl_batch)
            print(f"[*] Crawling {len(crawl_batch)} URLs...")

            done, pending = await asyncio.wait(tasks)

            for task in done:
                new_links = task.result()
                for link in new_links:
                    if link not in crawled_urls and link not in urls_to_visit:
                        urls_to_visit.add(link)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="email_theifer.py", description="Web crawler to extract emails from a website.")
    parser.add_argument("url", nargs='?', default=None, help="The URL to start crawling from.")
    parser.add_argument("-f", "--file", help="A file containing multiple URLs to crawl.")
    parser.add_argument("-o", "--output", help="The output file to save the results to.", default="emails.txt")
    args = parser.parse_args()

    if not args.url and not args.file:
        parser.print_help()
        exit()

    urls_to_crawl = set()
    if args.url:
        urls_to_crawl.add(args.url)
    if args.file:
        with open(args.file, 'r') as f:
            for line in f:
                urls_to_crawl.add(line.strip())

    async def main():
        for url in urls_to_crawl:
            global internal_urls
            internal_urls = set()
            await crawl(url)

    asyncio.run(main())

    with open(args.output, "w") as f:
        for email in sorted(found_emails):
            print(email, file=f)
