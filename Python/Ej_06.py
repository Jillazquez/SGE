lista = [5,2,3,5,6,237,45,6,57,1,6,4,4,345,76,346,252,3234,12,52]

print(lista)
cambio = True
while(cambio):
    cambio = False
    for i in range (len(lista)-1):
        if lista[i] > lista[i+1]:
            aux = lista[i]
            lista[i] = lista[i+1]
            lista[i+1] = aux
            cambio = True

print(lista)