import os
import numpy as np
os.chdir('C:\\Users\\Кирилл\\Downloads\\PythonProject\\SaveDocuments')
import pandas as pd

# Получаем файл на вход и редактируем информацию(обьединяем столбцы, убираем ненужные строки, переводим в нужный формат данных)
pd.options.display.float_format = '{:.1f}'.format
xls_file = pd.read_excel('FILE76_01.01.2018_1191_1191.xls', 'Раздел5', index_col=None)
os.chdir('C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2018')
xls_file[9:].to_csv('Пятая часть5.csv', encoding='utf-8',sep=';',index=False)
df=pd.read_csv('Пятая часть5.csv',sep=';', comment='#',index_col=None)
df = df.fillna('')

for i in range(3,13):
    k='Unnamed: '+ str(i)
    df[k]=np.where(df[k] == 'X','', df[k])

# Изменяем формат данных в столбцах 'Unnamed(i)' на float для округления
for i in range(len(df['Unnamed: 3'])):
  try:
    for b in range(3,13):
        m='Unnamed: '+ str(b)
        if (df[m][i]!='') and  (df[m][i]!=m):
            df[m][i]=float(df[m][i])
            if b==5 or b==8 or b==11:
                df[m][i]=round(df[m][i],3)
            else:
                df[m][i]=round(df[m][i],1)
  except:
    continue

df = df.rename(columns={'Unnamed: 0': 'ПОКАЗАТЕЛЬ','Unnamed: 2':'Всего','Unnamed: 3':'В % к предыдущему периоду','Unnamed: 4':'Удельный вес (%)','Unnamed: 5':'Всего','Unnamed: 6':'В % к предыдущему периоду','Unnamed: 7':'Удельный вес (%)','Unnamed: 8':'Всего','Unnamed: 9':'В % к предыдущему периоду','Unnamed: 10':'Удельный вес (%)','Unnamed: 11':'Всего','Unnamed: 12':'В % к предыдущему периоду'})
del df['Unnamed: 1']
df = df.loc[df['ПОКАЗАТЕЛЬ'] != '1']
arrays = [['', 'Поступило в консолидированный бюджет Российской Федерации', 'Поступило в консолидированный бюджет Российской Федерации', 'Поступило в консолидированный бюджет Российской Федерации','В федеральный бюджет','В федеральный бюджет','В федеральный бюджет','В консолидированный бюджет субъекта РФ','В консолидированный бюджет субъекта РФ','В консолидированный бюджет субъекта РФ','В местный бюджет','В местный бюджет'], df.columns]
df.columns = pd.MultiIndex.from_arrays(arrays)
pd.set_option('max_colwidth', 1000)

# Сохраняем полученный результат в папке "html tablis"
os.chdir("C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2018\\html tablis")
df.to_html('Таблица_5(2018).html',index=False)
