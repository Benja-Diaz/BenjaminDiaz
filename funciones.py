def cargar_productos(): #funcion usada para ordenar los productos en el txt
    productos = []
    try:
        with open('productos.txt','r') as file:
            for element in file:
                nombre_producto, categoria, precio = line.strip().split(',')
                precio = int(precio)
                productos.append((nombre_producto, categoria, precio))
    except FileNotFoundError:
        productos = []
    return productos

def guardar_productos(productos): #funcion para guardar los productos en el archivo de texto
    with open('peliculas.txt','w') as file:
        for producto in productos:
            file.write(f"{producto[0]},{producto[1]},{producto[2]}\n")

def agregar_productos(): #funcion usada para agregar productos
    nombre_producto = input("ingrese el nombre del producto: ")
    categoria = input("ingrese la categoria del producto: ")
    while True:
        try:
            precio = int(input("ingrese el precio del producto"))
            break
        except ValueError:
            print("Error! por favor ingrese el precio con números")

    producto = (nombre_producto, categoria, precio)
    productos = cargar_productos()
    productos.append(producto)
    guardar_productos(productos)
    return "producto ingresado correctamente. "

def listar_productos():
    productos = cargar_productos()
    if not productos:
        return "no hay productos registrados. "

    lista_productos = []
    for producto in productos:
        lista_productos.append(f"nombre: {producto[0]}, categoria: {producto[1]}, precio: {producto[2]}")
    return lista_productos

def buscar_por_categoria(categoria_buscar):
    productos = cargar_productos()
    productos_encontrados = [producto for producto in productos if producto[1].lower() == categoria_buscar.lower()]
    if not productos_encontrados:
        return (f"no se encontraron productos para esa categoria. ")
    
    lista_productos_encontrados = []
    for producto in productos_encontrados:
        lista_productos_encontrados.append(f"nombre: {producto[0]}, precio: {producto[2]}")
    return lista_productos_encontrados

def precio_promedio():
    productos = cargar_productos
    promedio = sum(producto[2] for producto in productos)/productos
    return promedio

while True:
    print("1. Ingrese el producto: ")
    print("2. lista de todos los productos: ")
    print("3. productos por categoria: ")
    print("4. Calcular el precio promedio de los productos. ")
    print("5. salir. ")
   
    opcion = input("ingrese una opcion: ")

    if opcion == "1":
        mensaje = agregar_productos()
        print(mensaje)
    elif opcion == "2":
        resultado = listar_productos()
        if isinstance(resultado, list):
            for producto in resultado:
                print(producto)
            

 except ValueError:
   print("Error! ingrese un número del 1 al 5")












