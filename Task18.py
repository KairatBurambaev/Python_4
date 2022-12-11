import random
def inputN(inputN):
    while True:
        try:
            k = int(input(f'{inputN}'))
            return k
        except ValueError:
            print('Введите число')
k = inputN('Введите максимальную степень k: ')
koef_list = []
for i in range(k):
    i = random.randint(0,100)
    koef_list.append(i)
mnogoX = ''
X = 0
for i in koef_list:
    if i > 0:
        if k == 1:
            k = ''
            if i == 1:
                i = ''
            X = str(i) + 'x' + '^' + str(k) + '+'
            mnogoX = mnogoX + X
        else:
            if i == 1:
                i = ''
            X = str(i) + 'x' + '^' + str(k) + '+'
            mnogoX = mnogoX + X
            k = k - 1
mnogoX = mnogoX[:-2] + '+' + str(random.randint(0,100)) + '=0'
data = open('mnogochlen1.txt', 'w')
data.write(mnogoX)
data.close()
print(mnogoX)