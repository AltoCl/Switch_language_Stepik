import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
    def open(self):
        self.browser.get(self.url)

def test_switch_languag(browser):
   link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/" 
   page = BasePage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
   page.open()                      # открываем страницу
   button = browser.find_element_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket")
   assert button, \
   f"Кнопка не найдена"
   time.sleep(20)