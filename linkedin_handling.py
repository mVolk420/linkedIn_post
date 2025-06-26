from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

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
        post_button = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(., 'Beitrag')]"))
        )
        # 🖱️ JavaScript-Click, um Blockaden zu umgehen
        self.driver.execute_script("arguments[0].click();", post_button)

        # ⏳ Warte auf das Textfeld
        text_area = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, "ql-editor"))
        )
        # 📝 Beitragstext eingeben
        lines = post_text.split('\n')
        for line in lines:
            text_area.send_keys(line)
            text_area.send_keys(Keys.SHIFT, Keys.ENTER)  # SHIFT+ENTER für neuen Absatz (oft nötig bei JS-Feldern)
        time.sleep(random.uniform(7.0,8.0) )

        # ✅ „Posten“-Button suchen & klicken
        post_button_final = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Posten')]"))
        )
        self.driver.execute_script("arguments[0].click();", post_button_final)
        print("✅ Beitrag wurde erfolgreich gepostet.")

    def connect_with_all(self) -> int:
        clicked_count = 0

        # 🔁 Feed aufrufen (manchmal lädt die Seite intern doppelt)
        self.driver.get("https://www.linkedin.com/in/me/")
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(., 'Profilsprache')]"))
        )

        time.sleep(random.uniform(0.3, 1.6))

        # 🔍 Suche alle sichtbaren "Vernetzen"-Buttons
        buttons = self.driver.find_elements(By.XPATH, "//button[.//span[text()='Vernetzen']]")

        if not buttons:
            print("🔎 Keine 'Vernetzen'-Buttons gefunden.")
            return 0
        else:
            print(f"🔎 {len(buttons)} 'Vernetzen'-Buttons gefunden.")

        for idx, button in enumerate(buttons, 1):
            try:
                self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
                time.sleep(random.uniform(0.3, 1.6))
                self.driver.execute_script("arguments[0].click();", button)
                print(f"✅ Button {idx} gedrückt.")
                clicked_count += 1
                time.sleep(random.uniform(0.3, 1.6))

                # Optional: Bestätigen, falls ein Modal erscheint
                send_button = self.driver.find_elements(By.XPATH, "//button[contains(text(), 'Senden')]")
                if send_button:
                    send_button[0].click()
                    print(f"📨 Anfrage {idx} gesendet.")
                    time.sleep(random.uniform(0.3, 1.6))
            except Exception as e:
                print(f"❌ Fehler beim Klicken von Button {idx}: {e}")

        return clicked_count

    def quit(self):
        self.driver.quit()
