import os
import numpy as np
os.chdir('C:\\Users\\Кирилл\\Downloads\\PythonProject\\SaveDocuments')
import pandas as pd

# Получаем файл на вход и редактируем информацию(обьединяем столбцы, убираем ненужные строки, переводим в нужный формат данных)
xls_file = pd.read_excel('FILE76_01.01.2014_452_452.xls', 'Раздел11', index_col=None)
os.chdir('C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2014')
xls_file[4:].to_csv('Одиннадцатая часть.csv', encoding='utf-8',sep=';',index=False)
df=pd.read_csv('Одиннадцатая часть.csv',sep=';', comment='#',index_col=None)
df = df.fillna('')

# Изменяем формат данных в столбцах "Unnamed(i)" на float для округления
for i in range(len(df['Unnamed: 3'])):
  try:
    for b in range(2,5):
        m='Unnamed: '+ str(b)
        if (df[m][i]!='') and  (df[m][i]!=m):
            df[m][i]=float(df[m][i])
            df[m][i]=round(df[m][i],2)
  except:
    continue
for b in range(2,5):
    p='Unnamed: '+ str(b)
    df[p]=np.where(df[p] == 'X','', df[p])

df = df.rename(columns={'Раздел 11.Оценка и прогнозирование поступлений отдельных налогов': 'ПОКАЗАТЕЛЬ','Unnamed: 2':'2014 год (базисный год - факт)','Unnamed: 3':'2015 год (текущий год - оценка)','Unnamed: 4':'Планируемый период (прогноз)'})
df = df.loc[df['ПОКАЗАТЕЛЬ'] != '-']
df = df.loc[df['ПОКАЗАТЕЛЬ'] != 'Заполняется вручную']
del df['Unnamed: 1']
pd.set_option('max_colwidth', 1000)

# Сохраняем полученный результат в папке "html tables"
os.chdir("C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2014\\html tables")
df.to_html('Таблица_11(2014).html',index=False)