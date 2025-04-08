entrada_h1 = int(input("Digite a primeira hora: "))
entrada_min1 = int(input("Digite os minutos da primeira hora:"))
entrada_h2 = int(input("Digite a segunda hora:"))
entrada_min2 = int(input("Digite os minutos da segunda hora:"))
soma_minutos = entrada_min1+entrada_min2
if entrada_h1 >= 12:
    entrada_h1 = entrada_h1 - 12
if entrada_h2 >= 12:
    entrada_h2 = entrada_h2 - 12
soma_horas = entrada_h1 + entrada_h2
if soma_minutos >= 60:
    soma_horas = soma_horas+1
    soma_minutos = soma_minutos - 60
if soma_horas > 12:
    soma_horas -=12
print(f"{soma_horas}:{soma_minutos}")



