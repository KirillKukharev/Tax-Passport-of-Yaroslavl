import os
import numpy as np
os.chdir('C:\\Users\\Кирилл\\Downloads\\PythonProject\\SaveDocuments')
import pandas as pd

# Получаем файл на вход и редактируем информацию(обьединяем столбцы, убираем ненужные строки, переводим в нужный формат данных)
pd.options.display.float_format = '{:.1f}'.format
xls_file = pd.read_excel('FILE76_01.01.2017_824_824.xls', 'Раздел3', index_col=None)
os.chdir('C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2017')
xls_file[7:].to_csv('Третья часть4.csv', encoding='utf-8',sep=';',index=False)
df=pd.read_csv('Третья часть4.csv',sep=';', comment='#',index_col=None)
df = df.fillna('')
df = df.rename(columns={'Раздел 3. Льготы по отдельным администрируемым доходам': 'ПОКАЗАТЕЛЬ', 'Unnamed: 2': '2017 год','Unnamed: 3':'В % к предыдущему году'})
del df['Unnamed: 1']
df = df.loc[df['ПОКАЗАТЕЛЬ'] != 'из стр. 310:']
pd.set_option('max_colwidth', 1000)

# Сохраняем полученный результат в папке "html table"
os.chdir("C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2017\\html table")
df.to_html('Таблица_3(2017).html',index=False)