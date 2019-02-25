
from ConvertNumbers import AllNumbers
num = input('Digite um número: ')

if num != '0':
    n = AllNumbers(num)
    if n.startConvert():
        vetor = n.convertNumbers()
        n.createString(vetor)
else:
    print("zero")

