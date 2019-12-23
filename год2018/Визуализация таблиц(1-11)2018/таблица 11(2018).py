import os
import numpy as np
os.chdir('C:\\Users\\Кирилл\\Downloads\\PythonProject\\SaveDocuments')
import pandas as pd

# Получаем файл на вход и редактируем информацию(обьединяем столбцы, убираем ненужные строки, переводим в нужный формат данных)
pd.options.display.float_format = '{:.1f}'.format
xls_file = pd.read_excel('FILE76_01.01.2018_1191_1191.xls', 'Раздел11', index_col=None)
os.chdir('C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2018')
xls_file[5:].to_csv('Одиннадцатая часть4.csv', encoding='utf-8',sep=';',index=False)
df=pd.read_csv('Одиннадцатая часть4.csv',sep=';', comment='#',index_col=None)
df = df.fillna('')

for s in range(3,8):
    p='Unnamed: '+ str(s)
    df[p]=np.where(df[p] == 'X','', df[p])

df = df.rename(columns={'Раздел 11. Показатели налоговой нагрузки по отдельным видам экономической деятельности в 2017-2018 годах': 'ПОКАЗАТЕЛЬ','Unnamed: 2':'Поступило в консолидированный бюджет РФ, млрд.руб','Unnamed: 3':'Оборот организаций, млрд.руб.','Unnamed: 4':'Налоговая нагрузка, %','Unnamed: 5':'Поступило в консолидированный бюджет РФ, млрд.руб','Unnamed: 6':'Оборот организаций, млрд.руб.','Unnamed: 7':'Налоговая нагрузка, %'})
del df['Unnamed: 1']

arrays = [['','2017 год','2017 год','2017 год','2018 год','2018 год','2018 год'], df.columns]
df.columns = pd.MultiIndex.from_arrays(arrays)
pd.set_option('max_colwidth', 1000)

# Сохраняем полученный результат в папке "html tablis"
os.chdir("C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2018\\html tablis")
df.to_html('Таблица_11(2018).html',index=False)
