import math
def inputN(inputN):
    while True:
        try:
            N = int(input(f'{inputN}'))
            N = list(range(1,N+1))
            return N
        except ValueError:
            print('Введите натуральное число')
N = inputN('Введите натуральное число: ')
list_number = []
for i in N:
    if max(N) % i == 0:
        list_number.append(i)
print(list_number)