import os
import numpy as np
os.chdir('C:\\Users\\Кирилл\\Downloads\\PythonProject\\SaveDocuments')
import pandas as pd
pd.options.display.float_format = '{:.1f}'.format
xls_file = pd.read_excel('FILE76_01.01.2018_1191_1191.xls', 'Раздел12', index_col=None)
os.chdir('C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2018')
xls_file[6:].to_csv('Двенадцатая часть4.csv', encoding='utf-8',sep=';',index=False)
df=pd.read_csv('Двенадцатая часть4.csv',sep=';', comment='#',index_col=None)
df = df.fillna('')

for s in range(2,3):
    p='Unnamed: '+ str(s)
    df[p]=np.where(df[p] == 'X','', df[p])

for i in range(len(df['Unnamed: 3'])):
  try:
    for b in range(2,5):
        m='Unnamed: '+ str(b)
        if (df[m][i]!='') and  (df[m][i]!=m):
            df[m][i]=float(df[m][i])
            df[m][i]=round(df[m][i],2)
  except:
    continue

df = df.rename(columns={'Раздел 12. Оценка и прогнозирование поступлений отдельных налогов': 'ПОКАЗАТЕЛЬ','Unnamed: 2':'2017 год (базисный год - факт)','Unnamed: 3':'2018 год (текущий год - оценка)','Unnamed: 4':'Планируемый период (прогноз)'})
df = df.loc[df['ПОКАЗАТЕЛЬ'] != 'Заполняется вручную']
df = df.loc[df['ПОКАЗАТЕЛЬ'] != '']
del df['Unnamed: 1']
pd.set_option('max_colwidth', 1000)
os.chdir("C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2018\\html tablis")
df.to_html('Таблица_12(2018).html',index=False)
