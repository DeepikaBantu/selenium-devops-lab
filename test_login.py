from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Launch browser
driver = webdriver.Chrome()

# Open your sample HTML file
driver.get("file:///C:/Users/bantu/OneDrive/Documents/labproject/index.html")
driver.maximize_window()

# Wait until page elements load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))

# Fill and click
driver.find_element(By.ID, "username").send_keys("Deepika")
driver.find_element(By.ID, "password").send_keys("12345")
driver.find_element(By.ID, "login-btn").click()

time.sleep(2)
print("Login button clicked successfully!")

# Close browser
driver.quit()
