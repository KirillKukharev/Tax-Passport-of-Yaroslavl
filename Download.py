import os
import requests
import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
os.chdir('C:\\Users\\Кирилл\\Downloads\\PythonProject\\SaveDocuments')
# URL адреса для запроса ссылок на загрузку и имена таблиц
param_list = [
##    ('https://analytic.nalog.ru/portal/GetBLOB.htm', 'T_ANALYTICAL_INFORMATION'),
    ('https://analytic.nalog.ru/portal/GetLongRaw.htm', 'T_PASSPORTS'),
]

# Ниже можно указать через запятую ID файлов
id_list = [452,263,178,824,1191]

# Если не указано, то с 0 по 4999
if not id_list:
    id_list = range(5000)

for i in id_list:
    try:
        for load_url, table_name in param_list:
            data = {'ID': i, 'TABLE': table_name}

            # Получение ссылки на загрузку файла
            response = requests.post(load_url, data, timeout=3, verify=False)

            file_name = response.text.replace('files/', '')
            file_url = 'https://analytic.nalog.ru/portal/files/{}'.format(file_name)
            print('ид: {}, имя: {}, ссылка: {}'.format(i, file_name, file_url))

            if 'Истраченный набор результатов' not in file_name and 'Недопустимый тип столбца' not in file_name:
                # Загрузка файла
                response = requests.get(file_url, timeout=6, verify=False)
                # Сохранение файла в текущую папку
                with open(file_name, 'wb') as file:
                    file.write(response.content)

    except Exception as error:
        print(type(error), error)