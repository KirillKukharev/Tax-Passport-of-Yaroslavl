import os
import numpy as np
os.chdir('C:\\Users\\Кирилл\\Downloads\\PythonProject\\SaveDocuments')
import pandas as pd

# Получаем файл на вход и редактируем информацию(обьединяем столбцы, убираем ненужные строки, переводим в нужный формат данных)
pd.options.display.float_format = '{:.1f}'.format
xls_file = pd.read_excel('FILE76_01.01.2016_178_178.xls', 'Раздел2', index_col=None)
os.chdir('C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2016')
xls_file[13:].to_csv('Вторая часть3.csv', encoding='utf-8',sep=';',index=False)
df=pd.read_csv('Вторая часть3.csv',sep=';', comment='#',index_col=None)
df = df.fillna('')
df = df.rename(columns={'Раздел 2.Основные показатели налоговой базы по администрируемым доходам': 'ПОКАЗАТЕЛЬ', 'Unnamed: 2': '2016 год','Unnamed: 3':'В % к предыдущему году'})


# Изменяем формат данных в столбцах '2016 год' и "В % к предыдущему году" на float для округления
for i in range(len(df['2016 год'])+3):
  try:
    if (df['2016 год'][i]!='') and  (df['2016 год'][i]!='2016 год'):
        df['2016 год'][i]=float(df['2016 год'][i])
        df['2016 год'][i]=round(df['2016 год'][i],3)
  except:
    continue

for i in range(len(df['В % к предыдущему году'])+3):
  try:
    if (df['В % к предыдущему году'][i]!='') and  (df['В % к предыдущему году'][i]!='В % к предыдущему году'):
        df['В % к предыдущему году'][i]=float(df['В % к предыдущему году'][i])
        df['В % к предыдущему году'][i]=round(df['В % к предыдущему году'][i],1)
  except:
    continue

df['2016 год'] = np.where(df['2016 год'] == 'X','', df['2016 год'])
df['В % к предыдущему году'] = np.where(df['В % к предыдущему году'] == 'X','', df['В % к предыдущему году'])
del df['Unnamed: 1']
pd.set_option('max_colwidth', 1000)

# Сохраняем полученный результат в папке "html tablici"
os.chdir("C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2016\\html tablici")
df.to_html('Таблица_2(2016).html',index=False)
