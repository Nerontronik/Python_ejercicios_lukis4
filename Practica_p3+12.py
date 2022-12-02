#Listas en python
nombres = ["marco", "juan", "caro", "roberto", "rosa"]
numeros = [1, 2, 3, 4, 5,]
barios = [1, 5, 4, "mari", "juan", True, False, False ]

print(barios)
print("-")
print(len(barios))
print("-")

#Acceder a elementos de una lista
print(nombres[0:3])
print("-")

#Cambiar elementos de una lista
barios[5] = False
print(barios)
print("-")

#Metodos de las listas append(), remove()
barios.append(True)
print(barios)
print("-")

barios.remove(4)
print(barios)
print("-")