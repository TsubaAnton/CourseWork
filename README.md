Данный код выводит на экран список из 5 последних выполненных операций.
Требования к окружению:
Python 3.11
Дополнительные библиотеки json и datetime
Другие зависимости указаны в файлах:
requirements.txt и pyproject.toml
Для того, чтобы запустить скрипты, необходимо использовать данный код:
filename = 'operations.json'
operations_data = read_operations(filename)
display_last_operations(operations_data)
Используется фреймворк pytest для тестирования кода
