import random
def inputN(inputN):
    while True:
        try:
            N = int(input(f'{inputN}'))
            return N
        except ValueError:
            print('Введите число')
N = inputN('Введите число: ')
new_list =list(range(1,N+1))
new_list2 = []
for i in new_list:
    i = random.randint(1,25)
    new_list2.append(i)
new_list2.sort()
print('случайный список: ',new_list2,'\nнеповторяющиеся элементы: ',set(new_list2))