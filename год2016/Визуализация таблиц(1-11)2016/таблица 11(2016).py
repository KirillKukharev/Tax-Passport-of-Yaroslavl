import os
import numpy as np
os.chdir('C:\\Users\\Кирилл\\Downloads\\PythonProject\\SaveDocuments')
import pandas as pd

# Получаем файл на вход и редактируем информацию(обьединяем столбцы, убираем ненужные строки, переводим в нужный формат данных)
pd.options.display.float_format = '{:.1f}'.format
xls_file = pd.read_excel('FILE76_01.01.2016_178_178.xls', 'Раздел11', index_col=None)
os.chdir('C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2016')
xls_file[4:].to_csv('Одиннадцатая часть3.csv', encoding='utf-8',sep=';',index=False)
df=pd.read_csv('Одиннадцатая часть3.csv',sep=';', comment='#',index_col=None)
df = df.fillna('')

# Изменяем формат данных в столбцах 'Unnamed(i)' на float для округления
for i in range(len(df['Unnamed: 3'])):
  try:
    for b in range(2,3):
        m='Unnamed: '+ str(b)
        if (df[m][i]!='') and  (df[m][i]!=m):
            df[m][i]=float(df[m][i])
            df[m][i]=round(df[m][i],2)
  except:
    continue

df = df.rename(columns={'Раздел 11.Оценка и прогнозирование поступлений отдельных налогов': 'ПОКАЗАТЕЛЬ','Unnamed: 2':'2016 год (базисный год - факт)','Unnamed: 3':'2017 год (текущий год - оценка)','Unnamed: 4':'Планируемый период (прогноз)'})
df = df.loc[df['ПОКАЗАТЕЛЬ'] != '-']
df = df.loc[df['ПОКАЗАТЕЛЬ'] != 'Заполняется вручную']
del df['Unnamed: 1']
df['2016 год (базисный год - факт)']=np.where(df['2016 год (базисный год - факт)'] == 'X','', df['2016 год (базисный год - факт)'])
pd.set_option('max_colwidth', 1000)

# Сохраняем полученный результат в папке "html tablici"
os.chdir("C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2016\\html tablici")
df.to_html('Таблица_11(2016).html',index=False)
