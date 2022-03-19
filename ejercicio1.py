numeros = []
cantidadNumeros = int(
    input("Ingrese la cantidad de numeros que va a digitar: "))

for i in range(cantidadNumeros):
    numero = int(input("Ingrese un número entero: "))
    numeros.append(numero)

pares = 0
impares = 0

for num in numeros:
    if (num % 2 == 0 and num % 3 == 0):
        pares += 1
        impares += 1
    elif (num % 2 == 0):
        pares += 1
    elif (num % 3 == 0):
        impares += 1

print(f"La cantidad de múltiplos de 2 es {pares}")
print(f"La cantidad de múltiplos 3 es {impares}")
