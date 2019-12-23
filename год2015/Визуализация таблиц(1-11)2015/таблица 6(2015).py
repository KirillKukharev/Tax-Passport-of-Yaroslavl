import os
import numpy as np
os.chdir('C:\\Users\\Кирилл\\Downloads\\PythonProject\\SaveDocuments')
import pandas as pd

# Получаем файл на вход и редактируем информацию(обьединяем столбцы, убираем ненужные строки, переводим в нужный формат данных)
xls_file = pd.read_excel('FILE76_01.01.2016_178_178.xls', 'Раздел6', index_col=None)
os.chdir('C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2015')
xls_file[16:].to_csv('Шестая часть2.csv', encoding='utf-8',sep=';',index=False)
df=pd.read_csv('Шестая часть2.csv',sep=';', comment='#',index_col=None)
df = df.fillna('')

# Изменяем формат данных в столбцах "Unnamed(i)" на float для округления
pd.options.display.float_format = '{:.1f}'.format
for i in range(len(df['Unnamed: 3'])):
  try:
    for b in range(3,15):
        m='Unnamed: '+ str(b)
        if (df[m][i]!='') and  (df[m][i]!=m):
            df[m][i]=float(df[m][i])
            if b==3:
                df[m][i]=round(df[m][i],1)
            else:
                df[m][i]=round(df[m][i],3)
  except:
    continue

df = df.rename(columns={'Раздел 6.Поступления администрируемых доходов в консолидированный бюджет Российской Федерации в структуре основных видов экономической деятельности': 'ВИДЫ ЭКОНОМИЧЕСКОЙ ДЕЯТЕЛЬНОСТИ','Unnamed: 2':'Поступило в консолидированный бюджет, всего','Unnamed: 3':'Уд. вес в общей сумме поступлений (%)','Unnamed: 4':'Федеральные налоги','Unnamed: 5':'Всего','Unnamed: 6':'в том числе в федеральный бюджет','Unnamed: 7':'налог на доходы физических лиц','Unnamed: 8':'НДС','Unnamed: 9':'акцизы по подакцизным товарам','Unnamed: 10':'налог на добычу полезных ископаемых','Unnamed: 11':'остальные налоги и сборы','Unnamed: 12':'Региональные налоги и сборы','Unnamed: 13':'Местные налоги и сборы','Unnamed: 14':'Налоги со специальным налоговым режимом'})
del df['Unnamed: 1']
df['Уд. вес в общей сумме поступлений (%)'] = np.where(df['Уд. вес в общей сумме поступлений (%)'] == 'X','', df['Уд. вес в общей сумме поступлений (%)'])

arrays = [['', '', '', '','налог на прибыль организации','налог на прибыль организации','','','','','','в том числе:','в том числе:','в том числе:'], df.columns]
df.columns = pd.MultiIndex.from_arrays(arrays)
pd.set_option('max_colwidth', 1000)

# Сохраняем полученный результат в папке "html_tables"
os.chdir("C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2015\\html_tables")
df.to_html('Таблица_6(2015).html',index=False)