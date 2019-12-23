import os
import numpy as np
os.chdir('C:\\Users\\Кирилл\\Downloads\\PythonProject\\SaveDocuments')
import pandas as pd

# Получаем файл на вход и редактируем информацию(обьединяем столбцы, убираем ненужные строки, переводим в нужный формат данных)
xls_file = pd.read_excel('FILE76_01.01.2014_452_452.xls', 'Раздел10', index_col=None)
os.chdir('C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2014')
xls_file[14:].to_csv('Десятая часть.csv', encoding='utf-8',sep=';',index=False)
df=pd.read_csv('Десятая часть.csv',sep=';', comment='#',index_col=None)
df = df.fillna('')
del df['Unnamed: 1']

# Изменяем формат данных в столбцах "Unnamed(i)" на float для округления
for s in range(3,6):
    p='Unnamed: '+ str(s)
    df[p]=np.where(df[p] == 'X','', df[p])
for i in range(len(df['Unnamed: 3'])):
  try:
    for b in range(2,6):
        m='Unnamed: '+ str(b)
        if (df[m][i]!='') and  (df[m][i]!=m):
            df[m][i]=float(df[m][i])
            df[m][i]=round(df[m][i],2)
  except:
    continue
df = df.rename(columns={'Раздел 10.Показатели налоговой нагрузки по отдельным видам экономической деятельности': 'ПОКАЗАТЕЛЬ','Unnamed: 2':'Обрабатывающие производства','Unnamed: 3':'Добыча полезных ископаемых','Unnamed: 4':'Производство и распределение электроэнергии, газа и воды','Unnamed: 5':'Строительство'})
arrays = [['', 'НАЛОГОВАЯ НАГРУЗКА  (копеек с 1 рубля объема отгруженных товаров собственного производства, выполненных работ и услуг собственными силами)', 'НАЛОГОВАЯ НАГРУЗКА  (копеек с 1 рубля объема отгруженных товаров собственного производства, выполненных работ и услуг собственными силами)', 'НАЛОГОВАЯ НАГРУЗКА  (копеек с 1 рубля объема отгруженных товаров собственного производства, выполненных работ и услуг собственными силами)', 'НАЛОГОВАЯ НАГРУЗКА (копеек с 1 рубля объема выполненных работ)'], df.columns]
df.columns = pd.MultiIndex.from_arrays(arrays)
pd.set_option('max_colwidth', 1000)

# Сохраняем полученный результат в папке "html tables"
os.chdir("C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2014\\html tables")
df.to_html('Таблица_10(2014).html',index=False)