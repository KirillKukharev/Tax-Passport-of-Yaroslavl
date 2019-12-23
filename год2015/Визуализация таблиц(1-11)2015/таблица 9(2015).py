import os
import numpy as np
os.chdir('C:\\Users\\Кирилл\\Downloads\\PythonProject\\SaveDocuments')
import pandas as pd

# Получаем файл на вход и редактируем информацию(обьединяем столбцы, убираем ненужные строки, переводим в нужный формат данных)
pd.options.display.float_format = '{:.1f}'.format
xls_file = pd.read_excel('FILE76_01.01.2015_263_263.xls', 'Раздел9', index_col=None)
os.chdir('C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2015')
xls_file[14:].to_csv('Девятая часть2.csv', encoding='utf-8',sep=';',index=False)
df=pd.read_csv('Девятая часть2.csv',sep=';', comment='#',index_col=None)
df = df.fillna('')
del df['Unnamed: 1']
df['Unnamed: 3']=np.where(df['Unnamed: 3'] == 'X','', df['Unnamed: 3'])
df['Unnamed: 4']=np.where(df['Unnamed: 4'] == 'X','', df['Unnamed: 4'])

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
df = df.rename(columns={'Раздел 9.Показатели налоговой нагрузки': 'ПОКАЗАТЕЛЬ','Unnamed: 2':'в консолидированный бюджет Российской Федерации','Unnamed: 3':'в федеральный бюджет','Unnamed: 4':'в консолидированный бюджет субъекта РФ'})
arrays = [['', 'НАЛОГОВАЯ НАГРУЗКА  (В %  К ВВП) В 2015 ГОДУ', 'НАЛОГОВАЯ НАГРУЗКА  (В %  К ВВП) В 2015 ГОДУ', 'НАЛОГОВАЯ НАГРУЗКА  (В %  К ВВП) В 2015 ГОДУ'], df.columns]
df.columns = pd.MultiIndex.from_arrays(arrays)
pd.set_option('max_colwidth', 1000)

# Сохраняем полученный результат в папке "html_tables"
os.chdir("C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2015\\html_tables")
df.to_html('Таблица_9(2015).html',index=False)