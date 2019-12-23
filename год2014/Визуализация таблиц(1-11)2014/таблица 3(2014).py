import os
os.chdir('C:\\Users\\Кирилл\\Downloads\\PythonProject\\SaveDocuments')
import pandas as pd

# Получаем файл на вход и редактируем информацию(обьединяем столбцы, убираем ненужные строки, переводим в нужный формат данных)
xls_file = pd.read_excel('FILE76_01.01.2014_452_452.xls', 'Раздел3', index_col=None)
os.chdir('C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2014')
xls_file[13:].to_csv('Третья часть.csv', encoding='utf-8',sep=';',index=False)
df=pd.read_csv('Третья часть.csv',sep=';', comment='#',index_col=None)
df = df.fillna('')
df = df.rename(columns={'Раздел 3.Льготы по отдельным администрируемым доходам': 'ПОКАЗАТЕЛЬ', 'Unnamed: 2': '2014 год','Unnamed: 3':'В % к предыдущему году'})
del df['Unnamed: 1']

# Изменяем формат данных в столбце  "В % к предыдущему году" на float для округления
for i in range(len(df['В % к предыдущему году'])+3):
  try:
    if (df['В % к предыдущему году'][i]!='') and  (df['В % к предыдущему году'][i]!='В % к предыдущему году'):
        df['В % к предыдущему году'][i]=float(df['В % к предыдущему году'][i])

    if (type(df['В % к предыдущему году'][i]))==float:
        df['В % к предыдущему году'][i]=round(df['В % к предыдущему году'][i],0)
  except:
    continue
pd.set_option('max_colwidth', 1000)

# Сохраняем полученный результат в папке "html tables"
os.chdir("C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2014\\html tables")
df.to_html('Таблица_3(2014).html',index=False)