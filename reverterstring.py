# vamos reverter strings, por exemplo "banana" vai virar "ananab"

#por slicing 
def reverterString(stringParaReverter):
    return stringParaReverter[::-1] ##pegamos a string do inicio ao fim e percorremos ela de trás para frente para criarmos uma substring invertida


stringPassada = string(input("Informe uma string:"))
stringinvertida = reverterString(stringPassada)

print("String invertida:", stringinvertida)
