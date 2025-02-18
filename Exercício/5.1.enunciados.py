numero_inteiro = input(f"Digite um número inteiro: ")
try:
    numero_inteiro = int(numero_inteiro)
    par_impar_resto = numero_inteiro % 2
    if par_impar_resto > 0:
        print(f"O número {numero_inteiro} é ímpar")
    else:
        print(f"O número {numero_inteiro} é par")
except:
    print(f"O número {numero_inteiro} não é um número inteiro")