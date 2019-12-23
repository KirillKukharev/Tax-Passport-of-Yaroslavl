import os
import numpy as np
os.chdir('C:\\Users\\Кирилл\\Downloads\\PythonProject\\SaveDocuments')
import pandas as pd

# Получаем файл на вход и редактируем информацию(обьединяем столбцы, убираем ненужные строки, переводим в нужный формат данных)
pd.options.display.float_format = '{:.1f}'.format
xls_file = pd.read_excel('FILE76_01.01.2017_824_824.xls', 'Раздел2', index_col=None)
os.chdir('C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2017')
xls_file[7:].to_csv('Вторая часть4.csv', encoding='utf-8',sep=';',index=False)
df=pd.read_csv('Вторая часть4.csv',sep=';', comment='#',index_col=None)
df = df.fillna('')
df = df.rename(columns={'Раздел 2. Основные показатели налоговой базы по администрируемым доходам': 'ПОКАЗАТЕЛЬ', 'Unnamed: 2': '2017 год','Unnamed: 3':'В % к предыдущему году'})

# Изменяем формат данных в столбцах '2017 год' и "В % к предыдущему году" на float для округления
for i in range(len(df['2017 год'])+3):
  try:
    if (df['2017 год'][i]!='') and  (df['2017 год'][i]!='2017 год'):
        df['2017 год'][i]=float(df['2017 год'][i])
        df['2017 год'][i]=round(df['2017 год'][i],3)
  except:
    continue

for i in range(len(df['В % к предыдущему году'])+3):
  try:
    if (df['В % к предыдущему году'][i]!='') and  (df['В % к предыдущему году'][i]!='В % к предыдущему году'):
        df['В % к предыдущему году'][i]=float(df['В % к предыдущему году'][i])
        df['В % к предыдущему году'][i]=round(df['В % к предыдущему году'][i],1)
  except:
    continue

df['2017 год'] = np.where(df['2017 год'] == 'X','', df['2017 год'])
df['В % к предыдущему году'] = np.where(df['В % к предыдущему году'] == 'X','', df['В % к предыдущему году'])
del df['Unnamed: 1']
pd.set_option('max_colwidth', 1000)

# Сохраняем полученный результат в папке "html table"
os.chdir("C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2017\\html table")
df.to_html('Таблица_2(2017).html',index=False)
