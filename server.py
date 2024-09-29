import random as aleatorio #importamos la libreria random

n1 = aleatorio.randint(0, 12) #generamos un numero aleatorio
n2 = aleatorio.randint(0, 12) #generamos un numero aleatorio

print(f"{n1} + {n2}=?") #imprimimos la suma

n3 = int(input(""))  #ingresamos la suma

if n1 + n2 == n3: #comparamos la suma   
    print("suma correcta") #imprimimos el resultado
else:
    print("suma incorrecta") #imprimimos el resultado


    
