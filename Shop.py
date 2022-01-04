import time
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

# ТЕСТ НА ОТОБРАЖЕНИЕ СТРАНИЦЫ ТОВАРА

# driver.get("http://practice.automationtesting.in/")
#
# myAcc_btn = driver.find_element(By.CSS_SELECTOR, "[href=\"http://practice.automationtesting.in/my-account/\"]").click()
#
# username_field = driver.find_element(By.ID, "username")
# username_field.send_keys("hhhhow5@gmail.com")
#
# password_field = driver.find_element(By.ID, "password")
# password_field.send_keys("1234qwer1234QWERgtrgdSDASDS")
#
# log_btn = driver.find_element(By.CSS_SELECTOR, "[value=\"Login\"]").click()
#
# shop_btn = driver.find_element(By.CSS_SELECTOR, ".main-nav [href=\"http://practice.automationtesting.in/shop/\"]")
# shop_btn.click()
# driver.execute_script("window.scrollBy(0,450);")
# time.sleep(2)
#
# book_HTML5 = driver.find_element(By.CSS_SELECTOR, ".post-181 .attachment-shop_catalog").click()
# time.sleep(2)
#
# title_HTML5 = driver.find_element(By.TAG_NAME, "h1")
# title_HTML5_text = title_HTML5.text
# assert "HTML5 Forms" in title_HTML5_text

# ТЕСТ НА КОЛИЧЕСТВО ТОВАРОВ В КАТЕГОРИИ

# driver.get("http://practice.automationtesting.in/")
#
# myAcc_btn = driver.find_element(By.CSS_SELECTOR, "[href=\"http://practice.automationtesting.in/my-account/\"]").click()
#
# username_field = driver.find_element(By.ID, "username")
# username_field.send_keys("hhhhow5@gmail.com")
#
# password_field = driver.find_element(By.ID, "password")
# password_field.send_keys("1234qwer1234QWERgtrgdSDASDS")
#
# log_btn = driver.find_element(By.CSS_SELECTOR, "[value=\"Login\"]").click()
#
# shop_btn = driver.find_element(By.CSS_SELECTOR, ".main-nav [href=\"http://practice.automationtesting.in/shop/\"]")
# shop_btn.click()
#
# html = "[href=\"http://practice.automationtesting.in/product-category/html/\"]"
# html_category = driver.find_element(By.CSS_SELECTOR, html).click()
#
# products_number = driver.find_elements(By.CSS_SELECTOR, ".product")
# if len(products_number) == 3:
#     print("Выставлено 3 товара")
# else:
#     print("Должно быть выставлено 3 товара, а выставлено: " + str(len(products_number)))


# ТЕСТ НА СОРТИРОВКУ ТОВАРОВ

# driver.get("http://practice.automationtesting.in/")
#
# myAcc_btn = driver.find_element(By.CSS_SELECTOR, "[href=\"http://practice.automationtesting.in/my-account/\"]").click()
#
# username_field = driver.find_element(By.ID, "username")
# username_field.send_keys("hhhhow5@gmail.com")
#
# password_field = driver.find_element(By.ID, "password")
# password_field.send_keys("1234qwer1234QWERgtrgdSDASDS")
#
# log_btn = driver.find_element(By.CSS_SELECTOR, "[value=\"Login\"]").click()
#
# shop_btn = driver.find_element(By.CSS_SELECTOR, ".main-nav [href=\"http://practice.automationtesting.in/shop/\"]")
# shop_btn.click()
#
# # sort_slector = driver.find_element(By.CSS_SELECTOR, ".woocommerce-ordering")
# # sort_slector_default = sort_slector.text
# # assert "Default sorting" in sort_slector_default   # Проверка по тексту
#
# sort_slector = driver.find_element(By.CSS_SELECTOR, ".orderby")
# sort_slector_default = sort_slector.get_attribute("value")
# assert "menu_order" == str(sort_slector_default)
#
# sort_slector = driver.find_element(By.CSS_SELECTOR, ".orderby")
# select = Select(sort_slector)
# select.select_by_value("price-desc")
#
# sort_slector = driver.find_element(By.CSS_SELECTOR, ".orderby")
# select = Select(sort_slector)
# select.select_by_value("price-desc")
#
# sort_slector = driver.find_element(By.CSS_SELECTOR, ".orderby")
# sort_slector_default = sort_slector.get_attribute("value")
# assert "price-desc" == str(sort_slector_default)


