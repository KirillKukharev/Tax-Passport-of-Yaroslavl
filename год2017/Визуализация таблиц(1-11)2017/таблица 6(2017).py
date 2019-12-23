import os
import numpy as np
os.chdir('C:\\Users\\Кирилл\\Downloads\\PythonProject\\SaveDocuments')
import pandas as pd

# Получаем файл на вход и редактируем информацию(обьединяем столбцы, убираем ненужные строки, переводим в нужный формат данных)
pd.options.display.float_format = '{:.1f}'.format
xls_file = pd.read_excel('FILE76_01.01.2017_824_824.xls', 'Раздел6', index_col=None)
os.chdir('C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2017')
xls_file[8:].to_csv('Шестая часть4.csv', encoding='utf-8',sep=';',index=False)
df=pd.read_csv('Шестая часть4.csv',sep=';', comment='#',index_col=None)
df = df.fillna('')
df['Unnamed: 3'] = np.where(df['Unnamed: 3'] == 'X','', df['Unnamed: 3'])
df = df.rename(columns={'Раздел 6. Поступление доходов по страховым  взносам на обязательное социальное страхование в Российской Федерации': 'ПОКАЗАТЕЛЬ','Unnamed: 2':'Всего','Unnamed: 3':'В % к предыдущему периоду'})
del df['Unnamed: 1']
arrays = [['', 'Поступление доходов по страховым взносам на обязательное социальное страхование в Российской Федерации', 'Поступление доходов по страховым взносам на обязательное социальное страхование в Российской Федерации'], df.columns]
df.columns = pd.MultiIndex.from_arrays(arrays)
pd.set_option('max_colwidth', 1000)

# Сохраняем полученный результат в папке "html table"
os.chdir("C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2017\\html table")
df.to_html('Таблица_6(2017).html',index=False)