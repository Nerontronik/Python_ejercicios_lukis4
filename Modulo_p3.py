#Modulo 1:

def suma(x, y):
    print(x + y)

#Modulo 2:

def factor(numero):
    if numero == 1:
        return 1
    else:
        return (numero * factor(numero-1))



#Modulo 3:

def numeroposi(x):
    if x > 0:
        print("tu numero es positivo")
    elif x < 0:
        print("el numero es negativo")
    elif x == 0:
        print("tu numero es cero") 

#Modulo 4:

def ciclo(x):
    while x <= 10:
        print(x)
        x += 1