# ТЕСТ НА ОТОБРАЖЕНИЕ СКИДКИ ТОВАРА


# driver.get("http://practice.automationtesting.in/")
#
# myAcc_btn = driver.find_element(By.CSS_SELECTOR, "[href=\"http://practice.automationtesting.in/my-account/\"]").click()
#
# username_field = driver.find_element(By.ID, "username")
# username_field.send_keys("hhhhow5@gmail.com")
#
# password_field = driver.find_element(By.ID, "password")
# password_field.send_keys("1234qwer1234QWERgtrgdSDASDS")
#
# log_btn = driver.find_element(By.CSS_SELECTOR, "[value=\"Login\"]").click()
#
# shop_btn = driver.find_element(By.CSS_SELECTOR, ".main-nav [href=\"http://practice.automationtesting.in/shop/\"]")
# shop_btn.click()
# driver.execute_script("window.scrollBy(0,450);")
#
# book_android = driver.find_element(By.CSS_SELECTOR, "[title=\"Android Quick Start Guide\"]").click()
#
# old_count = driver.find_element(By.CSS_SELECTOR, "del .woocommerce-Price-amount.amount")
# old_count_text = old_count.text
# assert "₹600.00" == str(old_count_text)
#
# new_count = driver.find_element(By.CSS_SELECTOR, "ins .woocommerce-Price-amount.amount")
# new_count_text = new_count.text
# assert "₹450.00" == str(new_count_text)
#
# wait = WebDriverWait(driver, 5)
# open_img_of_book = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[title=\"Android Quick Start Guide\"]")))
# open_img_of_book.click()
#
# close_img_of_book = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
# close_img_of_book.click()


# ТЕСТ НА ПРОВЕРКУ ЦЕНЫ В КОРЗИНЕ


# driver.get("http://practice.automationtesting.in/")
#
# shop_btn = driver.find_element(By.CSS_SELECTOR, ".main-nav [href=\"http://practice.automationtesting.in/shop/\"]")
# shop_btn.click()
# driver.execute_script("window.scrollBy(0,450);")
#
# book_htmlWebApp = driver.find_element(By.CSS_SELECTOR, "[title=\"HTML5 Web Application Development Beginner's guide\"]")
# book_htmlWebApp.click()
#
# book_count = driver.find_element(By.CSS_SELECTOR, "[type=\"number\"]")
# book_count_value = book_count.get_attribute("value")
# assert "1" == book_count_value
#
# book_cost = driver.find_element(By.CSS_SELECTOR, "p .woocommerce-Price-amount.amount")
# book_cost_price = book_cost.text
# assert "₹180.00" == str(book_cost_price)
#
# addToCart_btn = driver.find_element(By.CSS_SELECTOR, ".single_add_to_cart_button.button.alt").click()
#
# basket_btn = driver.find_element(By.CSS_SELECTOR, ".button.wc-forward").click()
#
# wait = WebDriverWait(driver, 10)
# subtotal_field = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[data-title=\"Subtotal\"]"), "₹180.00"))
#
# total_field = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total [data-title=\"Total\"]"), "₹189.00"))


# ТЕСТ ПО РАБОТЕ В КОРЗИНЕ


