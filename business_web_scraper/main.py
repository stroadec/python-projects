from scraper.fetcher import fetch_page
from scraper.parser import parse_quotes
from scraper.exporter import export_csv
from pathlib import Path

URL = "https://quotes.toscrape.com"
OUTPUT_FILE = Path("data/output.csv")

def main():
    print("🌐 Fetching page...")
    html = fetch_page(URL)

    print("🔍 Parsing data...")
    quotes = parse_quotes(html)

    print("📤 Exporting data...")
    export_csv(quotes, OUTPUT_FILE)

    print("✅ Done! Data saved to data/output.csv")

if __name__ == "__main__":
    main()
