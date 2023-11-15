# Adivinar el numero
import random

def adivinaNumero(num,real):
    if(num > real):
        print("El numero es menor")
        return False
    elif(num < real):
        print(" El numero es mayor")
        return False
    else:
        print("Has ganado")
        return True
def main():
    numero = random.randint(0,10)

    ad = int(input("Introduce el numero"))
    while(not adivinaNumero(ad,numero)):
        ad = int(input("Introduce el numero"))

if __name__ == "__main__":
    main()