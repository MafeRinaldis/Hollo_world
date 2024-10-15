def generar_factura():
    print("Bienvenido al generador de facturas")

    # Datos del cliente
    nombre_cliente = input("Nombre del cliente: ")
    fecha = input("Fecha (DD/MM/AAAA): ")

    # Productos
    productos = []
    while True:
        producto = input("Producto (o 'salir' para terminar): ")
        if producto.lower() == 'salir':
            break
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))
        total_producto = precio * cantidad
        productos.append((producto, precio, cantidad, total_producto))

    # Total de la factura
    total_factura = sum(item[3] for item in productos)

    # Mostrar factura
    print("\n--- FACTURA ---")
    print(f"Cliente: {nombre_cliente} | Fecha: {fecha}")
    for producto, precio, cantidad, total in productos:
        print(f"{producto}: {cantidad} x {precio:.2f} = {total:.2f}")
    print(f"Total: {total_factura:.2f}")

if __name__ == "__main__":
    generar_factura()