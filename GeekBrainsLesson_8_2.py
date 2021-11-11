# 2. * (вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
#
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) для получения
# информации вида: (<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>,
# <response_size>), например:
#
# raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian
# APT-HTTP/1.3 (0.9.7.9)"' parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET',
# '/downloads/product_2', '304', '0')
#
# Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле? Были ли особенные строки?
# Можно ли для них уточнить регулярное выражение?

# подключаем библиотеки requests и re
import requests
import re
# обявляем путь до файла
link = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
# считываем даныые из файла удаленно
link_content = requests.get(link).content.decode(encoding=requests.get(link).encoding)

# парсим
RE_PARCED = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*\[(.*)\].*"(\S{3})\s(\S*)\s\S*\s(\d+)\s(\d+)')
# выводим результат
for i in RE_PARCED.findall(link_content):
    print(i)