#Tarea #1 Estructuras de Datos
#José Julián Garbanzo Acuña
#UH
arreglo1=[]
arreglo2=[]


for i in range (5):
    lista1=int(input("Ingrese 5 numeros para añadir al primer arreglo: "))
    arreglo1.append(lista1)
for i in range(5):
    lista2=int(input("Ingrese 5 numeros para añadir al segundo arreglo: "))
    arreglo2.append(lista2)
    
arreglosSumados=arreglo1+arreglo2
arregloOrdenado=sorted(arreglosSumados,reverse=True)
print(arregloOrdenado)
       



