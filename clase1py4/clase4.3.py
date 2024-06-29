mesesAno=["enero","febrero", "marzo", "abril","mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
while True:
    posi=int(input("ingres el mes del ano: "))
    if posi>=0 and posi<=len(mesesAno):
        print(mesesAno[posi-1])
    else:
        print(f"indice fuera de rango, el tamano es {len(mesesAno)}")

    resp=input("escriba espacio para detener")
    if resp==" ":
        break