import random
def inputK():
    while True:
        try:
            k = int(input('Введите максимальную степень k: '))
            return k
        except ValueError:
            print('Введите число')
k = inputK()

mnogoX = ''

for i in range(k + 1):
    step = k - i

    koef = random.randint(0, 100)
    koef_str = str(koef)

    if koef == 0:
        continue

    if koef == 1 and step != 0:
        koef_str = ''

    if mnogoX != '':
        koef_str = '+' + koef_str

    if step > 1:
        X = f'{koef_str}x^{step}'
    elif step == 1:
        X = f'{koef_str}x'
    elif step == 0:
        X = koef_str

    mnogoX = mnogoX + X

mnogoX = mnogoX + '=0'

data = open('mnogochlen1.txt', 'w')
data.write(mnogoX)
data.close()

print(mnogoX)