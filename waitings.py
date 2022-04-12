import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import capture

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
    browser.find_element_by_id('book').click()

    value = browser.find_element_by_id('input_value').text
    browser.find_element_by_id('answer').send_keys(capture.calc(value))
    browser.find_element_by_id('solve').click()

finally:
    time.sleep(10)
    browser.quit()