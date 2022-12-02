#Como usar las tuplas.
nombres = ("carlos", "marco", "luz", "luis")
numeros = (1, 2, 2, 2, 5,)
valor = (True, False, True)
comvinada = ( "marco", 2, 4, True, False) 

print(len(nombres))
print("-")
#Acceder a elementos de una tupla.
print(nombres[-1])
print("-")

#Actualizar una tupla.
x = list(comvinada)
x[3] = "oscar"
comvinada = tuple(x)
print(comvinada[3])
print("--")

#Desempaquetar una tuplas.
(uno, dos, tres, cuatro, cinco) = numeros
print(uno)
print(dos)
print(tres)
print(cuatro)
print(cinco)
print("---")

#Metodos de una tupla count(), index().
print(numeros.count(2))
print(numeros.index(5))
print("----")