import os
os.chdir('C:\\Users\\Кирилл\\Downloads\\PythonProject\\SaveDocuments')
import pandas as pd

# Получаем файл на вход и редактируем информацию(обьединяем столбцы, убираем ненужные строки, переводим в нужный формат данных)
pd.options.display.float_format = '{:.1f}'.format
xls_file = pd.read_excel('FILE76_01.01.2018_1191_1191.xls', 'Раздел3', index_col=None)
os.chdir('C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2018')
xls_file[4:].to_csv('Третья часть5.csv', encoding='utf-8',sep=';',index=False)
df=pd.read_csv('Третья часть5.csv',sep=';', comment='#',index_col=None)
df = df.fillna('')
df = df.rename(columns={'Раздел 3. Льготы по отдельным администрируемым доходам': 'ПОКАЗАТЕЛЬ', 'Unnamed: 2': '2018 год','Unnamed: 3':'В % к предыдущему году'})
del df['Unnamed: 1']
df = df.loc[df['ПОКАЗАТЕЛЬ'] != 'из стр. 310:']
pd.set_option('max_colwidth', 1000)

# Сохраняем полученный результат в папке "html tablis"
os.chdir("C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2018\\html tablis")
df.to_html('Таблица_3(2018).html',index=False)