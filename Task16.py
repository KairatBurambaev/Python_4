def inputN(inputN):
    while True:
        try:
            N = int(input(inputN))
            return N
        except ValueError:
            print('Введите натуральное число')

N = inputN('Введите натуральное число: ')

list_number = [i for i in range(1,N+1) if N % i == 0]

print(list_number)