# Contador de palabras en Python

def contador(texto):
    palabras = 1
    for i in texto:
        if( i == ' '):
            palabras += 1
    return palabras

ejemplo = input("Introduce la frase ")
total = contador(ejemplo)
print(total)