# Quote Scraper: Scrapes quotes from quotes.toscrape.com across multiple pages.
# Run in a terminal (e.g., `python quote_scraper.py`) for interactive prompts.

import requests
from bs4 import BeautifulSoup

def scrape_quotes(pages=2, keyword=None, output_file="quotes.txt"):
    quotes_list = []
    for page in range(1, pages + 1):
        url = f"http://quotes.toscrape.com/page/{page}"
        try:
            response = requests.get(url, timeout=5)
            if response.status_code != 200:
                print(f"Failed to load page {page}")
                continue
        except requests.RequestException as e:
            print(f"Error fetching page {page}: {e}")
            continue
        
        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.find_all("div", class_="quote")
        for quote in quotes:
            text = quote.find("span", class_="text").text.strip()
            author = quote.find("small", class_="author").text.strip()
            if keyword is None or keyword.lower() in text.lower():
                quotes_list.append(f"{text} - {author}")
    
    # Save to file
    if quotes_list:
        with open(output_file, "w", encoding="utf-8") as file:
            for i, quote in enumerate(quotes_list, 1):
                file.write(f"{i}. {quote}\n")
        print(f"Saved {len(quotes_list)} quotes to {output_file}")
    else:
        print("No quotes found matching your criteria.")

# Basic CLI
if __name__ == "__main__":
    pages = int(input("How many pages to scrape? (e.g., 2): ") or 2)
    keyword = input("Enter a keyword to filter (or press Enter for all): ") or None
    scrape_quotes(pages=pages, keyword=keyword)