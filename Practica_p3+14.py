#Funciones en python
def mifuncion():
    print("hola mundo")
    print("-")

mifuncion()
def suma(x, y):
    print(x + y)
    print("-")

numero1 = int(input("introduce un numero:"))
numero2 = int(input("introduce otro numero:"))
suma(numero1, numero2)

#Recursividad
def factor(numero):
    if numero == 1:
        return 1
    else:
        return (numero * factor(numero-1))

factor2 = int(input("dame un numero para calcular su factorial:"))

print("Este es el resultado", factor(factor2))
print("-")

#Uso de if
def numeroposi(x):
    if x > 0:
        print("tu numero es positivo")
        print("-")
    elif x < 0:
        print("el numero es negativo")
        print("-")
    elif x == 0:
        print("tu numero es cero") 
        print("-")
print("-")

numero = int(input("introduce un numero negativo o positivo:"))
numeroposi(numero)

#Uso de While
def ciclo(x):
    while x <= 10:
        print(x)
        print("-")
        x += 1
numero = 0
ciclo(numero)