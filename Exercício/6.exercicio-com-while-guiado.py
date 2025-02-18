nome = "Erick Rodrigues"

indice = 0
novo_nome = ""
while indice < len(nome):
    print(nome[indice])
    letra = nome[indice]
    novo_nome += f"[{letra}]"
    print(novo_nome)
    indice += 1
