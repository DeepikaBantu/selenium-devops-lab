from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Setup Chrome options for headless mode
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Initialize driver
driver = webdriver.Chrome(options=options)

# Open an online sample site (GitHub Actions can't open local files)
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

print("Opened sample form successfully!")

# Interact with form fields
driver.find_element(By.NAME, "my-text").send_keys("Deepika")
driver.find_element(By.NAME, "my-password").send_keys("12345")
driver.find_element(By.CSS_SELECTOR, "button").click()

time.sleep(2)
print("Login simulation successful!")

driver.quit()
print("Test completed successfully ✅")
