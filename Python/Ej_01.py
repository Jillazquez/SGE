# Programa que calcula si un numero es primo o no

def esPrimo(numero):
    if numero < 2:
        return False;
    for i in range(2, int((numero/2)+1)):
        if( numero % i == 0 ):
            return False;
    return True;
def main():
    num = int(input("Ingresa el numero que quieres saber si es primo"))
    if(esPrimo(num)):
        print("WOW es primo")
    else:
        print("WOW no es primo")

if __name__ == "__main__":
    main()