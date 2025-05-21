import feedparser
import urllib.request
import random

TOPICS = [
    "Artificial Intelligence",
    "AI Technology",
    "Machine Learning",
    "Cloud Security",
    "Cybersecurity",
    "Data Privacy",
    "Digital Transformation",
    "Quantum Computing",
    "5G Technology",
    "Edge Computing",
    "Internet of Things",
    "IT Security",
    "Big Data",
    "Robotic Process Automation",
    "Augmented Reality",
    "Virtual Reality",
    "DevOps"
]

def fetch_news(topics=TOPICS, max_articles=5):
    all_entries = []
    headers = {'User-Agent': 'Mozilla/5.0'}  # Trick: echter Browser-Agent

    for topic in topics:
        query = topic.replace(" ", "+")
        url = f"https://news.google.com/rss/search?q={query}&hl=en&gl=US&ceid=US:en"
        print(f"⤵️ Lade News zu: {topic}")

        # Anfrage wie Browser simulieren
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            feed_content = response.read()

        feed = feedparser.parse(feed_content)

        if feed.entries:
            print(f"✅ {len(feed.entries[:max_articles])} Artikel gefunden")
            all_entries.extend(feed.entries[:max_articles])
        else:
            print(f"⚠️ Keine Artikel gefunden für Thema: {topic}")

    return all_entries

# Funktion 2: Nur Titel extrahieren
def get_titles(news_entries):
    return [entry.title for entry in news_entries]
