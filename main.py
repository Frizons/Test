# Task_1

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options
import time

URL = "https://go.slotimo.com/login/"

chrome_driver = uc.Chrome()
chrome_driver.get(URL)

try:
    WebDriverWait(chrome_driver, 10).until(
        expected_conditions.presence_of_element_located(
            (By.CSS_SELECTOR, "div.login-form")
        )
    )
    find_tag_form_head = chrome_driver.find_element(By.TAG_NAME, "h2")
    find_tag_form_body = chrome_driver.find_element(By.TAG_NAME, "form")

    form_head_content = find_tag_form_head.get_attribute("innerHTML")
    form_body_content = find_tag_form_body.get_attribute("innerHTML")

    print(f"{form_head_content} {form_body_content}")

finally:
    chrome_driver.quit()



# Task_2

import requests
from bs4 import BeautifulSoup

PROX = {"91.65.103.3": "80"}
URL = "https://www.woocasino.com/promotions"

get_page = requests.get(URL, proxies=PROX)
get_content = get_page.text
soup_obj = BeautifulSoup(get_content, "html.parser")
find_content = soup_obj.find_all("div", class_="promotions-single__content")

for promotion in find_content:
    get_name_promotion = promotion.contents[0].string
    get_condition_promotion = promotion.contents[1].string

    print(f"Name promotion: {get_name_promotion}, Condition: {get_condition_promotion}")



# Task_3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

URL = "https://betandyou-227625.top/pl/bonus/rules"

edge_options = Options()
edge_options.add_argument("--headless")
driver = webdriver.Edge(options=edge_options)
driver.get(URL)

try:
    WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located(
            (By.CSS_SELECTOR, "span.bonuses-bonus-tile-name__caption")
        )
    )
    find_tag_bonuses = driver.find_elements(
        By.CSS_SELECTOR, "span.bonuses-bonus-tile-name__caption"
    )
    print(f"Total count bonuses: {len(find_tag_bonuses)}")

    for element in find_tag_bonuses:
        name_bonus = element.get_attribute("innerText")
        print(f"Name: {name_bonus}")

finally:
    driver.quit()

