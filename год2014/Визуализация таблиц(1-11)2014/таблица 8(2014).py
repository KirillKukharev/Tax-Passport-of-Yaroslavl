import os
import numpy as np
os.chdir('C:\\Users\\Кирилл\\Downloads\\PythonProject\\SaveDocuments')
import pandas as pd

# Получаем файл на вход и редактируем информацию(обьединяем столбцы, убираем ненужные строки, переводим в нужный формат данных)
xls_file = pd.read_excel('FILE76_01.01.2014_452_452.xls', 'Раздел8', index_col=None)
os.chdir('C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2014')
xls_file[15:].to_csv('Восьмая часть.csv', encoding='utf-8',sep=';',index=False)
df=pd.read_csv('Восьмая часть.csv',sep=';', comment='#',index_col=None)
df = df.fillna('')

df['-.1']=np.where(df['-.1'] == '-','', df['-.1'])

# Изменяем формат данных в столбцах "Unnamed(i)" на float для округления
for i in range(len(df['Unnamed: 3'])):
  try:
    for b in range(3,10):
        m='Unnamed: '+ str(b)
        if (df[m][i]!='') and  (df[m][i]!=m):
            df[m][i]=float(df[m][i])
        if b==3 or b==5 or b==7 or b==9:
            df[m][i]=round(df[m][i],1)
        else:
            df[m][i]=round(df[m][i],3)
  except:
    continue

for i in range(len(df['-.1'])):
    if (df['-.1'][i]!='') and  (df['-.1'][i]!='-.1'):
        df['-.1'][i]=float(df['-.1'][i])
        df['-.1'][i]=round(df['-.1'][i],3)

del df['-']
df = df.rename(columns={'Раздел 8.Задолженность по налогам и сборам по основным видам экономической деятельности': 'ПОКАЗАТЕЛЬ','-.1':'млн. рублей','Unnamed: 3':'Удельный вес в общей сумме задолженности (%)','Unnamed: 4':'млн. рублей','Unnamed: 5':'Удельный вес в сумме задолженности (%)','Unnamed: 6':'млн. рублей','Unnamed: 7':'Удельный вес в сумме задолженности (%)','Unnamed: 8':'млн. рублей','Unnamed: 9':'Удельный вес в сумме задолженности (%)'})
arrays = [['', 'Задолженность', 'Задолженность', 'Недоимка','Недоимка','Отсроченные (рассроченные) платежи и реструктурированная задолженность','Отсроченные (рассроченные) платежи и реструктурированная задолженность','Приостановленные к взысканию платежи','Приостановленные к взысканию платежи'], df.columns]
df.columns = pd.MultiIndex.from_arrays(arrays)
pd.set_option('max_colwidth', 1000)

# Сохраняем полученный результат в папке "html tables"
os.chdir("C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2014\\html tables")
df.to_html('Таблица_8(2014).html',index=False)