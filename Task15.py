d = input('Введите с какой точностью вывести Пи: ')
d = len(d)
from math import pi
result = ''
p = str(round(pi,20))
for i in p:
    if d>0:
        result = result + i
        d = d - 1
print(result)