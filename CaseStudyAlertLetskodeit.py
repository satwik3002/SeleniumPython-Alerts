from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Step 1: Launch the LetsKodeIt practice URL in Chrome
driver = webdriver.Chrome()  # Ensure ChromeDriver is in PATH
driver.get("https://www.letskodeit.com/practice")
driver.maximize_window()

# Step 2: Wait for the page to load
time.sleep(5)

# Step 3: Click the "Alert" button to handle the alert
alert_button = driver.find_element(By.ID, "alertbtn")  # ID of the alert button
alert_button.click()

# Step 4: Handle the simple alert and click "OK"
time.sleep(5)  # Wait for the alert to appear
alert = driver.switch_to.alert  # Switch to the alert
alert.accept()  # Click the 'OK' button to accept the alert

# Step 5: Click the "Confirm" button to handle the confirmation alert
confirm_button = driver.find_element(By.ID, "confirmbtn")  # ID of the confirm button
confirm_button.click()

# Step 6: Handle the confirmation alert and click "OK"
time.sleep(5)  # Wait for the confirmation alert to appear
alert = driver.switch_to.alert  # Switch to the alert
alert.accept()  # Click the 'OK' button to accept the confirmation

# Step 7: Click the "Cancel" button on the confirmation alert
confirm_button.click()  # Click the confirm button again
time.sleep(5)
alert = driver.switch_to.alert  # Switch to the confirmation alert again
alert.dismiss()  # Click 'Cancel' to dismiss the alert

# Step 8: Close the browser
driver.quit()
