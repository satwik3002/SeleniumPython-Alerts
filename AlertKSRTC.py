from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Step 1: Launch the URL in the Chrome browser
driver = webdriver.Chrome()  # Ensure ChromeDriver is in PATH
driver.get("https://ksrtc.in/login")
driver.maximize_window()

# Step 2: Wait for the login page to load
time.sleep(5)  # Wait for 5 seconds to ensure the page is loaded

# Step 3: Find and click the "Login" button
login_button = driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[3]/div[4]")  # Original XPath
login_button.click()

# Step 4: Wait for the alert to appear and accept it
time.sleep(5)  # Wait for the alert to appear

Ok_button = driver.find_elements(By.ID, "okayButton")
time.sleep(3)

# Close the browser
driver.quit()