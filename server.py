import random as aleatorio

n1 = aleatorio.randint(0, 12)
n2 = aleatorio.randint(0, 12)

print(f"{n1} + {n2}=?")

n3 = int(input(""))

if n1 + n2 == n3:
    print("suma correcta")
else:
    print("suma incorrecta")

    