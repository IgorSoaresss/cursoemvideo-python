print("-="*12)
print("Analisador de Triângulos")
print("-="*12)

r1 = float(input("Primeiro lado: "))
r2 = float(input("Segundo lado: "))
r3 = float(input("Terceiro lado: "))

if r1 >= r2 + r3 or r2 >= r1 + r3 or r3 >= r1 + r2:
    print("Esses segmentos NÃO podem formar um triângulo.")
else:
    print("Esses segmentos podem formar um triângulo!")
