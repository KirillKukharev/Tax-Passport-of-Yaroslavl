import os
os.chdir('C:\\Users\\Кирилл\\Downloads\\PythonProject\\SaveDocuments')
import pandas as pd

# Получаем файл на вход и редактируем информацию(обьединяем столбцы, убираем ненужные строки, переводим в нужный формат данных)
xls_file = pd.read_excel('FILE76_01.01.2017_824_824.xls', 'Руководители', index_col=None)
os.chdir('C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2017')
xls_file[6:].to_csv('Первая часть4.csv', encoding='utf-8',sep=';',index=False)
df=pd.read_csv('Первая часть4.csv',sep=';', comment='#',index_col=None)
df = df.fillna('')
df = df.rename(columns={'РУКОВОДИТЕЛИ ФЕДЕРАЛЬНОГО ОКРУГА, АДМИНИСТРАЦИИ СУБЪЕКТА РОССИЙСКОЙ ФЕДЕРАЦИИ ': 'ПОКАЗАТЕЛЬ', 'Unnamed: 2': 'Фамилия, имя, отчество','Unnamed: 3':'почтовый','Unnamed: 4':'электронной почты','Unnamed: 5':'телефона','Unnamed: 6':'факса'})
del df['Unnamed: 1']
df = df.loc[df['ПОКАЗАТЕЛЬ'] != '1']
arrays = [['', '', 'Адрес', 'Адрес','Код и номер','Код и номер'], df.columns]
df.columns = pd.MultiIndex.from_arrays(arrays)
pd.set_option('max_colwidth', 1000)

# Сохраняем полученный результат в папке "html table"
os.chdir("C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2017\\html table")
df.to_html('Руководители(2017).html',index=False)
