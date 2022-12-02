#Cadenas en Python.

nombre = "marco {}"
edad = 34
nombres = """Marco
luis 
rosa 
carlos
"""

#Trabajar con una cadena.
for x in nombre:
    print(x)
    print("-")
print("--")
print(len(nombre))
print("--")
print(nombre * 3)
print("---")

#Cortar cadenas.
print("-")
print(nombre[0:2])
print("-")

#Cadenas y sus metodos: upper(), lower(), replace(), format()
print(nombre.upper())
print("--")
print(nombre.lower())
print("---")
print(nombre.replace("C", "p"))
print("----")
print(nombre.format(edad))
print("-----")