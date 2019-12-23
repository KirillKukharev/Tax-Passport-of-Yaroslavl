import pandas as pd
import os
import chart_studio.plotly as py
import plotly.graph_objs as go
from plotly.offline import plot
import time
# Считывание файла result1part(2016).csv и преобразование данных в столбце "2016 год"
pd.options.display.float_format = '{:.1f}'.format
os.chdir("C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2016\\очищенные результаты для 1 таблицы")
import pandas as pd
df1=pd.read_csv('result1part(2016).csv',sep=';', comment='#',index_col=None,encoding='cp1251')
k1=df1['ПОКАЗАТЕЛЬ']
del df1['В % к предыдущему году']
for i in range(len(df1['2016 год'])):
  try:
    if (df1['2016 год'][i]!='') and  (df1['2016 год'][i]!='2016 год'):
        df1['2016 год'][i]=float(df1['2016 год'][i])
  except:
    continue
b1=df1['2016 год']


# Считывание файла result1part(2015).csv и преобразование данных в столбце "2015 год"
os.chdir("C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2015\\очищенные результаты для 1 таблицы")
df2=pd.read_csv('result1part(2015).csv',sep=';', comment='#',index_col=None,encoding='cp1251')
del df2['В % к предыдущему году']
for i in range(len(df2['2015 год'])):
  try:
    if (df2['2015 год'][i]!='') and  (df2['2015 год'][i]!='2015 год'):
        df2['2015 год'][i]=float(df2['2015 год'][i])
  except:
    continue
k2=df2['ПОКАЗАТЕЛЬ']
b2=df2['2015 год']
new_df=df1.assign(год_2015=b2)
pd.set_option('max_colwidth', 500)


# Считывание файла result1part(2014).csv и преобразование данных в столбце "2014 год"
os.chdir("C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2014\\очищенные результаты для 1 таблицы")
df3=pd.read_csv('result1part(2014).csv',sep=';', comment='#',index_col=None,encoding='cp1251')
del df3['В % к предыдущему году']
b3=df3['2014 год']
new_df['год_2014']=[b3[0],b3[1],b3[2],b3[3],b3[7],b3[5],b3[9],b3[6],b3[4],b3[8],b3[11],b3[10],b3[13],b3[14],b3[15],b3[16],b3[17],b3[18],b3[19],b3[20],b3[21],b3[22],b3[23],b3[24],'-',b3[25],'-',b3[26],b3[27],b3[28],b3[29],b3[30],b3[31],b3[32],b3[34],b3[35],b3[33],b3[36],b3[37],b3[38],'-',b3[39],'-',b3[40],b3[41],'-','-','-',b3[42],b3[43],b3[44],b3[45]]
new_df = new_df.rename(columns={'год_2014': '2014 год','год_2015':'2015 год'})
cols = list(new_df.columns)
a, b = cols.index('2014 год'), cols.index('2016 год')
cols[b], cols[a] = cols[a], cols[b]
new_df = new_df[cols]
for i in range(len(new_df['2014 год'])):
  try:
    for b in range(4,7):
        m='201'+ str(b)+' год'
        if (new_df[m][i]!='') and  (new_df[m][i]!=m):
            new_df[m][i]=float(new_df[m][i])
            new_df[m][i]=round(new_df[m][i],3)
  except:
    continue


# Добавление и корректировка недостающих результатов в Dataframe
new_df.at[26, '2014 год']=28.1
new_df.at[24, '2014 год']=10.5
new_df.at[40, '2014 год']=1406104
new_df.at[42, '2014 год']=1361604
new_df.at[45, '2014 год']=44566
new_df.at[21, '2014 год']=88.5

new_df.at[18, 'ПОКАЗАТЕЛЬ']='ВНЕШНЕТОРГОВЫЙ ОБОРОТ (млрд. руб.)'
new_df.at[19, 'ПОКАЗАТЕЛЬ']='экспорт товаров (млрд. руб.)'
new_df.at[20, 'ПОКАЗАТЕЛЬ']='импорт товаров (млрд. руб.)'

