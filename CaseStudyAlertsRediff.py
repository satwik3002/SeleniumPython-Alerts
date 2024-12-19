from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Step 1: Launch the URL in the Chrome browser
driver = webdriver.Chrome()  # Ensure ChromeDriver is in PATH
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
driver.maximize_window()

# Step 2: Wait for the page to load
time.sleep(5)

# Step 3: Find and click the "Sign in" button
sign_in_button = driver.find_element(By.NAME, "proceed")  # "proceed" is the name of the sign-in button
sign_in_button.click()

# Step 4: Wait for the alert to appear and accept it
time.sleep(5)  # Wait for the alert to appear
alert = driver.switch_to.alert  # Switch to the alert
alert.accept()  # Click the 'OK' button to accept the alert

# Close the browser
driver.quit()
