import os
os.chdir('C:\\Users\\Кирилл\\Downloads\\PythonProject\\SaveDocuments')
import pandas as pd

# Получаем файл на вход и редактируем информацию(обьединяем столбцы, убираем ненужные строки, переводим в нужный формат данных)
xls_file = pd.read_excel('FILE76_01.01.2015_263_263.xls', 'Раздел4', index_col=None)
os.chdir('C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2015')
xls_file[13:].to_csv('Четвертая часть2.csv', encoding='utf-8',sep=';',index=False)
df=pd.read_csv('Четвертая часть2.csv',sep=';', comment='#',index_col=None)
df = df.fillna('')
pd.options.display.float_format = '{:.1f}'.format
df = df.rename(columns={'Раздел 4.Основные показатели контрольной работы налоговых органов': 'ПОКАЗАТЕЛЬ', 'Unnamed: 2': '2015 год','Unnamed: 3':'В % к предыдущему году'})
del df['Unnamed: 1']
pd.set_option('max_colwidth', 1000)

# Сохраняем полученный результат в папке "html_tables"
os.chdir("C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2015\\html_tables")
df.to_html('Таблица_4(2015).html',index=False)