new_df.at[18, '2014 год']=73.6
new_df.at[18, '2015 год']=84.8
new_df.at[18, '2016 год']=85.5

new_df.at[19, '2014 год']=39.4
new_df.at[19, '2015 год']=49.5
new_df.at[19, '2016 год']=42

new_df.at[20, '2014 год']=34.2
new_df.at[20, '2015 год']=35.4
new_df.at[20, '2016 год']=43.5

new_df.at[0, 'ПОКАЗАТЕЛЬ']='ВАЛОВОЙ РЕГИОНАЛЬНЫЙ ПРОДУКТ (млрд. руб.)'
new_df.at[1, 'ПОКАЗАТЕЛЬ']='ИНДЕКС ФИЗИЧЕСКОГО ОБЪЕМА ВРП (%)'
new_df.at[45, 'ПОКАЗАТЕЛЬ']='КОЛИЧЕСТВО СУБЪЕКТОВ МАЛОГО И СРЕДНЕГО ПРЕДПРИНИМАТЕЛЬСТВА (единиц)'
new_df.at[50, 'ПОКАЗАТЕЛЬ']='ЧИСЛЕННОСТЬ НАСЕЛЕНИЯ (тыс.чел.)'
new_df.at[51, 'ПОКАЗАТЕЛЬ']='УДЕЛЬНЫЙ ВЕС ГОРОДСКОГО НАСЕЛЕНИЯ В ОБЩЕЙ ЧИСЛЕННОСТИ НАСЕЛЕНИЯ (%)'

new_df =new_df.loc[new_df['ПОКАЗАТЕЛЬ'] != 'КОЛИЧЕСТВО КОНСОЛИДИРОВАННЫХ ГРУПП НАЛОГОПЛАТЕЛЬЩИКОВ (единиц)']
new_df =new_df.loc[new_df['ПОКАЗАТЕЛЬ'] != 'КОЛИЧЕСТВО УЧАСТНИКОВ КОНСОЛИДИРОВАННЫХ ГРУПП НАЛОГОПЛАТЕЛЬЩИКОВ (единиц)']
new_df =new_df.loc[new_df['ПОКАЗАТЕЛЬ'] !='ФОНД НАЧИСЛЕННОЙ ЗАРАБОТНОЙ ПЛАТЫ РАБОТНИКОВ СПИСОЧНОГО СОСТАВА И ВНЕШНИХ СОВМЕСТИТЕЛЕЙ ОРГАНИЗАЦИЙ (по состоянию на 01.01.2017) (млрд. руб.)']
new_df =new_df.loc[new_df['ПОКАЗАТЕЛЬ'] != 'ВНЕШНЕТОРГОВЫЙ ОБОРОТ (млн. долларов США)']
new_df =new_df.loc[new_df['ПОКАЗАТЕЛЬ'] != 'экспорт товаров (млн. долларов США)']
new_df =new_df.loc[new_df['ПОКАЗАТЕЛЬ'] != 'импорт товаров (млн. долларов США)']
new_df =new_df.loc[new_df['ПОКАЗАТЕЛЬ'] != 'КУРС ДОЛЛАРА США (СРЕДНЕГОДОВОЙ) (руб.)']


#Сохраняем таблицу для графика в формате html файла.
os.chdir("C:\\Users\\Кирилл\\Downloads\\PythonProject")
new_df.to_html('Таблица.html',index=False)


# Заводим список, состоящий из данных,взятых из столбцов "2014 год", "2015 год", "2016 год"
my_list1 = new_df["2014 год"].tolist()
my_list2 = new_df["2015 год"].tolist()
my_list3 = new_df["2016 год"].tolist()
z=[]
for i in range(len(my_list1)):
    z.append([my_list1[i],my_list2[i],my_list3[i]])

