import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

# ТЕСТ СОЗДАНИЕ АККАУНТА
# driver.get("http://practice.automationtesting.in/")
#
# myAcc_btn = driver.find_element(By.CSS_SELECTOR, "[href=\"http://practice.automationtesting.in/my-account/\"]").click()
#
# reg_email_field = driver.find_element(By.ID, "reg_email")
# reg_email_field.send_keys("hhhhow5@gmail.com")
# time.sleep(2)
#
# reg_password_field = driver.find_element(By.ID, "reg_password")
# reg_password_field.send_keys("1234qwer1234QWERgtrgdSDASDS")
#
# reg_btn = driver.find_element(By.CSS_SELECTOR, "[value=\"Register\"]").click()

# ТЕСТ ЛОГИН В СИСТЕМУ
driver.get("http://practice.automationtesting.in/")

myAcc_btn = driver.find_element(By.CSS_SELECTOR, "[href=\"http://practice.automationtesting.in/my-account/\"]").click()

username_field = driver.find_element(By.ID, "username")
username_field.send_keys("hhhhow5@gmail.com")

password_field = driver.find_element(By.ID, "password")
password_field.send_keys("1234qwer1234QWERgtrgdSDASDS")

log_btn = driver.find_element(By.CSS_SELECTOR, "[value=\"Login\"]").click()

signout = ".woocommerce-MyAccount-content [href=\"http://practice.automationtesting.in/my-account/customer-logout/\"]"
signout_btn = driver.find_element(By.CSS_SELECTOR, signout)
signout_btn_text = signout_btn.text
assert "Sign out" in signout_btn_text  #Доп проверка на этот эелемент)

logout = ".woocommerce-MyAccount-navigation [href=\"http://practice.automationtesting.in/my-account/customer-logout/\"]"
logout_btn = driver.find_element(By.CSS_SELECTOR, logout)
logout_btn_text = logout_btn.text
assert "Logout" in logout_btn_text


driver.quit()
