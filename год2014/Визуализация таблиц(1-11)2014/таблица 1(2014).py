import os
import numpy as np
os.chdir('C:\\Users\\Кирилл\\Downloads\\PythonProject\\SaveDocuments')
import pandas as pd

# Получаем файл на вход и редактируем информацию(обьединяем столбцы, убираем ненужные строки, переводим в нужный формат данных)
xls_file = pd.read_excel('FILE76_01.01.2014_452_452.xls', 'Раздел1', index_col=None)
os.chdir('C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2014')
xls_file[13:64].to_csv('Первая часть.csv', encoding='utf-8',sep=';',index=False)
df=pd.read_csv('Первая часть.csv',sep=';', comment='#',index_col=None)
df = df.rename(columns={'Раздел 1.Социально-экономическая характеристика региона': 'ПОКАЗАТЕЛЬ', 'Unnamed: 2': '2014 год','Unnamed: 3':'В % к предыдущему году'})

del df['Unnamed: 1']
df.dropna(subset=['2014 год'], inplace=True)
df = df.loc[df['2014 год'] != '-']
df = df.fillna('')
df['2014 год']=df['2014 год'].astype(float)
df['2014 год']=round(df['2014 год'],3)

df['В % к предыдущему году'] = np.where(df['В % к предыдущему году'] == 'X','', df['В % к предыдущему году'])

# Изменяем формат данных в столбце "В % к предыдущему году" на float для округления
for i in range(len(df['В % к предыдущему году'])+3):
  try:
    if (df['В % к предыдущему году'][i]!='') and  (df['В % к предыдущему году'][i]!='В % к предыдущему году'):
        df['В % к предыдущему году'][i]=float(df['В % к предыдущему году'][i])

    if (type(df['В % к предыдущему году'][i]))==float:
        df['В % к предыдущему году'][i]=round(df['В % к предыдущему году'][i],0)
  except:
    continue
pd.set_option('max_colwidth', 1000)

# Сохраняем полученный результат в папке "html tables"
os.chdir("C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2014\\html tables")
df.to_html('Таблица_1(2014).html',index=False)