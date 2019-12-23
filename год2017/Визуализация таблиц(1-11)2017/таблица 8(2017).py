import os
import numpy as np
os.chdir('C:\\Users\\Кирилл\\Downloads\\PythonProject\\SaveDocuments')
import pandas as pd

# Получаем файл на вход и редактируем информацию(обьединяем столбцы, убираем ненужные строки, переводим в нужный формат данных)
pd.options.display.float_format = '{:.1f}'.format
xls_file = pd.read_excel('FILE76_01.01.2017_824_824.xls', 'Раздел8', index_col=None)
os.chdir('C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2017')
xls_file[12:40].to_csv('Восьмая часть4.csv', encoding='utf-8',sep=';',index=False)
df=pd.read_csv('Восьмая часть4.csv',sep=';', comment='#',index_col=None)
df = df.fillna('')

# Изменяем формат данных в столбцах 'Unnamed(i)' на float для округления
for i in range(len(df['Unnamed: 3'])):
  try:
    for b in range(3,12):
        m='Unnamed: '+ str(b)
        if (df[m][i]!='') and  (df[m][i]!=m):
            df[m][i]=float(df[m][i])
        if b==3 or b==5 or b==7 or b==9:
            df[m][i]=round(df[m][i],1)
        else:
            df[m][i]=round(df[m][i],3)
  except:
    continue
for i in range(3,12):
    k='Unnamed: '+ str(i)
    df[k]=np.where(df[k] == 'X','', df[k])

df = df.rename(columns={'Раздел 8. Задолженность по налогам и сборам, пеням и налоговым санкциям в бюджетную систему Российской Федерации': 'ПОКАЗАТЕЛЬ','Unnamed: 2':'Всего','Unnamed: 3':'Недоимка / Задолженность по пеням и налоговым санкциям','Unnamed: 4':'Отсроченные (рассроченные) платежи и реструктурированная задолженность','Unnamed: 5':'Приостановленные к взысканию платежи','Unnamed: 6':'Невозможно к взысканию налоговыми органами','Unnamed: 7':'Всего','Unnamed: 8':'Недоимка / Задолженность по пеням и налоговым санкциям','Unnamed: 9':'Отсроченные (рассроченные) платежи и реструктурированная задолженность','Unnamed: 10':'Приостановленные к взысканию платежи','Unnamed: 11':'Невозможно к взысканию налоговыми органами'})
df = df.loc[df['ПОКАЗАТЕЛЬ'] != '1']
del df['Unnamed: 1']
arrays = [['', 'По состоянию на 01.01.2018', 'По состоянию на 01.01.2018', 'По состоянию на 01.01.2018','По состоянию на 01.01.2018','По состоянию на 01.01.2018','Изменение за 2017 год','Изменение за 2017 год','Изменение за 2017 год','Изменение за 2017 год','Изменение за 2017 год'], df.columns]
df.columns = pd.MultiIndex.from_arrays(arrays)
pd.set_option('max_colwidth', 1000)

# Сохраняем полученный результат в папке "html_tables"
os.chdir("C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2017\\html table")
df.to_html('Таблица_8(2017).html',index=False)