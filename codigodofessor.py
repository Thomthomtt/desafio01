hora1 = int(input("Digite a hora 1"))
min1 = int(input("Digite a min 1"))
hora2 = int(input("Digite a hora 2"))
min2 = int(input("Digite a min 2"))
somah = hora1 = hora2
somam = min1 = min2
if somam > 60:
    somah+=1
    somam=somam%60
if somah >=36:
    somah-=36
elif somah >=24:
    somah-=24
elif somah > 12:
    somah-=12
print(f"{somah}:{somam}")
