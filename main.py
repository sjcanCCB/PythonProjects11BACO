
#Declarando una Lista
listaDeEjemplo=["Sandia","Limon","Pera","Licha",1,3,123,321,True,False,"12ABC"]
#Imprimiendo tipo de dato
print(type(listaDeEjemplo))

#Imprimiendo lista
print(listaDeEjemplo)
print("")
#ejemplo acceder a item con indice
print(listaDeEjemplo[3])
#Acceso a item con indice negativo
print(listaDeEjemplo[-1])
#Modificando un valor en un indice específico
listaDeEjemplo[2]="Mango"

print("")
print(listaDeEjemplo)
print("")
print("")
#Agregar un elemento al final de la lista
listaDeEjemplo.append("Steban")
print(listaDeEjemplo)
#Agregar un elemento en la lista según Indice
listaDeEjemplo.insert(1,"Mia")
print(listaDeEjemplo)

listaDeEjemplo[1]="Juan Diego"
print(listaDeEjemplo)
#Ejemplos de remover valor específico de la lista
listaDeEjemplo.remove(123)
listaDeEjemplo.remove("12ABC")
#Ejemplo de remover valor según indice especifico
listaDeEjemplo.pop(8)

print("")
print(listaDeEjemplo)