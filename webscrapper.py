import requests
from bs4 import BeautifulSoup

def scrape_bbc_headlines():
    url = "https://www.bbc.com/news"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print("❌ Error fetching the website:", e)
        return

    soup = BeautifulSoup(response.text, "html.parser")

    # Extract headlines (BBC uses 'gs-c-promo-heading__title')
    headlines = soup.find_all("h3", class_="gs-c-promo-heading__title")

    if not headlines:
        print("⚠️ Could not find headlines. Website structure may have changed.")
        return

    print("📰 Top BBC News Headlines:")
    print("=" * 50)
    for i, headline in enumerate(headlines[:10], 1):  # Show top 10
        print(f"{i}. {headline.get_text(strip=True)}")

if __name__ == "__main__":
    scrape_bbc_headlines()
