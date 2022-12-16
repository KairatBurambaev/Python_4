import random
def inputN(inputN):
    while True:
        try:
            N = int(input(inputN))
            return N
        except ValueError:
            print('Введите число')

N = inputN('Введите число: ')

def function(x):
    return random.randint(1,10)

original_list = list(map(function,[i for i in range(N)]))

unique_list = []
for elem in original_list:
    if elem not in unique_list:
        unique_list.append(elem)

print('случайный список: ', original_list)
print('неповторяющиеся элементы: ', unique_list)