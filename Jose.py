# Productos disponibles en la tienda
productos_disponibles = {
    "Coca Cola": 8.00,
    "Pepsi": 6.00,
    "Pan Bimbo": 18.00,
    "Tortrix": 2.00,
    "Dorito": 2.00,
    "Agua Pura": 2.50,
    "Jamon": 15.00,
    "Azucar": 5.00,
    "Chetos": 3.75,
    "Recarga": 50.00,
    "Raptor": 8.00,
}

# Carrito de compras
carrito = []

# Función para mostrar el menú de productos disponibles
def mostrar_menu():
    print("Productos disponibles:")
    for producto, precio in productos_disponibles.items():
        print(f"{producto}: Q{precio}")

# Función para agregar productos al carrito
def agregar_carrito():
    while True:
        producto = input("Ingresa el producto que deseas agregar al carrito (o 'salir' para terminar): ").capitalize()
        if producto == "Salir":
            break
        elif producto in productos_disponibles:
            cantidad = int(input(f"¿Cuántas unidades de {producto} deseas agregar?: "))
            carrito.append((producto, productos_disponibles[producto], cantidad))
            print(f"{cantidad} unidades de {producto} agregadas al carrito.")
        else:
            print("Producto no disponible.")

# Función para calcular el total de la compra
def calcular_total():
    total = 0
    for producto, precio, cantidad in carrito:
        total += precio * cantidad
    return total

# Función para aplicar descuentos
def aplicar_descuento(total):
    descuento = 0
    if total > 20:
        descuento = total * 0.10
        total -= descuento
    return total, descuento

# Función para finalizar la compra y generar reporte
def finalizar_compra(nombre_cliente):
    print("\n--- Resumen de tu compra ---")
    for producto, precio, cantidad in carrito:
        print(f"{producto} - {cantidad} unidades - Q{precio * cantidad}")
    
    total = calcular_total()
    total_con_descuento, descuento_aplicado = aplicar_descuento(total)
    
    if descuento_aplicado > 0:
        print(f"Descuento aplicado: Q{descuento_aplicado:.2f}")
    
    print(f"Total a pagar: Q{total_con_descuento:.2f}")
    print(f"Gracias por tu compra, {nombre_cliente}!")

    # Generar reporte en un archivo .txt
    with open("reporte_compra.txt", "w") as reporte:
        reporte.write(f"Cliente: {nombre_cliente}\n")
        reporte.write("--- Resumen de la compra ---\n")
        for producto, precio, cantidad in carrito:
            reporte.write(f"{producto} - {cantidad} unidades - Q{precio * cantidad}\n")
        if descuento_aplicado > 0:
            reporte.write(f"Descuento aplicado: Q{descuento_aplicado:.2f}\n")
        reporte.write(f"Total a pagar: Q{total_con_descuento:.2f}\n")

# Función principal del programa
def iniciar_tienda():
    nombre_cliente = input("Bienvenido, ¿cuál es tu nombre?: ")
    while True:
        print("\n--- Menú de la tienda ---")
        mostrar_menu()
        agregar_carrito()
        finalizar = input("¿Deseas finalizar la compra? (s/n): ").lower()
        if finalizar == 's':
            finalizar_compra(nombre_cliente)
            break
        else:
            print("Puedes seguir agregando productos al carrito.")

if __name__ == "__main__":
    iniciar_tienda()
    
    