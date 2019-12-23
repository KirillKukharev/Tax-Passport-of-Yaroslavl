import os
os.chdir('C:\\Users\\Кирилл\\Downloads\\PythonProject\\SaveDocuments')
import pandas as pd

# Получаем файл на вход и редактируем информацию(обьединяем столбцы, убираем ненужные строки, переводим в нужный формат данных)
xls_file = pd.read_excel('FILE76_01.01.2015_263_263.xls', 'Раздел3', index_col=None)
os.chdir('C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2015')
xls_file[13:].to_csv('Третья часть2.csv', encoding='utf-8',sep=';',index=False)
df=pd.read_csv('Третья часть2.csv',sep=';', comment='#',index_col=None)
df = df.fillna('')
df = df.rename(columns={'Раздел 3.Льготы по отдельным администрируемым доходам': 'ПОКАЗАТЕЛЬ', 'Unnamed: 2': '2015 год','Unnamed: 3':'В % к предыдущему году'})
del df['Unnamed: 1']

# Изменяем формат данных в столбце "В % к предыдущему году" на float для округления
pd.options.display.float_format = '{:.1f}'.format
for i in range(len(df['В % к предыдущему году'])+3):
  try:
    if (df['В % к предыдущему году'][i]!='') and  (df['В % к предыдущему году'][i]!='В % к предыдущему году'):
        df['В % к предыдущему году'][i]=float(df['В % к предыдущему году'][i])
        df['В % к предыдущему году'][i]=round(df['В % к предыдущему году'][i],1)
  except:
    continue
df = df.loc[df['ПОКАЗАТЕЛЬ'] != 'из строки 310:']
pd.set_option('max_colwidth', 1000)

# Сохраняем полученный результат в папке "html_tables"
os.chdir("C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2015\\html_tables")
df.to_html('Таблица_3(2015).html',index=False)