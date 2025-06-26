from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
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
    "Edge Computing",
    "Internet of Things",
    "IT Security",
    "Big Data",
    "Robotic Process Automation",
    "Augmented Reality",
    "Virtual Reality",
    "DevOps"
]

def fetch_news(topics=TOPICS):
    headers = {'User-Agent': 'Mozilla/5.0'}  # Trick: echter Browser-Agent

    topic = topics[random.randint(0, len(topics) -1)]
    query = topic.replace(" ", "+")
    url = f"https://news.google.com/rss/search?q={query}&hl=en&gl=US&ceid=US:en"
    print(f"⤵️ Lade News zu: {topic}")

    # Anfrage wie Browser simulieren
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as response:
        feed_content = response.read()

    feed = feedparser.parse(feed_content)

    if feed.entries:
        print(f"✅ Artikel gefunden")
        entrie = feed.entries[0]
        return entrie
    else:
        print(f"⚠️ Keine Artikel gefunden für Thema: {topic}") 

def get_link(news_entrie):
    driver = webdriver.Safari()
    driver.get(news_entrie.link)
    cookie_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Alle')]"))
    )
    driver.execute_script("arguments[0].click();", cookie_button)
    time.sleep(2)
    final_url = driver.current_url

    print("Finale URL:", final_url)
    driver.quit()
    return final_url