# driver.get("http://practice.automationtesting.in/")
#
# shop_btn = driver.find_element(By.CSS_SELECTOR, ".main-nav [href=\"http://practice.automationtesting.in/shop/\"]")
# shop_btn.click()
# driver.execute_script("window.scrollBy(0,450);")
#
# book_htmlWebApp = driver.find_element(By.CSS_SELECTOR, "[title=\"HTML5 Web Application Development Beginner's guide\"]")
# book_htmlWebApp.click()
# driver.execute_script("window.scrollBy(0,300);")
# addToCart_btn = driver.find_element(By.CSS_SELECTOR, ".single_add_to_cart_button.button.alt").click()
# time.sleep(1)
#
# shop_btn = driver.find_element(By.CSS_SELECTOR, ".main-nav [href=\"http://practice.automationtesting.in/shop/\"]")
# shop_btn.click()
# driver.execute_script("window.scrollBy(0,650);")
#
# book_JS_Data = driver.find_element(By.CSS_SELECTOR, "[title=\"Learning JavaScript Data Structures and Algorith\"]")
# book_JS_Data.click()
# driver.execute_script("window.scrollBy(0,300);")
# addToCart_btn = driver.find_element(By.CSS_SELECTOR, ".single_add_to_cart_button.button.alt").click()
#
# basket_btn = driver.find_element(By.CSS_SELECTOR, ".button.wc-forward").click()
#
# remove_1st_book_btn = driver.find_element(By.CSS_SELECTOR, "[data-product_id=\"182\"]").click()
# time.sleep(5)
#
# quantity_field = driver.find_element(By.CSS_SELECTOR, "[title=\"Qty\"]")
# quantity_field.clear()
# quantity_field.send_keys("3")
#
# update_basket = driver.find_element(By.CSS_SELECTOR, "[value=\"Update Basket\"]").click()
#
# quantity_field_count = quantity_field.get_attribute("value")
# assert "3" == str(quantity_field_count)
# time.sleep(3)
#
# coupon_btn = driver.find_element(By.CSS_SELECTOR, "[value=\"Apply Coupon\"]").click()
#
# error_field = driver.find_element(By.CSS_SELECTOR, ".woocommerce-error")
# error_field_text = error_field.text
# assert "Please enter a coupon code." == error_field_text


# ТЕСТ НА ПОКУПКУ ТОВАРА


driver.get("http://practice.automationtesting.in/")

shop_btn = driver.find_element(By.CSS_SELECTOR, ".main-nav [href=\"http://practice.automationtesting.in/shop/\"]")
shop_btn.click()
driver.execute_script("window.scrollBy(0,300);")

book_htmlWebApp = driver.find_element(By.CSS_SELECTOR, "[title=\"HTML5 Web Application Development Beginner's guide\"]")
book_htmlWebApp.click()
driver.execute_script("window.scrollBy(0,300);")
addToCart_btn = driver.find_element(By.CSS_SELECTOR, ".single_add_to_cart_button.button.alt").click()

basket_btn = driver.find_element(By.CSS_SELECTOR, ".button.wc-forward").click()

wait = WebDriverWait(driver, 20)
checkout_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button.button.alt.wc-forward")))
checkout_btn.click()

firstname_field = wait.until(EC.element_to_be_clickable((By.ID, "billing_first_name")))
firstname_field.send_keys("Gleb")

lastname_field = driver.find_element(By.ID, "billing_last_name")
lastname_field.send_keys("Lyrchikov")

email_field = driver.find_element(By.ID, "billing_email")
email_field.send_keys("hhhhow5@gmail.com")

phone_field = driver.find_element(By.ID, "billing_phone")
phone_field.send_keys("89887402626")

country_selector = driver.find_element(By.ID, "select2-chosen-1").click()
country_selector_field = driver.find_element(By.ID, "s2id_autogen1_search")
country_selector_field.send_keys("Russia")
country_selector1 = driver.find_element(By.ID, "select2-results-1").click()


address_field = driver.find_element(By.ID, "billing_address_1")
address_field.send_keys("asdadasdadasdaasd")

city_field = driver.find_element(By.ID, "billing_city")
city_field.send_keys("Severodvinsk")

county_field = driver.find_element(By.ID, "billing_state")
county_field.send_keys("ASddasdawqd")

postcode_field = driver.find_element(By.ID, "billing_postcode")
postcode_field.send_keys("164500")
driver.execute_script("window.scrollBy(0,600);")
time.sleep(2)

radiobtn = driver.find_element(By.CSS_SELECTOR, "[value=\"cheque\"]")
driver.execute_script("return arguments[0].scrollIntoView(true);", radiobtn)
time.sleep(2)
radiobtn.click()


place_order_btn = driver.find_element(By.ID, "place_order").click()

received_field = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))

payment_method_field = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tfoot tr:nth-child(3) > td"), "Check Payments"))


driver.quit()
