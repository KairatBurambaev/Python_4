def inputN(inputN):
    while True:
        try:
            N = int(input(inputN))
            return N
        except ValueError:
            print('Введите натуральное число')

N = inputN('Введите натуральное число: ')

def function(i):
    if N % i == 0:
        return i  

list_number = list(filter(function,[i for i in range(1,N+1)]))

print(list_number)