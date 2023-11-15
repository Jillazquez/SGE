# Contador de palabras en Python

def contador(texto):
    palabras = 1
    for i in texto:
        if( i == ' '):
            palabras += 1
    return palabras
def main():
    ejemplo = input("Introduce la frase ")
    total = contador(ejemplo)
    print(total)

if __name__ == "__main__":
    main()