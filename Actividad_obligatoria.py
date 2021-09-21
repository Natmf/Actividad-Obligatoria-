import random

Min=100
Max=200
Lecturas=10
objetivo=150


sumatoria=0
promedio=0

listaTemp=[]
TempFueraDeRango = []
TempRango=[]

for ciclo in range (Lecturas):
    lectura = random.randint (Min, Max)


    listaTemp.append(lectura)

    if (lectura > objetivo):
        TempFueraDeRango.append(lectura)

    if (lectura < objetivo):
        TempRango.append(lectura) 
          

print(listaTemp)
print()


print(len(TempRango))
TempRango.sort()
print(TempRango)
print()

print(TempFueraDeRango)
print(len(TempFueraDeRango))

for item in TempRango:
    sumatoria = sumatoria + item
    promedio = sumatoria / len (TempRango)
print ("Horno Estable", promedio)


if (promedio < objetivo):
    print ("Temperatura baja, se enciende el quemador", promedio)

if (promedio > objetivo):
    print ("Temperatura alta, se apaga el quemador")

    
while (objetivo == 0):
    print ("fin de lecturas")
    break