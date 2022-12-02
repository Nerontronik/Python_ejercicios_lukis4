# Uso del WHILE en PYTHON
# Repeticion de numeros 
numero = 0
while numero <= 10:
    print(numero)
    print("-")
    numero += 1

# Repeticion de numeros con BREAK
while numero <= 10:
    print(numero)
    print("--")
    if numero == 6:
        break
    numero += 1
    
# Repeticion de numero con CONTINUE
while numero <= 10:
    numero += 1
    if numero == 6:
        continue
    print(numero)
    print("---")

# Suma de numeros naturales 
numeros = int(input("introduce un numero natural:"))
resul = 0
contro = 1

while contro <= numeros:
    resul += contro
    contro += 1
print("La suma de numeros naturales es:", resul)
print("-")