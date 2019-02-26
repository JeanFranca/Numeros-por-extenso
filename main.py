
from ConvertNumbers import Number
num = input('Digite um número: ')

if num != '0':
    try: 
        n = Number(num)
        print (n.literal)
    except ValueError:
        print("Valor inválido")
else:
    print("zero")

