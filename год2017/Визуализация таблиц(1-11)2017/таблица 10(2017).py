import os
import numpy as np
os.chdir('C:\\Users\\Кирилл\\Downloads\\PythonProject\\SaveDocuments')
import pandas as pd

# Получаем файл на вход и редактируем информацию(обьединяем столбцы, убираем ненужные строки, переводим в нужный формат данных)
pd.options.display.float_format = '{:.1f}'.format
xls_file = pd.read_excel('FILE76_01.01.2017_824_824.xls', 'Раздел10', index_col=None)
os.chdir('C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2017')
xls_file[8:].to_csv('Десятая часть4.csv', encoding='utf-8',sep=';',index=False)
df=pd.read_csv('Десятая часть4.csv',sep=';', comment='#',index_col=None)
df = df.fillna('')

for s in range(3,5):
    p='Unnamed: '+ str(s)
    df[p]=np.where(df[p] == 'X','', df[p])

# Изменяем формат данных в столбцах 'Unnamed(i)' на float для округления
for i in range(len(df['Unnamed: 3'])):
  try:
    for b in range(2,5):
        m='Unnamed: '+ str(b)
        if (df[m][i]!='') and  (df[m][i]!=m):
            df[m][i]=float(df[m][i])
            df[m][i]=round(df[m][i],2)
  except:
    continue

df = df.rename(columns={'Раздел 10. Показатели налоговой нагрузки': 'ПОКАЗАТЕЛЬ','Unnamed: 2':'в консолидированный бюджет Российской Федерации','Unnamed: 3':'в федеральный бюджет','Unnamed: 4':'в консолидированный бюджет субъекта РФ'})
del df['Unnamed: 1']
arrays = [['', 'НАЛОГОВАЯ НАГРУЗКА  (В %  К ВВП) В 2017 ГОДУ', 'НАЛОГОВАЯ НАГРУЗКА  (В %  К ВВП) В 2017 ГОДУ', 'НАЛОГОВАЯ НАГРУЗКА  (В %  К ВВП) В 2017 ГОДУ'], df.columns]
df.columns = pd.MultiIndex.from_arrays(arrays)
pd.set_option('max_colwidth', 1000)

# Сохраняем полученный результат в папке "html_tables"
os.chdir("C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2017\\html table")
df.to_html('Таблица_10(2017).html',index=False)