import csv
import pandas
import os

# Редактирование файла для визуализации
os.chdir("C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2016\\Отсортированные разделы")
z=[]
file=open('База2016(1часть).csv',encoding="cp1251")
reader = csv.reader(file)
for row in reader:
    if 'ПЛОЩАДЬ ТЕРРИТОРИИ' in row[1]:
        z.append(row)
    if row[1]!='' and row[2]!='' :
                z.append(row)
p=[]
for i in range(len(z)):
    if i==1 or i==2:
        p.append(z[i])
    if i>=4:
        p.append(z[i])
p=p[0:-2]
rpk=[]
value=[]
for i in range(len(p)):
    del p[i][2]
    for k in range(len(p[i])):
        if p[i][k]=='':
            p[i][k]='-'
        if p[i][k]=='X':
            p[i][k]='-'
        if k==1 and i>1:
            rpk.append(p[i][1])
        if k==2 and i>1:
            value.append(p[i][1:])
np=p[1][1]
rp=p[1][2]
dp=p[1][3]
df = pandas.DataFrame(value,columns=(np, rp, dp),index=(rpk))

# Сохраняем результат в папку "очищенные результаты для 1 таблицы"
os.chdir("C:\\Users\\Кирилл\\Downloads\\PythonProject\\год2016\\очищенные результаты для 1 таблицы")
df.to_csv("result1part(2016).csv",encoding='cp1251', sep=';',index=False)
