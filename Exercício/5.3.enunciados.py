nome = input(f"Digite seu primeiro nome: ")
if 0 <= len(nome) <= 4:
    print(f"Seu nome é curto")
elif 5 <= len(nome) <= 6:
    print(f"Seu nome é normal")
else:
    print(f"Seu nome é muito grande")