# Ось X-список teams, trace(i)- характеристика для каждой линии(цвет, имя, значение) для таблицы с параметрами,измеряемыми в %
teams = ['2014 год', '2015 год', '2016 год']
trace1 = go.Scatter(x=teams, y=z[1],
                    marker=dict(color='#6495ED'),
                    name='ИНДЕКС ФИЗИЧЕСКОГО ОБЪЕМА ВВП <br>',
                    text='ИНДЕКС ФИЗИЧЕСКОГО ОБЪЕМА ВВП',
                    xaxis='x2', yaxis='y2')
trace2 = go.Scatter(x=teams, y=z[2],
                    marker=dict(color='#191970'),
                    name='ИНДЕКС ПРОМЫШЛЕННОГО ПРОИЗВОДСТВА<br>',
                    text='ИНДЕКС ПРОМЫШЛЕННОГО ПРОИЗВОДСТВА',
                    xaxis='x2', yaxis='y2')
trace3 = go.Scatter(x=teams, y=z[3],
                    marker=dict(color='#1E90FF'),
                    name='ИНДЕКС ЦЕН ПРОИЗВОДИТЕЛЕЙ ПРОМЫШЛЕННЫХ ТОВАРОВ<br>',
                    text='ИНДЕКС ЦЕН ПРОИЗВОДИТЕЛЕЙ ПРОМЫШЛЕННЫХ ТОВАРОВ',
                    xaxis='x2', yaxis='y2')
trace4 = go.Scatter(x=teams, y=z[4],
                    marker=dict(color='#00BFFF'),
                    name='ИНДЕКС ПРОИЗВОДСТВА ПО ВИДУ ДЕЯТЕЛЬНОСТИ:<br> "ДОБЫЧА ПОЛЕЗНЫХ ИСКОПАЕМЫХ" <br>',
                    text='ИНДЕКС ПРОИЗВОДСТВА ПО ВИДУ ДЕЯТЕЛЬНОСТИ:<br> "ДОБЫЧА ПОЛЕЗНЫХ ИСКОПАЕМЫХ"',
                    xaxis='x2', yaxis='y2')
trace5 = go.Scatter(x=teams, y=z[5],
                    marker=dict(color='#4682B4'),
                    name='ИНДЕКС ПРОИЗВОДСТВА ПО ВИДУ ДЕЯТЕЛЬНОСТИ:<br> "ОБРАБАТЫВАЮЩИЕ ПРОИЗВОДСТВА"<br>',
                    text='ИНДЕКС ПРОИЗВОДСТВА ПО ВИДУ ДЕЯТЕЛЬНОСТИ:<br> "ОБРАБАТЫВАЮЩИЕ ПРОИЗВОДСТВА"',
                    xaxis='x2', yaxis='y2')
trace6 = go.Scatter(x=teams, y=z[6],
                    marker=dict(color='#483D8B'),
                    name='ИНДЕКС ПРОИЗВОДСТВА ПО ВИДУ ДЕЯТЕЛЬНОСТИ:<br> "ПРОИЗВОДСТВО И РАСПРЕДЕЛЕНИЕ ЭЛЕКТРОЭНЕРГИИ, ГАЗА И ВОДЫ"<br>',
                    text='ИНДЕКС ПРОИЗВОДСТВА ПО ВИДУ ДЕЯТЕЛЬНОСТИ:<br> "ПРОИЗВОДСТВО И РАСПРЕДЕЛЕНИЕ ЭЛЕКТРОЭНЕРГИИ, ГАЗА И ВОДЫ"',
                    xaxis='x2', yaxis='y2')
trace25 = go.Scatter(x=teams, y=z[21],
                    marker=dict(color='#49ff00'),
                    name='УДЕЛЬНЫЙ ВЕС ПРИБЫЛЬНЫХ ПРЕДПРИЯТИЙ <br>',
                    text='УДЕЛЬНЫЙ ВЕС ПРИБЫЛЬНЫХ ПРЕДПРИЯТИЙ ',
                    xaxis='x2', yaxis='y2')
trace26 = go.Scatter(x=teams, y=z[22],
                    marker=dict(color='#FF0000'),
                    name='УДЕЛЬНЫЙ ВЕС УБЫТОЧНЫХ ПРЕДПРИЯТИЙ<br>',
                    text='УДЕЛЬНЫЙ ВЕС УБЫТОЧНЫХ ПРЕДПРИЯТИЙ<br>',
                    xaxis='x2', yaxis='y2')
