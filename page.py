# -*- coding: utf-8 -*-
from locators import MainPageLocators
from locators import SearchResultsPageLocators


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """Работа с домашней страницей google.com"""



    def search(self, srch):
        search_field = self.driver.find_element(*MainPageLocators.INPUT_FIELD)
        search_field.send_keys(srch)
        search_field.send_keys(u'\ue007')

    def is_title_matches(self):
        """Проверяет, что google в строке"""
        return "Google" in self.driver.title


class SearchResultsPage(BasePage):
    """Страница с результатами поиска"""


    def check_first_result(self, ref):
        """Проверяет, что первый результат соответсвует запросу"""
        first_link = self.driver.find_element(*SearchResultsPageLocators.FIRST_LINK)
        link_text = first_link.text
        assert link_text == ref , 'Oops, incorrect result'
