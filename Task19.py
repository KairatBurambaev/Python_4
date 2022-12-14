data = open('mnogochlen1.txt', 'r')
mnogoX1 = data.read()
data.close()
data = open('mnogochlen2.txt', 'r')
mnogoX2 = data.read()
data.close()

mnogoX1 = mnogoX1[:-2].split('+')
mnogoX2 = mnogoX2[:-2].split('+')

one = [i for i in mnogoX1]
one1 = [i for i in mnogoX2]

resOne = {}
resOne1 = {}

def dictionary(x, y):
    for i in x:
        if 'x^' in i:
            i = i.split('x^')
            i.reverse()
            y[i[0]] = int(i[1])
        elif 'x' in i and '^' not in i:
            i = i.split('x')
            i.reverse()
            y[1] = int(i[1])
        else: 
            y[0] = int(i)
    return y

dictionary(one,resOne)
dictionary(one1,resOne1)

for key in resOne1.keys():
    if key in resOne:
        resOne[key] += resOne1[key]
    else:
        resOne[key] = resOne1[key]

result = '+'.join([f'{key}x^{value}' for value, key in resOne.items()])

result = result.replace('^1','')
result = result.replace('x^0','') + '=0'
   
print(result)