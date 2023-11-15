# Programa que invierte un string en Python

def girar_string(texto):
    return (texto[::-1])

def main():
    frase = (input("Que frase quieres girar"))
    print(girar_string(frase))

if __name__ == "__main__":
    main()