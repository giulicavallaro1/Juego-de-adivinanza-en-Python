import random

numero_secreto = random.randrange (1,101)
adivinado=False
cantidad_max_intentos= 5
cantidad_intentos= 0

print("Bienvenido al juego de adivinar el numero secreto:")

while not adivinado and cantidad_intentos < cantidad_max_intentos:
    Entrada= input("introducir un numero del 1 al 100: ")  
    numero= int(Entrada)

    if numero ==numero_secreto:
        print("Felicitaciones , adivinaste el numero secreto")

        adivinado=True

    elif numero < numero_secreto:
        print("El numero es mayor al ingresado")

    else:
        print ("El numero es menor al ingresado")

    cantidad_intentos +=1

if not cantidad_intentos < cantidad_max_intentos:
    print ("¡Game over! No has podido superar el juego")
