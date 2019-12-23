import os
import numpy as np
os.chdir('C:\\Users\\Кирилл\\Downloads\\PythonProject\\SaveDocuments')
import pandas as pd

# Получаем файл на вход и редактируем информацию(обьединяем столбцы, убираем ненужные строки, переводим в нужный формат данных)
xls_file = pd.read_excel('FILE76_01.01.2015_263_263.xls', 'Раздел7', index_col=None)
os.chdir('C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2015')
xls_file[15:].to_csv('Седьмая часть2.csv', encoding='utf-8',sep=';',index=False)
df=pd.read_csv('Седьмая часть2.csv',sep=';', comment='#',index_col=None)
df = df.fillna('')
del df['Unnamed: 1']

# Изменяем формат данных в столбцах "Unnamed(i)" на float для округления
for i in range(3,10):
    k='Unnamed: '+ str(i)
    df[k]=np.where(df[k] == 'X','', df[k])
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
arrays = [['', 'По состоянию на 01.01.2016', 'По состоянию на 01.01.2016', 'По состоянию на 01.01.2016','По состоянию на 01.01.2016','Изменение за 2015 год','Изменение за 2015 год','Изменение за 2015 год','Изменение за 2015 год'], df.columns]
df.columns = pd.MultiIndex.from_arrays(arrays)
pd.set_option('max_colwidth', 1000)

# Сохраняем полученный результат в папке "html_tables"
os.chdir("C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2015\\html_tables")
df.to_html('Таблица_7(2015).html',index=False)




