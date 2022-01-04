import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

# ТЕСТ НА ДОБАВЛЕНИЕ КОММЕНТАРИЯ

driver.get("http://practice.automationtesting.in/")
driver.execute_script("window.scrollBy(0,600);")
seleniumRuby_btn = driver.find_element(By.CSS_SELECTOR, ".text-22-sub_row_1-0-2-0-0 .attachment-shop_catalog").click()
review_btn = driver.find_element(By.CSS_SELECTOR, "[href=\"#tab-reviews\"]").click()
star5_selector = driver.find_element(By.CSS_SELECTOR, ".star-5").click()

comment_field = driver.find_element(By.ID, "comment")
comment_field.send_keys("Nice book!")

author_field = driver.find_element(By.ID, "author")
author_field.send_keys("Gleb")
time.sleep(2)

email_field = driver.find_element(By.ID, "email")
email_field.send_keys("hhhhow5@gmail.com")

submit_btn = driver.find_element(By.ID, "submit").click



driver.quit()
