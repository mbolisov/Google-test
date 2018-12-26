# Google-test

Тестирование поиска в системе Google.com

Краткое описание : 
Поисковая система Google.com принимает запрос и выдает корректные результаты поиска 

Шаги:
1. Загрузка домашней страницы google.com
2. Ввод в поисковую строку запроса "yandex.ru"
3. Загрузка страницы с результатами поиска : первая строка представляет собой ссылку на домашнюю страницу запрашиваемого сайта " https://www.yandex.ru"

Тест включает в себя три файла : test.py, locators.py,page.py

test.py : непосредственно файл теста : обращается к методам файла page.py, и вызывает их с заданными критериями 
page.py :  файл с описанием методов работы с учавствующими в тестировании страницами
locators.py : файл с описанием локаторов - обьектов страниы, которыми оперирует тест

Инструкция к запуску: 
1. В командной стркое прописать путь до хранения файлов ( cd %Путь% ) 
2. Ввести команду - python test.py
3. Тест запущен
