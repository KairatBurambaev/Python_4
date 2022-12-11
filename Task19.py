data = open('mnogochlen1.txt', 'r')
mnogoX1 = [line for line in data]
data.close()
data = open('mnogochlen2.txt', 'r')
mnogoX2 = [line for line in data]
data.close()
print(mnogoX1, '\n',mnogoX2)