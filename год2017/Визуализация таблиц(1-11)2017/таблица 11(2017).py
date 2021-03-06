import os
import numpy as np
os.chdir('C:\\Users\\Кирилл\\Downloads\\PythonProject\\SaveDocuments')
import pandas as pd

# Получаем файл на вход и редактируем информацию(обьединяем столбцы, убираем ненужные строки, переводим в нужный формат данных)
pd.options.display.float_format = '{:.1f}'.format
xls_file = pd.read_excel('FILE76_01.01.2017_824_824.xls', 'Раздел11', index_col=None)
os.chdir('C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2017')
xls_file[7:].to_csv('Одиннадцатая часть4.csv', encoding='utf-8',sep=';',index=False)
df=pd.read_csv('Одиннадцатая часть4.csv',sep=';', comment='#',index_col=None)
df = df.fillna('')

for s in range(3,11):
    p='Unnamed: '+ str(s)
    df[p]=np.where(df[p] == 'X','', df[p])

# Изменяем формат данных в столбцах 'Unnamed(i)' на float для округления
for i in range(len(df['Unnamed: 3'])):
  try:
    for b in range(2,11):
        m='Unnamed: '+ str(b)
        if (df[m][i]!='') and  (df[m][i]!=m):
            df[m][i]=float(df[m][i])
            df[m][i]=round(df[m][i],2)
  except:
    continue

df = df.rename(columns={'Раздел 11. Показатели налоговой нагрузки по отдельным видам экономической деятельности в 2014- 2016 годах*': 'ПОКАЗАТЕЛЬ','Unnamed: 2':'Поступило в консолидированный бюджет РФ, млрд.руб.','Unnamed: 3':'Оборот организаций*, млрд.руб.','Unnamed: 4':'Налоговая нагрузка, %','Unnamed: 5':'Поступило в консолидированный бюджет РФ, млрд.руб','Unnamed: 6':'Оборот организаций*, млрд.руб.','Unnamed: 7':'Налоговая нагрузка, %','Unnamed: 8':'Поступило в консолидированный бюджет РФ, млрд.руб','Unnamed: 9':'Оборот организаций*, млрд.руб.','Unnamed: 10':'Налоговая нагрузка, %'})
del df['Unnamed: 1']
arrays = [['', '2014 год', '2014 год', '2014 год','2015 год','2015 год','2015 год','2016 год','2016 год','2016 год'], df.columns]
df.columns = pd.MultiIndex.from_arrays(arrays)
pd.set_option('max_colwidth', 1000)

# Сохраняем полученный результат в папке "html_tables"
os.chdir("C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2017\\html table")
df.to_html('Таблица_11(2017).html',index=False)