trace31 = go.Scatter(x=teams, y=z[27],
                    marker=dict(color='#FFA07A'),
                    name='ИНДЕКС ПОТРЕБИТЕЛЬСКИХ ЦЕН<br>',
                    text='ИНДЕКС ПОТРЕБИТЕЛЬСКИХ ЦЕН<br>',
                    xaxis='x2', yaxis='y2')
trace32 = go.Scatter(x=teams, y=z[28],
                    marker=dict(color='#FF6347'),
                    name='РЕАЛЬНЫЕ ДЕНЕЖНЫЕ ДОХОДЫ<br>',
                    text='РЕАЛЬНЫЕ ДЕНЕЖНЫЕ ДОХОДЫ<br>',
                    xaxis='x2', yaxis='y2')
trace35 = go.Scatter(x=teams, y=z[30],
                    marker=dict(color='#FF8C00'),
                    name='РЕАЛЬНАЯ СРЕДНЕМЕСЯЧНАЯ НАЧИСЛЕННАЯ ЗАРАБОТНАЯ ПЛАТА ОДНОГО РАБОТНИКА<br>',
                    text='РЕАЛЬНАЯ СРЕДНЕМЕСЯЧНАЯ НАЧИСЛЕННАЯ ЗАРАБОТНАЯ ПЛАТА ОДНОГО РАБОТНИКА<br>',
                    xaxis='x2', yaxis='y2')
trace51 = go.Scatter(x=teams, y=z[44],
                    marker=dict(color='#FFD700'),
                    name='УДЕЛЬНЫЙ ВЕС ГОРОДСКОГО НАСЕЛЕНИЯ В ОБЩЕЙ ЧИСЛЕННОСТИ НАСЕЛЕНИЯ <br>',
                    text='УДЕЛЬНЫЙ ВЕС ГОРОДСКОГО НАСЕЛЕНИЯ В ОБЩЕЙ ЧИСЛЕННОСТИ НАСЕЛЕНИЯ <br>',
                    xaxis='x2', yaxis='y2')

# Формирование фигуры и добавление линий
figure= go.Figure(data=[trace1])
figure.add_traces([trace2, trace3,trace4,trace5,trace6,trace25,trace26,trace31,trace32,trace35,trace51])

# Изменение характеристик фигуры
figure.layout.margin.update({'t':75, 'b':100})
figure.layout.update({'height':800})
# Изменение параметров легенды(списка с наименованиями)
figure.update_layout(
    legend=go.layout.Legend(
        x=1,
        y=1,
        traceorder="normal",
        font=dict(
            family="sans-serif",
            size=10,
            color="black"
        ),
        bgcolor="LightSteelBlue",
        bordercolor="Black",
        borderwidth=2
    )

)
# Добавить подпись к оси Y
figure['layout']['xaxis2'] = {}
figure['layout']['yaxis2'] = {}
figure.layout.yaxis.update({'domain': [0, .45]})
figure.layout.yaxis2.update({'title': 'В %'})
# Сохранить и вывести на экран получившийся график
plot(figure, filename='Vizualization_Table.html')

time.sleep(2)

# Конвертирование данных в нужный формат
for i in range(len(z[29])):
    z[29][i]=round((z[29][i]/1000),1)
    z[35][i]=round((z[35][i]/1000),1)
    z[36][i]=round((z[36][i]/1000),1)
    z[37][i]=round((z[37][i]/1000),1)
    z[38][i]=round((z[38][i]/1000),1)
    z[39][i]=round((z[39][i]/1000),1)
    z[40][i]=round((z[40][i]/1000),1)


# trace(i)- характеристика для каждой линии(цвет, имя, значение) для таблицы с параметрами,измеряемыми в тысячах единиц
trace40 = go.Scatter(x=teams, y=z[35],
                    marker=dict(color='#FF0000'),
                    name='КОЛИЧЕСТВО НАЛОГОПЛАТЕЛЬЩИКОВ <br>',
                    text='КОЛИЧЕСТВО НАЛОГОПЛАТЕЛЬЩИКОВ <br>',
                    xaxis='x2', yaxis='y2')
