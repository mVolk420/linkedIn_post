from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LinkedInHandler:
    def __init__(self):
        # 🌐 Starte Safari WebDriver
        self.driver = webdriver.Safari()
    
    def log_in(self, email:str, password:str):
        self.driver.get("https://www.linkedin.com/login")
        # 🔐 Login durchführen
        self.driver.find_element(By.ID, "username").send_keys(email)
        self.driver.find_element(By.ID, "password").send_keys(password + Keys.RETURN)
        # ⏳ Warte bis Navigation geladen ist (sicheres Zeichen für vollständigen Login)
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.ID, "global-nav-search"))
        )
    
    def post(self, post_text:str):
        # 🔁 Feed aufrufen (manchmal lädt die Seite intern doppelt)
        self.driver.get("https://www.linkedin.com/feed/")
        # 🧭 Warte auf das Haupt-Feed-Modul („Beitrag beginnen“-Bereich)
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'share-box-feed-entry__top-bar')]"))
        )
        # 🧩 Suche den „Beitrag beginnen“-Button über Textinhalt
        post_button = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(., 'Beitrag')]"))
        )
        # 🖱️ JavaScript-Click, um Blockaden zu umgehen
        self.driver.execute_script("arguments[0].click();", post_button)

        # ⏳ Warte auf das Textfeld
        text_area = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "ql-editor"))
        )
        # 📝 Beitragstext eingeben
        text_area.send_keys(post_text)
        time.sleep(1)

        # ✅ „Posten“-Button suchen & klicken
        post_button_final = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Posten')]"))
        )
        self.driver.execute_script("arguments[0].click();", post_button_final)
        print("✅ Beitrag wurde erfolgreich gepostet.")

    def quit(self):
        self.driver.quit()
