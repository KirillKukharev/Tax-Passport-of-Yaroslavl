import os
import numpy as np
os.chdir('C:\\Users\\Кирилл\\Downloads\\PythonProject\\SaveDocuments')
import pandas as pd

# Получаем файл на вход и редактируем информацию(обьединяем столбцы, убираем ненужные строки, переводим в нужный формат данных)
pd.options.display.float_format = '{:.1f}'.format
xls_file = pd.read_excel('FILE76_01.01.2016_178_178.xls', 'Раздел6', index_col=None)
os.chdir('C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2016')
xls_file[16:].to_csv('Шестая часть3.csv', encoding='utf-8',sep=';',index=False)
df=pd.read_csv('Шестая часть3.csv',sep=';', comment='#',index_col=None)
df = df.fillna('')

# Изменяем формат данных в столбцах 'Unnamed(i)' на float для округления
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
df['Unnamed: 3'] = np.where(df['Unnamed: 3'] == 'X','', df['Unnamed: 3'])
df = df.rename(columns={'Раздел 6.Поступления администрируемых доходов в консолидированный бюджет Российской Федерации в структуре основных видов экономической деятельности': 'ПОКАЗАТЕЛЬ','Unnamed: 2':'Поступило в консолидированный бюджет, всего','Unnamed: 3':'Уд. вес в общей сумме поступлений (%)','Unnamed: 4':'Федеральные налоги','Unnamed: 5':'Всего','Unnamed: 6':'в том числе в федеральный бюджет','Unnamed: 7':'налог на доходы физических лиц','Unnamed: 8':'НДС','Unnamed: 9':'акцизы по подакцизным товарам','Unnamed: 10':'налог на добычу полезных ископаемых','Unnamed: 11':'остальные налоги и сборы','Unnamed: 12':'Региональные налоги и сборы','Unnamed: 13':'Местные налоги и сборы','Unnamed: 14':'Налоги, предусмотренные специальными налоговыми режимами'})
df = df.loc[df['ПОКАЗАТЕЛЬ'] != '1']
del df['Unnamed: 1']
arrays = [['', '', '', '','налог на прибыль организации','налог на прибыль организации','','','','','','в том числе:','в том числе:','в том числе:'], df.columns]
df.columns = pd.MultiIndex.from_arrays(arrays)
pd.set_option('max_colwidth', 1000)

# Сохраняем полученный результат в папке "html tablici"
os.chdir("C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2016\\html tablici")
df.to_html('Таблица_6(2016).html',index=False)