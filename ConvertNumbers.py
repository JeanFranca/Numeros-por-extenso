import math

class Number:  
    units = ["","um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
    dozens = ["","dez", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
    hundreds = ["","cem", "duzentos", "trezentos", "quatrocentos", "quinhentos", "seiscentos", "setecentos", "oitocentos", "novecentos"]
    primaryTens = ["dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
    numberType = ["", "mil","milhão", "bilhão", "trilhão", "quatrilhão"]
    numbersType = ["", "mil", "milhões", "bilhões", "trilhões", "quatrilhões"]

    def __init__(self, num):
        if not num.isdigit():
            raise ValueError("Invalid number {} provided".format(num))
        self._num = num
        self._literal = None
    
    @property
    def literal(self):
        if self._literal == None:
            self._literal = self.to_literal()
        return self._literal 


    def to_literal(self):
        inverted_number = self._num[::-1]
        vet = []
        for i in range(len(inverted_number)):
            #essa parte traduz a unidade e diz o tipo do numero
            if (i % 3) == 0:
                if (int(inverted_number[i]) > 1) and ((i - 1 > 0) or (i - 2 > 0)):
                    vet.append(Number.numbersType[int(i / 3)])
                else:
                    vet.append(Number.numberType[int(i / 3)])
                    
                if(((i + 1) < len(inverted_number)) and (int(inverted_number[i + 1]) != 1)):
                    vet.append(Number.units[int(inverted_number[i])])                

            #já essa parte traduz a dezena
            elif (i % 3) == 1:
                if(int(inverted_number[i]) == 1):
                    vet.append(Number.primaryTens[int(inverted_number[i - 1])])
                else:
                    if(int(inverted_number[i - 1])!=0):
                        vet.append(Number.dozens[int(inverted_number[i])] + " e")
                    else:
                        vet.append(Number.dozens[int(inverted_number[i])])
            #e por ultimo essa parte traduz a centena
            else:
                if(int(inverted_number[i]) == 1):
                    if(int(inverted_number[i - 1]) != 0):
                        vet.append("cento e")
                    elif(int(inverted_number[i - 2]) != 0):
                        vet.append("cento e")
                    else:
                        vet.append(Number.hundreds[int(inverted_number[i])])
                else:
                    vet.append(Number.hundreds[int(inverted_number[i])])

        vet = vet[::-1]
        return " ".join(vet)