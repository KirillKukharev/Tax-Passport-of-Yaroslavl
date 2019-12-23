import os
import numpy as np
os.chdir('C:\\Users\\Кирилл\\Downloads\\PythonProject\\SaveDocuments')
import pandas as pd

# Получаем файл на вход и редактируем информацию(обьединяем столбцы, убираем ненужные строки, переводим в нужный формат данных)
pd.options.display.float_format = '{:.1f}'.format
xls_file = pd.read_excel('FILE76_01.01.2018_1191_1191.xls', 'Раздел1', index_col=None)
os.chdir('C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2018')
xls_file[10:].to_csv('Первая часть5.csv', encoding='utf-8',sep=';',index=False)
df=pd.read_csv('Первая часть5.csv',sep=';', comment='#',index_col=None)
df = df.fillna('')
df = df.rename(columns={'Unnamed: 0': 'ПОКАЗАТЕЛЬ', 'Unnamed: 2': '2018 год','Unnamed: 3':'В % к предыдущему году'})

# Изменяем формат данных в столбце 'В % к предыдущему году' на float для округления
for i in range(len(df['В % к предыдущему году'])+3):
  try:
    if (df['В % к предыдущему году'][i]!='') and  (df['В % к предыдущему году'][i]!='В % к предыдущему году'):
        df['В % к предыдущему году'][i]=float(df['В % к предыдущему году'][i])
    if (type(df['В % к предыдущему году'][i]))==float:
        df['В % к предыдущему году'][i]=round(df['В % к предыдущему году'][i],1)
  except:
    continue

df['В % к предыдущему году'] = np.where(df['В % к предыдущему году'] == 'X','', df['В % к предыдущему году'])
del df['Unnamed: 1']
pd.set_option('max_colwidth', 1000)

# Сохраняем полученный результат в папке "html tablis"
os.chdir("C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2018\\html tablis")
df.to_html('Таблица_1(2018).html',index=False)
