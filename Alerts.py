from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up WebDriver
driver = webdriver.Chrome()  # Ensure ChromeDriver is in PATH

# Step 1: Launch the target webpage
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
time.sleep(5)  # Wait for the page to load

# Step 2: Find the button and click it
driver.find_element(By.XPATH, '//button[contains(text(),"Click for JS Alert")]').click()
time.sleep(4)

# Step 3: Handle the alert
driver.switch_to.alert.accept()  # Accept the alert

# Step 4: Retrieve the result
result = driver.find_element(By.ID, 'result').text
print("Value of attribute is: " + result)

# Step 5: Assertion to verify the result
assert "You successfully clicked an alert" in result, "Assertion Failed: Text did not match!"

# Step 6: JS Confirm Alert - Accept
driver.find_element(By.XPATH, "//button[contains(text(),'Click for JS Confirm')]").click()
time.sleep(4)
driver.switch_to.alert.accept()
result = driver.find_element(By.ID, 'result').text
print("Value of attribute is: " + result)
assert "You clicked: Ok" in result, "Assertion Failed: Text did not match!"

# Step 7: JS Confirm Alert - Dismiss
driver.find_element(By.XPATH, "//button[contains(text(),'Click for JS Confirm')]").click()
time.sleep(4)
driver.switch_to.alert.dismiss()
result = driver.find_element(By.ID, 'result').text
print("You Clicked: Cancel " + result)

# Step 8: JS Prompt Alert
driver.find_element(By.XPATH, "//button[contains(text(),'Click for JS Prompt')]").click()
time.sleep(4)
driver.switch_to.alert.send_keys('Raghavendra is a Good Mentor')
driver.switch_to.alert.accept()
result = driver.find_element(By.ID, 'result').text
print("Value of attribute is: " + result)
assert "You entered: Raghavendra is a Good Mentor" in result, "Assertion Failed: Text did not match!"

# Step 9: Basic Authentication
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
time.sleep(4)
value = driver.find_element(By.XPATH, "//p[contains(text(), 'Congratulations! You must have the proper credentials.')]").text
print("Value of attribute is: " + value)
assert 'Congratulations! You must have the proper credentials.' in value, "Assertion Failed: Text did not match!"

# Close the browser
driver.quit()
