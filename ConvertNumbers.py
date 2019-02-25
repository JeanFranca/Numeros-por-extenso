import math

units = ["","um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
dozens = ["","dez", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
hundreds = ["","cem", "duzentos", "trezentos", "quatrocentos", "quinhentos", "seiscentos", "setecentos", "oitocentos", "novecentos"]
primaryTens = ["dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
numberType = ["", "mil","milhão", "bilhão", "trilhão", "quatrilhão"]
numbersType = ["", "mil", "milhões", "bilhões", "trilhões", "quatrilhões"]

class AllNumbers:  

    def __init__(self, num):
        self.num = num
        self.invertedNum = str(self.num[::-1])

    #this function verifies that you have received only numbers
    def startConvert(self):
        n = self.num
        if n.isdigit():
            return True
        else:
            return False

    def convertNumbers(self):
        vet = []
        for i in range(len(self.invertedNum)):
            #essa parte traduz a unidade e diz o tipo do numero
            if (i % 3) == 0:

                if (int(self.invertedNum[i]) > 1) and ((i - 1 > 0) or (i - 2 > 0)):
                    vet.append(numbersType[math.floor(i / 3)])
                else:
                    vet.append(numberType[math.floor(i / 3)])
                    
                if(((i + 1) < len(self.invertedNum)) and (int(self.invertedNum[i + 1]) != 1)):
                    vet.append(units[int(self.invertedNum[i])])
                else:
                    vet.append(units[int(self.invertedNum[i])])
                
            #já essa parte traduz a dezena
            elif (i % 3) == 1:
                if(int(self.invertedNum[i]) == 1):
                    vet.append(primaryTens[int(self.invertedNum[i - 1])])
                else:
                    if(int(self.invertedNum[i - 1])!=0):
                        vet.append(dozens[int(self.invertedNum[i])] + " e")
                    else:
                        vet.append(dozens[int(self.invertedNum[i])])
                
            #e por ultimo essa parte traduz a centena
            else:
                if(int(self.invertedNum[i]) == 1):
                    if(int(self.invertedNum[i - 1]) != 0):
                        vet.append("cento e")
                    elif(int(self.invertedNum[i - 2]) != 0):
                        vet.append("cento e")
                    else:
                        vet.append(hundreds[int(self.invertedNum[i])])
                else:
                    vet.append(hundreds[int(self.invertedNum[i])])
        vet = vet[::-1]
        return vet

    def createString(self, vet):
        extendedNum = ""
        for i in range(len(vet)):
            if vet[i] != " e":
                extendedNum += vet[i]
                extendedNum += " "
        print(extendedNum)