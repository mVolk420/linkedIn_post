
import generate_openai_post
from dotenv import load_dotenv
import os
import news_fetcher
from linkedin_handling import LinkedInHandler
import random
import time

load_dotenv()
# 🔐 LinkedIn Zugangsdaten
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

news = news_fetcher.fetch_news()
link = news_fetcher.get_link(news)
post_text = generate_openai_post.generate_post(news.title)
post_text += "\n" + link
linkedin_handler = LinkedInHandler()

linkedin_handler.log_in(EMAIL,PASSWORD)
linkedin_handler.post(post_text)

buttons_clicked = 0
while buttons_clicked < 99 :
    buttons_clicked += linkedin_handler.connect_with_all()
    time.sleep(random.uniform(0.3,1.6) )
linkedin_handler.quit()