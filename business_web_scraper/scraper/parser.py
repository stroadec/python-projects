from bs4 import BeautifulSoup

def parse_quotes(html: str) -> list[dict]:
    soup = BeautifulSoup(html, "html.parser")
    quotes_data = []

    quotes = soup.find_all("div", class_="quote")
    for quote in quotes:
        text = quote.find("span", class_="text").get_text(strip=True)
        author = quote.find("small", class_="author").get_text(strip=True)

        quotes_data.append({
            "quote": text,
            "author": author
        })

    return quotes_data
