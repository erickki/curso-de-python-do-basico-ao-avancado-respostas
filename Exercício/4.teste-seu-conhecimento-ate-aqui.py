nome = input(f"Digite seu nome: ")
idade = input(f"Digite sua idade: ")

if nome == "" or idade == "":
    print(f"Desculpe, você deixou campos vazios.")
else:
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome[::-1]}")
    if '' in nome:
        print(f"Seu nome contém espaços")
    else:
        print(f"Seu nome não contém espaços")
    print(f"Seu nome tem {len(nome)} letras")
    print(f"A primeira letra do seu nome é {nome[0:1:]}")
    print(f"A última letra do seu nome é {nome[-1:-2:-1]}")