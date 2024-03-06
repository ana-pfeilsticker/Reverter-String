
#o que é fibonacci { 1, 1, 2, 3, 5, 8 ...} a sequencia se da pela soma de um numero com o seu anterior



def pertenceFib(numero): # teste com o 8 {1, 1, 2, 3, 5  8 }
    prev, num = 0, 1

    while num < numero:
        prev, num = num, num + prev     ##1, 0 = 1, 1  / 1, 1 = 2, 1  /2, 1 = 3, 2/ 3, 2 = 5, 3 /5, 3 = 8, 5/ ou seja, num = 8, fim da iteração

    if num == numero:
        return True
    else:
        return False

numeroInformado = int(input("Informe um número: "))  # teste com o 8 {1, 1, 2, 3, 5  8 }

if pertenceFib(numeroInformado):
    print(f"{numeroInformado} pertence à sequência de Fibonacci.")
else:
    print(f"{numeroInformado} não pertence à sequência de Fibonacci.")
