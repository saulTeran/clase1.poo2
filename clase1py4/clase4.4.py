def detMayor(arreglo):
    mayor=0
    for i in range(len(arreglo)):
        if arreglo[i]>mayor:
            mayor=arreglo[i]
    return mayor

def imprimirFor(arreglo):
    for value in arreglo:
        print(value)

def imprimiForI(arreglo):
    for i in range(len(arreglo)):
        print(arreglo[i])

def mostrar(arreglo):
    i=0
    while i<len(arreglo):
        print(arreglo[i])
        i=i+1

def cargar(arreglo):
    for i in range(len(arreglo)):
        print(f"ingresa el valor a guardar en la posicion {i+1}")
        dato=int(input())
        arreglo[i]=dato

#cuerpo principal
nombres=[""]*5
estados=["", "", "", "", ""]
precios=[0]*7
cargar(precios, "ingresa el precio")
mostrar(precios)
imprimiForI(estados)
#precioMayor
precioMayor=detMayor(precios)
print(f"el precio mayor es {precioMayor}")