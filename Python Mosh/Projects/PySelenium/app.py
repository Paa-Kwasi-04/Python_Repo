from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
browser.get("https:github.com")

signin_link = browser.find_element(By.LINK_TEXT, 'Sign in')

signin_link.click()
username_box = browser.find_element(By.ID, 'login_field')
username_box.send_keys('mk0_11')
password_box = browser.find_element(By.ID, 'password')
password_box.send_keys('Acity2023.')
password_box.submit()


assert 'mk0_11' in browser.page_source