trace41 = go.Scatter(x=teams, y=z[36],
                    marker=dict(color='#CD5C5C'),
                    name='КОЛИЧЕСТВО ЮРИДИЧЕСКИХ ЛИЦ,<br> СВЕДЕНИЯ О КОТОРЫХ СОДЕРЖАТСЯ В ЕГРЮЛ<br>',
                    text='КОЛИЧЕСТВО ЮРИДИЧЕСКИХ ЛИЦ,<br> СВЕДЕНИЯ О КОТОРЫХ СОДЕРЖАТСЯ В ЕГРЮЛ<br>',
                    xaxis='x2', yaxis='y2')
trace42 = go.Scatter(x=teams, y=z[37],
                    marker=dict(color='#FE2EC8'),
                    name='КОЛИЧЕСТВО ФИЗИЧЕСКИХ ЛИЦ <br>',
                    text='КОЛИЧЕСТВО ФИЗИЧЕСКИХ ЛИЦ <br>',
                    xaxis='x2', yaxis='y2')
trace43 = go.Scatter(x=teams, y=z[38],
                    marker=dict(color='#FF7F50'),
                    name='КОЛИЧЕСТВО ИНДИВИДУАЛЬНЫХ ПРЕДПРИНИМАТЕЛЕЙ <br> И КРЕСТЬЯНСКИХ (ФЕРМЕРСКИХ) ХОЗЯЙСТВ,<br> СВЕДЕНИЯ О КОТОРЫХ СОДЕРЖАТСЯ В ЕГРИП<br>',
                    text='КОЛИЧЕСТВО ИНДИВИДУАЛЬНЫХ ПРЕДПРИНИМАТЕЛЕЙ <br> И КРЕСТЬЯНСКИХ (ФЕРМЕРСКИХ) ХОЗЯЙСТВ,<br> СВЕДЕНИЯ О КОТОРЫХ СОДЕРЖАТСЯ В ЕГРИП<br>',
                    xaxis='x2', yaxis='y2')
trace44 = go.Scatter(x=teams, y=z[39],
                    marker=dict(color='#FF0040'),
                    name='ИНДИВИДУАЛЬНЫЕ ПРЕДПРИНИМАТЕЛИ,<br>СВЕДЕНИЯ О КОТОРЫХ СОДЕРЖАТСЯ В ЕГРИП<br>',
                    text='ИНДИВИДУАЛЬНЫЕ ПРЕДПРИНИМАТЕЛИ,<br>СВЕДЕНИЯ О КОТОРЫХ СОДЕРЖАТСЯ В ЕГРИП<br>',
                    xaxis='x2', yaxis='y2')
trace45 = go.Scatter(x=teams, y=z[40],
                    marker=dict(color='#FACC2E'),
                    name='КОЛИЧЕСТВО СУБЪЕКТОВ МАЛОГО И СРЕДНЕГО ПРЕДПРИНИМАТЕЛЬСТВА<br>',
                    text='КОЛИЧЕСТВО СУБЪЕКТОВ МАЛОГО И СРЕДНЕГО ПРЕДПРИНИМАТЕЛЬСТВА<br>',
                    xaxis='x2', yaxis='y2')
trace37 = go.Scatter(x=teams, y=z[32],
                    marker=dict(color='#00FF00'),
                    name='ЧИСЛЕННОСТЬ РАБОЧЕЙ СИЛЫ <br>(ЭКОНОМИЧЕСКИ АКТИВНОГО НАСЕЛЕНИЯ) <br>',
                    text='ЧИСЛЕННОСТЬ РАБОЧЕЙ СИЛЫ <br>(ЭКОНОМИЧЕСКИ АКТИВНОГО НАСЕЛЕНИЯ) <br>',
                    xaxis='x2', yaxis='y2')
