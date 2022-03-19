print("Supermercado El Cacheton")
print("****************")
print("1. Digita 1 ingresar un producto nuevo")
print("2. Digita 2 para mostrar todos los productos")
print("3. Digita 3 para buscar un producto y editar su precio")
print("4. Digita 4 para buscar un producto y eliminarlo")
print("0. Digita 0 para salir")

listaProductos = []
#producto = {}
opcion = 1

while (opcion != 0):
    opcion = int(input("Digita una opción "))
    if (opcion == 1):
        producto = {}

        codigo = input("Ingrese el código del producto: ")
        producto['codigo'] = codigo

        nombre = input("Ingrese el nombre del producto: ")
        producto['nombre'] = nombre

        precio = input("Ingrese el precio del producto: ")
        producto['precio'] = precio

        listaProductos.append(producto)

    elif (opcion == 2):
        print(listaProductos)

    elif (opcion == 3):
        codigo = input("Ingrese el código del producto: ")
        for indice, producto in enumerate(listaProductos):
            if (codigo == producto['codigo']):
                nuevoPrecio = int(
                    input("Ingrese el nuevo precio del producto: "))
                producto['precio'] = nuevoPrecio
                break
            else:
                print("El codigo del producto no se encuentra registrado")

    elif (opcion == 4):
        codigo = input("Ingrese el código del producto: ")

        for indice, producto in enumerate(listaProductos):

            if (codigo == producto['codigo']):
                #del listaProductos[listaProductos.index(codigo)]
                listaProductos.pop(indice)
                print("Producto eliminado con éxito")
            else:
                print("El codigo del producto no se encuentra registrado")

    elif (opcion == 0):
        print("Saliendo")
        break
    else:
        print("Opcion no válida, intente nuevamente")
