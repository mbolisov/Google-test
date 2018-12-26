# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
import page

class Google_search(unittest.TestCase):
    """ Тестирование поиска на сайте google.com"""

    def setUp(self):
        self.driver = webdriver.Chrome('/Applications/chromedriver')
        self.driver.get("https://www.google.com")

    def test_google_search(self):
        """
        Вбиваем в поисковике запрос "yandex.ru" и проверяем, что первая ссылка ( не реклама) ведет на искомый сайт
        """


        main_page = page.MainPage(self.driver)
        result_page = page.SearchResultsPage(self.driver)

        #Проверяем перешли ли мы на нужную страницу
        assert main_page.is_title_matches(), "Oops, it's not google main page"

        #Выполнение поиска по запросу "yandex.ru"
        main_page.search('yandex.ru')

        #Проверяем первую ссылку
        result_page.check_first_result('https://www.yandex.ru/')

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()