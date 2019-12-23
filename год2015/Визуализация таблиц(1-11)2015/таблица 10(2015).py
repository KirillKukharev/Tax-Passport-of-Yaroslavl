import os
import numpy as np
os.chdir('C:\\Users\\Кирилл\\Downloads\\PythonProject\\SaveDocuments')
import pandas as pd

# Получаем файл на вход и редактируем информацию(обьединяем столбцы, убираем ненужные строки, переводим в нужный формат данных)
pd.options.display.float_format = '{:.1f}'.format
xls_file = pd.read_excel('FILE76_01.01.2015_263_263.xls', 'Раздел10', index_col=None)
os.chdir('C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2015')
xls_file[14:].to_csv('Десятая часть2.csv', encoding='utf-8',sep=';',index=False)
df=pd.read_csv('Десятая часть2.csv',sep=';', comment='#',index_col=None)
df = df.fillna('')
del df['Unnamed: 1']

for s in range(3,11):
    p='Unnamed: '+ str(s)
    df[p]=np.where(df[p] == 'X','', df[p])

# Изменяем формат данных в столбцах "Unnamed(i)" на float для округления
for i in range(len(df['Unnamed: 3'])):
  try:
    for b in range(2,11):
        m='Unnamed: '+ str(b)
        if (df[m][i]!='') and  (df[m][i]!=m):
            df[m][i]=float(df[m][i])
        if b==2 or b==3 or b==5 or b==6 or b==8 or b==9:
            df[m][i]=round(df[m][i],3)
        else:
            df[m][i]=round(df[m][i],1)
  except:
    continue

df = df.rename(columns={'Раздел 10.Показатели налоговой нагрузки по отдельным видам экономической деятельности в 2012-2014 годах': 'ПОКАЗАТЕЛЬ','Unnamed: 2':'Поступило в консолидированный бюджет РФ','Unnamed: 3':'Оборот организаций*','Unnamed: 4':'Налоговая нагрузка, %','Unnamed: 5':'Поступило в консолидированный бюджет РФ','Unnamed: 6':'Оборот организаций*','Unnamed: 7':'Налоговая нагрузка, %','Unnamed: 8':'Поступило в консолидированный бюджет РФ','Unnamed: 9':'Оборот организаций*','Unnamed: 10':'Налоговая нагрузка, %'})
arrays = [['', '2012 г.', '2012 г.', '2012 г.', '2013 г.', '2013 г.', '2013 г.','2014 г.','2014 г.','2014 г.'], df.columns]
df.columns = pd.MultiIndex.from_arrays(arrays)
pd.set_option('max_colwidth', 1000)

# Сохраняем полученный результат в папке "html_tables"
os.chdir("C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2015\\html_tables")
df.to_html('Таблица_10(2015).html',index=False)