import requests
from bs4 import BeautifulSoup

def fetch_words_simple(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; WordScraper/1.0; +https://example.com/bot)"
    }
    r = requests.get(url, headers=headers, timeout=15)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")

    words_3000 = set()
    words_5000 = set()

    for li in soup.select('li[data-hw]'):
        # skip items hidden via class="hidden"
        classes = li.get("class", [])
        if "hidden" in classes:
            continue

        word = li.get("data-hw").strip().lower()
        if not word:   # skip multi-word entries
            continue

        if li.has_attr("data-ox3000"):
            words_3000.add(word)

        if li.has_attr("data-ox5000"):
            words_5000.add(word)

    # deduplicate and sort on length
    words_3000 = sorted(words_3000, key=len)
    words_5000 = sorted(words_5000, key=len)

    with open("dictionary/oxford3000.txt", "w", encoding="utf-8") as f:
        for w in words_3000:
            f.write(w + "\n")

    print(f"Saved {len(words_3000)} words to dictionary/oxford3000.txt")

    with open("dictionary/oxford5000.txt", "w", encoding="utf-8") as f:
        for w in words_5000:
            f.write(w + "\n")

    print(f"Saved {len(words_5000)} words to dictionary/oxford5000.txt")

if __name__ == "__main__":
    url = "https://www.oxfordlearnersdictionaries.com/wordlists/oxford3000-5000"
    fetch_words_simple(url)
