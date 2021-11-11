# 1. Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя
# пользователя и почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден,
# выбросить исключение ValueError. Пример:
#
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru
#

import re

email = input("Input email: ")


def email_parse(email_adress):
    # обьявляем словарь result_dict

    result_dict = {}
    # Создаем правило парсинга email адреса
    # 1) Для пользователя:
    #       - первый символ не может быть . ((?<!\.). а должен быть [A-Za-z0-9!#$%&'*+/=?^_`{|}~-]
    #       - следующие символы  [A-Za-z0-9!#$%&'*+/=?^_`{|}~-]*
    #       - последний смвол не может быть (?<!\.). проверяем его до '@'
    # 2) разрешено только 1 вхождение символа '@'
    # 3) Для домена:
    #       - проверяем до .:
    #           - первый символ не может быть числом или '-', он должен быть буквой или цифрой (?<![0-9-])[a-zA-Z]
    #           - следующие символы, если они есть должны быть [A - Za - z0 - 9-]*
    #           - последний символна может быть '-'. проверяем до точки (?<![-])
    #       - разрешено только одно вхождение символа .
    #       - после точки богут быть любые буквы t: [a-zA-Z]+
    RE_EMAIL = re.compile(
        r"^((?<!\.)[A-Za-z0-9!#$%&'*+/=?^_`{|}~-][A-Za-z0-9!#$%&'*+./=?^_`{|}~-]*)(?<!\.)@((?<![0-9-])[a-zA-Z][a-zA-Z0-9-]*(?<![-])[.][a-zA-Z]+)$")
    # если функция выполнилась
    if RE_EMAIL.match(email_adress):
        # добовляем данные в словарь
        result_dict['username'] = RE_EMAIL.findall(email_adress)[0][0]
        result_dict['domain'] = RE_EMAIL.findall(email_adress)[0][1]
        # двозвращаем словарь
        return (result_dict)
    else:
        # в других члучаях двозвращаем ошибку
        raise ValueError(f'wrong email: {email_adress}')


print(email_parse(email), '\n')

