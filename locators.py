# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """Локаторы домашней страницы Google"""
    INPUT_FIELD = (By.NAME, 'q')

class SearchResultsPageLocators(object):
    """Локаторы страницы результатов поиска"""


    FIRST_LINK = (By.CSS_SELECTOR, 'cite.iUh30')