trace38 = go.Scatter(x=teams, y=z[33],
                    marker=dict(color='#2E8B57'),
                    name='ЗАНЯТЫЕ<br>',
                    text='ЗАНЯТЫЕ<br>',
                    xaxis='x2', yaxis='y2')
trace39 = go.Scatter(x=teams, y=z[34],
                    marker=dict(color='#006400'),
                    name='БЕЗРАБОТНЫЕ<br>',
                    text='БЕЗРАБОТНЫЕ<br>',
                    xaxis='x2', yaxis='y2')
trace50 = go.Scatter(x=teams, y=z[43],
                    marker=dict(color='#7FFF00'),
                    name='ЧИСЛЕННОСТЬ НАСЕЛЕНИЯ <br>',
                    text='ЧИСЛЕННОСТЬ НАСЕЛЕНИЯ <br>',
                    xaxis='x2', yaxis='y2')
figshow= go.Figure(data=[trace40])
figshow.add_traces([trace41, trace42,trace43,trace44,trace45,trace37,trace38,trace39,trace50])

# Изменение характеристик фигуры
figshow.layout.margin.update({'t':50, 'b':50})
figshow.layout.update({'height':800})
figshow.update_layout(
    legend=go.layout.Legend(
        x=1,
        y=1,
        traceorder="normal",
        font=dict(
            family="sans-serif",
            size=12,
            color="black"
        ),
        bgcolor="LightSteelBlue",
        bordercolor="Black",
        borderwidth=2
    )

)

# Добавить подпись к оси Y
figshow['layout']['xaxis2'] = {}
figshow['layout']['yaxis2'] = {}
figshow.layout.yaxis.update({'domain': [0, .45]})
figshow.layout.yaxis2.update({'title': 'В тысячах единиц'})

# Сохранить и вывести на экран получившийся график
plot(figshow, filename='Vizualization_Table4.html')

time.sleep(2)

# trace(i)- характеристика для каждой линии(цвет, имя, значение) для таблицы с параметрами,измеряемыми в млрд. руб.
trace0 = go.Scatter(x=teams, y=z[0],
                    marker=dict(color='#000000'),
                    name='ВАЛОВОЙ РЕГИОНАЛЬНЫЙ ПРОДУКТ<br>',
                    text='ВАЛОВОЙ РЕГИОНАЛЬНЫЙ ПРОДУКТ',
                    xaxis='x2', yaxis='y2')
trace7 = go.Scatter(x=teams, y=z[7],
                    marker=dict(color='#6B8E23'),
                    name='ОБЪЕМ ОТГРУЖЕННЫХ ТОВАРОВ СОБСТВЕННОГО ПРОИЗВОДСТВА,<br>ВЫПОЛНЕННЫХ РАБОТ И УСЛУГ <br>СОБСТВЕННЫМИ СИЛАМИ ПО ДОБЫЧЕ ПОЛЕЗНЫХ ИСКОПАЕМЫХ<br>',
                    text='ОБЪЕМ ОТГРУЖЕННЫХ ТОВАРОВ СОБСТВЕННОГО ПРОИЗВОДСТВА,<br>ВЫПОЛНЕННЫХ РАБОТ И УСЛУГ <br>СОБСТВЕННЫМИ СИЛАМИ ПО ДОБЫЧЕ ПОЛЕЗНЫХ ИСКОПАЕМЫХ<br>',
                    xaxis='x2', yaxis='y2')
trace8 = go.Scatter(x=teams, y=z[8],
                    marker=dict(color='#32CD32'),
                    name='ОБЪЕМ ОТГРУЖЕННЫХ ТОВАРОВ СОБСТВЕННОГО ПРОИЗВОДСТВА,<br> ВЫПОЛНЕННЫХ РАБОТ И УСЛУГ <br>СОБСТВЕННЫМИ СИЛАМИ ОБРАБАТЫВАЮЩИХ ПРОИЗВОДСТВ<br>',
                    text='ОБЪЕМ ОТГРУЖЕННЫХ ТОВАРОВ СОБСТВЕННОГО ПРОИЗВОДСТВА,<br> ВЫПОЛНЕННЫХ РАБОТ И УСЛУГ <br>СОБСТВЕННЫМИ СИЛАМИ ОБРАБАТЫВАЮЩИХ ПРОИЗВОДСТВ<br>',
                    xaxis='x2', yaxis='y2')
