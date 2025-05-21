from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 🔐 LinkedIn Zugangsdaten
EMAIL = "mail"
PASSWORD = "password"
POST_TEXT = "Hi!"

# 🌐 Starte Safari WebDriver
driver = webdriver.Safari()
driver.get("https://www.linkedin.com/login")

# 🔐 Login durchführen
driver.find_element(By.ID, "username").send_keys(EMAIL)
driver.find_element(By.ID, "password").send_keys(PASSWORD + Keys.RETURN)

# ⏳ Warte bis Navigation geladen ist (sicheres Zeichen für vollständigen Login)
WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.ID, "global-nav-search"))
)

# 🔁 Feed aufrufen (manchmal lädt die Seite intern doppelt)
driver.get("https://www.linkedin.com/feed/")
time.sleep(3)  # kurz warten

# 🧭 Warte auf das Haupt-Feed-Modul („Beitrag beginnen“-Bereich)
WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'share-box-feed-entry__top-bar')]"))
)

# 🧩 Suche den „Beitrag beginnen“-Button über Textinhalt
post_button = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, "//button[contains(., 'Beitrag')]"))
)


# 🖱️ JavaScript-Click, um Blockaden zu umgehen
driver.execute_script("arguments[0].click();", post_button)

# ⏳ Warte auf das Textfeld
text_area = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "ql-editor"))
)

# 📝 Beitragstext eingeben
text_area.send_keys(POST_TEXT)
time.sleep(1)

# ✅ „Posten“-Button suchen & klicken
post_button_final = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Posten')]"))
)
driver.execute_script("arguments[0].click();", post_button_final)

# 🏁 Abschluss
print("✅ Beitrag wurde erfolgreich gepostet.")
time.sleep(5)
driver.quit()
