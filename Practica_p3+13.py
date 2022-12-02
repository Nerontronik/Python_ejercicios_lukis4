#Diccionarios en pythom.
nombres = {1: "marco", 2: "juan", 3:"lola", 4: True, 5: False, 6: "juan"}
tupla = {"nombre": "marco", "edad": 25, "tup": ("marco", 2, 4, "gorge")}
lista = {"nombre": "marco", "edad": 25, "list": ["marco", 2, 4, "gorge"]}

print(len(nombres))
print(len(tupla))
print(len(lista))
print("-")

#Acceder a elementos keys(), values(), items().
print(nombres[2])
print("-")

x = nombres[2]
print(x)
print("---")

print(nombres.keys())
print(nombres.values())
print(nombres.items())
print("-")

#Cambiar elementos update().
nombres[3] = "carla"
print(nombres)
print("-")

#nombres.update({3: "carla"})
print(nombres)
print("-")

#Agregar elemento.
nombres.update({7: "carla"})
print(nombres)
print("-")

#Elimninar elemento pop(), popitem(), del, clear()
nombres.pop(3)
print(nombres)
print("-")

nombres.popitem()
print(nombres)
print("-")

nombres.clear()
print(nombres)
print("-")

del nombres[2]
print(nombres)
print("-")