trace9 = go.Scatter(x=teams, y=z[9],
                    marker=dict(color='#008000'),
                    name='ОБЪЕМ ОТГРУЖЕННЫХ ТОВАРОВ СОБСТВЕННОГО ПРОИЗВОДСТВА,<br> ВЫПОЛНЕННЫХ РАБОТ И УСЛУГ<br> СОБСТВЕННЫМИ СИЛАМИ ПО ПРОИЗВОДСТВУ И РАСПРЕДЕЛЕНИЮ  <br>ЭЛЕКТРОЭНЕРГИИ, ГАЗА И ВОДЫ<br>',
                    text='ОБЪЕМ ОТГРУЖЕННЫХ ТОВАРОВ СОБСТВЕННОГО ПРОИЗВОДСТВА,<br> ВЫПОЛНЕННЫХ РАБОТ И УСЛУГ<br> СОБСТВЕННЫМИ СИЛАМИ ПО ПРОИЗВОДСТВУ И РАСПРЕДЕЛЕНИЮ  <br>ЭЛЕКТРОЭНЕРГИИ, ГАЗА И ВОДЫ<br>',
                    xaxis='x2', yaxis='y2')
trace10 = go.Scatter(x=teams, y=z[10],
                    marker=dict(color='#808000'),
                    name='ОБЪЕМ ПРОДУКЦИИ СЕЛЬСКОГО ХОЗЯЙСТВА<br>',
                    text='ОБЪЕМ ПРОДУКЦИИ СЕЛЬСКОГО ХОЗЯЙСТВА<br>',
                    xaxis='x2', yaxis='y2')
trace21 = go.Scatter(x=teams, y=z[17],
                    marker=dict(color='#008080'),
                    name='ИНВЕСТИЦИИ В ОСНОВНОЙ КАПИТАЛ<br>',
                    text='ИНВЕСТИЦИИ В ОСНОВНОЙ КАПИТАЛ<br>',
                    xaxis='x2', yaxis='y2')
trace22 = go.Scatter(x=teams, y=z[18],
                    marker=dict(color='#FF0000'),
                    name='САЛЬДИРОВАННЫЙ ФИНАНСОВЫЙ РЕЗУЛЬТАТ <br>(ПРИБЫЛЬ МИНУС УБЫТОК)<br>',
                    text='САЛЬДИРОВАННЫЙ ФИНАНСОВЫЙ РЕЗУЛЬТАТ <br>(ПРИБЫЛЬ МИНУС УБЫТОК)<br>',
                    xaxis='x2', yaxis='y2')
trace23 = go.Scatter(x=teams, y=z[19],
                    marker=dict(color='#800080'),
                    name='СУММА ПРИБЫЛИ ПО ПРИБЫЛЬНЫМ ОРГАНИЗАЦИЯМ<br>',
                    text='СУММА ПРИБЫЛИ ПО ПРИБЫЛЬНЫМ ОРГАНИЗАЦИЯМ<br>',
                    xaxis='x2', yaxis='y2')
trace24 = go.Scatter(x=teams, y=z[20],
                    marker=dict(color='#4169E1'),
                    name='СУММА УБЫТКА ПРЕДПРИЯТИЙ<br>',
                    text='СУММА УБЫТКА ПРЕДПРИЯТИЙ<br>',
                    xaxis='x2', yaxis='y2')
trace27 = go.Scatter(x=teams, y=z[23],
                    marker=dict(color='#8B4513'),
                    name='КРЕДИТОРСКАЯ ЗАДОЛЖЕННОСТЬ <br>',
                    text='КРЕДИТОРСКАЯ ЗАДОЛЖЕННОСТЬ <br>',
                    xaxis='x2', yaxis='y2')
