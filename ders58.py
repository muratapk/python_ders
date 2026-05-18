from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Driver başlat
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

# Google aç
driver.get("https://www.google.com")

# Sayfanın yüklenmesini bekle
time.sleep(2)

# Arama kutusunu bul
aramaKutusu = driver.find_element(By.NAME, "q")

# Yazı yaz
aramaKutusu.send_keys("Sabah Gazetesi")

# Enter tuşuna bas
aramaKutusu.send_keys(Keys.ENTER)

# 10 saniye bekle
time.sleep(30)

# Tarayıcıyı kapat
driver.quit()