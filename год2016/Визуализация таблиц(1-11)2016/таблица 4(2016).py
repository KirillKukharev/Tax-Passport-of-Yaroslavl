import os
import numpy as np
os.chdir('C:\\Users\\Кирилл\\Downloads\\PythonProject\\SaveDocuments')
import pandas as pd

# Получаем файл на вход и редактируем информацию(обьединяем столбцы, убираем ненужные строки, переводим в нужный формат данных)
pd.options.display.float_format = '{:.1f}'.format
xls_file = pd.read_excel('FILE76_01.01.2016_178_178.xls', 'Раздел4', index_col=None)
os.chdir('C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2016')
xls_file[13:].to_csv('Четвертая часть3.csv', encoding='utf-8',sep=';',index=False)
df=pd.read_csv('Четвертая часть3.csv',sep=';', comment='#',index_col=None)
df = df.fillna('')
df = df.rename(columns={'Раздел 4.Основные показатели контрольной работы налоговых органов': 'ПОКАЗАТЕЛЬ', 'Unnamed: 2': '2016 год','Unnamed: 3':'В % к предыдущему году'})

del df['Unnamed: 1']
pd.set_option('max_colwidth', 1000)

# Сохраняем полученный результат в папке "html tablici"
os.chdir("C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2016\\html tablici")
df.to_html('Таблица_4(2016).html',index=False)