trace28 = go.Scatter(x=teams, y=z[24],
                    marker=dict(color='#DAA520'),
                    name='Просроченная кредиторская задолженность<br>',
                    text='Просроченная кредиторская задолженность<br>',
                    xaxis='x2', yaxis='y2')
trace29 = go.Scatter(x=teams, y=z[25],
                    marker=dict(color='#8059ff'),
                    name='ДЕБИТОРСКАЯ ЗАДОЛЖЕННОСТЬ<br>',
                    text='ДЕБИТОРСКАЯ ЗАДОЛЖЕННОСТЬ<br>',
                    xaxis='x2', yaxis='y2')
trace30 = go.Scatter(x=teams, y=z[26],
                    marker=dict(color='#EE82EE'),
                    name='Просроченная дебиторская задолженность<br>',
                    text='Просроченная дебиторская задолженность<br>',
                    xaxis='x2', yaxis='y2')
trace19 = go.Scatter(x=teams, y=z[15],
                    marker=dict(color='#FF4500'),
                    name='Экспорт товаров<br>',
                    text='Экспорт товаров<br>',
                    xaxis='x2', yaxis='y2')
trace20 = go.Scatter(x=teams, y=z[16],
                    marker=dict(color='#FFD700'),
                    name='Импорт товаров<br>',
                    text='Импорт товаров<br>',
                    xaxis='x2', yaxis='y2')
trace11 = go.Scatter(x=teams, y=z[11],
                    marker=dict(color='#3CB371'),
                    name='ОБЪЕМ РАБОТ,<br> ВЫПОЛНЕННЫХ ПО ВИДУ ДЕЯТЕЛЬНОСТИ "СТРОИТЕЛЬСТВО"<br>',
                    text='ОБЪЕМ РАБОТ,<br> ВЫПОЛНЕННЫХ ПО ВИДУ ДЕЯТЕЛЬНОСТИ "СТРОИТЕЛЬСТВО"<br>',
                    xaxis='x2', yaxis='y2')
trace12 = go.Scatter(x=teams, y=z[12],
                    marker=dict(color='#FFA07A'),
                    name='ОБОРОТ РОЗНИЧНОЙ ТОРГОВЛИ<br>',
                    text='ОБОРОТ РОЗНИЧНОЙ ТОРГОВЛИ<br>',
                    xaxis='x2', yaxis='y2')
trace13 = go.Scatter(x=teams, y=z[13],
                    marker=dict(color='#CD5C5C'),
                    name='ОБОРОТ ОПТОВОЙ ТОРГОВЛИ ОРГАНИЗАЦИЙ ОПТОВОЙ ТОРГОВЛИ<br>',
                    text='ОБОРОТ ОПТОВОЙ ТОРГОВЛИ ОРГАНИЗАЦИЙ ОПТОВОЙ ТОРГОВЛИ<br>',
                    xaxis='x2', yaxis='y2')

# Формирование фигуры и добавление линий
figeshow= go.Figure(data=[trace0])
figeshow.add_traces([ trace7,trace8,trace9,trace10,trace11,trace21,trace22,trace23,trace24,trace27,trace28,trace29,trace30,trace19,trace20,trace12,trace13])

# Изменение характеристик фигуры
figeshow.layout.margin.update({'t':50, 'b':50})
figeshow.layout.update({'height':800})
figeshow.update_layout(
    legend=go.layout.Legend(
        x=1,
        y=1,
        traceorder="normal",
        font=dict(
            family="sans-serif",
            size=11,
            color="black"
        ),
        bgcolor="LightSteelBlue",
        bordercolor="Black",
        borderwidth=2
    )

)

# Добавить подпись к оси Y
figeshow['layout']['xaxis2'] = {}
figeshow['layout']['yaxis2'] = {}
figeshow.layout.yaxis.update({'domain': [0, .45]})
figeshow.layout.yaxis2.update({'title': 'В млрд. руб.'})

# Сохранить и вывести на экран получившийся график
plot(figeshow, filename='Vizualization_Table5.html')
