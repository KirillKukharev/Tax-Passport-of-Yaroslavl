import os
import numpy as np
os.chdir('C:\\Users\\Кирилл\\Downloads\\PythonProject\\SaveDocuments')
import pandas as pd

# Получаем файл на вход и редактируем информацию(обьединяем столбцы, убираем ненужные строки, переводим в нужный формат данных)
pd.options.display.float_format = '{:.1f}'.format
xls_file = pd.read_excel('FILE76_01.01.2016_178_178.xls', 'Раздел7', index_col=None)
os.chdir('C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2016')
xls_file[14:].to_csv('Седьмая часть3.csv', encoding='utf-8',sep=';',index=False)
df=pd.read_csv('Седьмая часть3.csv',sep=';', comment='#',index_col=None)
df = df.fillna('')
for i in range(3,10):
    k='Unnamed: '+ str(i)
    df[k]=np.where(df[k] == 'X','', df[k])

# Изменяем формат данных в столбцах 'Unnamed(i)' на float для округления
for i in range(len(df['Unnamed: 3'])):
  try:
    for b in range(3,10):
        m='Unnamed: '+ str(b)
        if (df[m][i]!='') and  (df[m][i]!=m):
            df[m][i]=float(df[m][i])
            df[m][i]=round(df[m][i],3)
  except:
    continue
df = df.rename(columns={'Раздел 7.Задолженность по налогам и сборам в консолидированный бюджет Российской Федерации': 'ПОКАЗАТЕЛЬ','Unnamed: 2':'Всего','Unnamed: 3':'Недоимка','Unnamed: 4':'Отсроченные (рассроченные) платежи и реструктурированная задолженность','Unnamed: 5':'Приостановленные к взысканию платежи','Unnamed: 6':'Всего','Unnamed: 7':'Недоимка','Unnamed: 8':'Отсроченные (рассроченные) платежи и реструктурированная задолженность','Unnamed: 9':'Приостановленные к взысканию платежи'})
df = df.loc[df['ПОКАЗАТЕЛЬ'] != '1']
del df['Unnamed: 1']
arrays = [['', 'По состоянию на 01.01.2017', 'По состоянию на 01.01.2017', 'По состоянию на 01.01.2017','По состоянию на 01.01.2017','Изменение за 2016 год','Изменение за 2016 год','Изменение за 2016 год','Изменение за 2016 год'], df.columns]
df.columns = pd.MultiIndex.from_arrays(arrays)
pd.set_option('max_colwidth', 1000)

# Сохраняем полученный результат в папке "html tablici"
os.chdir("C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2016\\html tablici")
df.to_html('Таблица_7(2016).html',index=False)

