hora = float(input(f"Digite um horário: "))
if 0 <= hora <= 11:
    print(f"Bom dia")
elif 12 <= hora <= 17:
    print(f"Bam tarde")
else:
    print(f"Bam noite")