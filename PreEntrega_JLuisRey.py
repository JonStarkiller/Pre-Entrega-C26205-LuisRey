# TalentoTech - PreEntrega
# Comisión 26205
# Autor: J. Luis Rey
# Descripción: Programa de gestión de productos.

# Fecha: 2026-10-01
# Version 1.01


import os

# Color ANSI
COLOR_TITULO = "\033[1;36m"   # Cian en negrita
COLOR_EXITO = "\033[1;32m"    # Verde en negrita
COLOR_ERROR = "\033[1;31m"    # Rojo en negrita
COLOR_RESET = "\033[0m"       # Restablecer color

productos = []

while True:
    # Limpiar la pantalla antes de mostrar el menú
    os.system("cls" if os.name == "nt" else "clear")

    print(f"{COLOR_TITULO}========================================{COLOR_RESET}")
    print(f"{COLOR_TITULO}       Gestion de Productos Rey         {COLOR_RESET}")
    print(f"{COLOR_TITULO}========================================{COLOR_RESET}")
    print("""
    1. Agregar productos
    2. Mostrar productos
    3. Buscar producto
    4. Eliminar producto
    5. Salir
    """)

    opcion = input("Elegir una opción (1-5): ").strip()

    if opcion == "1":
        while True:
            print(f"\n{COLOR_TITULO}--- Agregar producto ---{COLOR_RESET}")

            nombre = input("Nombre del producto: ").strip().title()
            while nombre == "":
                print(f"{COLOR_ERROR}Error: el nombre no puede estar vacío{COLOR_RESET}")
                nombre = input("Nombre del producto: ").strip().title()

            categoria = input("Categoría del producto: ").strip().title()
            while categoria == "":
                print(f"{COLOR_ERROR}Error: la categoría no puede estar vacía{COLOR_RESET}")
                categoria = input("Categoría del producto: ").strip().title()

            precio_str = input("Ingresar el precio del producto (Sin centavos): ").strip()
            while not precio_str.isdigit():
                print(f"{COLOR_ERROR}Error: ingresar un valor de precio válido (No negativo){COLOR_RESET}")
                precio_str = input("Ingresar el precio del producto (Sin centavos): ").strip()
            precio = int(precio_str)

            datos = [nombre, categoria, precio]
            productos.append(datos)
            print(f"{COLOR_EXITO}✓ Producto '{nombre}' agregado con éxito.{COLOR_RESET}")

            continuar = input("\n¿Desea agregar otro producto? (s/n): ").strip().lower()
            while continuar not in ["s", "n"]:
                print(f"{COLOR_ERROR}Error: Debe ingresar 's' para Sí o 'n' para No.{COLOR_RESET}")
                continuar = input("¿Desea agregar otro producto? (s/n): ").strip().lower()
            if continuar == "n":
                break

    elif opcion == "2":
        print(f"\n{COLOR_TITULO}--- Lista de productos ---{COLOR_RESET}")

        if len(productos) == 0:
            print(f"{COLOR_ERROR}No hay productos cargados{COLOR_RESET}")
        else:
            for i in range(len(productos)):
                print(f"{COLOR_EXITO}ID:{i+1}{COLOR_RESET}\n- Nombre: {productos[i][0]}\n- Categoría: {productos[i][1]}\n- Precio: ${productos[i][2]}\n")

        input("\nPresionar Enter para continuar...")

    elif opcion == "3":
        print(f"\n{COLOR_TITULO}--- Buscar productos ---{COLOR_RESET}")

        if len(productos) == 0:
            print(f"{COLOR_ERROR}No hay productos cargados{COLOR_RESET}")
        else:
            busqueda = input("Ingresar el nombre del producto a buscar: ").strip().lower()

            while busqueda == "":
                print(f"{COLOR_ERROR}Error: El ingreso no puede estar vacío{COLOR_RESET}")
                busqueda = input("Ingresar el nombre del producto a buscar: ").strip().lower()

            encontrado = 0
            for i in range(len(productos)):
                if busqueda in productos[i][0].lower():
                    print(f"\n{COLOR_EXITO}ID:{i+1}{COLOR_RESET}\n- Nombre: {productos[i][0]}\n- Categoría: {productos[i][1]}\n- Precio: ${productos[i][2]}")
                    encontrado += 1

            if encontrado == 0:
                print(f"{COLOR_ERROR}No se encontró ningún resultado{COLOR_RESET}")
            else:
                print(f"\n{COLOR_EXITO}Productos encontrados: {encontrado}{COLOR_RESET}")

        input("\nPresionar Enter para continuar...")

    elif opcion == "4":
        print(f"\n{COLOR_TITULO}--- Eliminar producto ---{COLOR_RESET}")
        if len(productos) == 0:
            print(f"{COLOR_ERROR}No hay productos cargados{COLOR_RESET}")
        else:
            for i in range(len(productos)):
                print(f"{COLOR_EXITO}{i+1}.{COLOR_RESET} {productos[i][0]} - {productos[i][1]} - ${productos[i][2]}")

            print(f"\n{COLOR_TITULO}(Ingresar 0 para cancelar y volver al menú){COLOR_RESET}\n")
            id_eliminar = input("Número de producto a eliminar: ").strip()

            # Validar que sea un número y esté dentro del rango (o sea 0 para cancelar)
            while not id_eliminar.isdigit() or int(id_eliminar) < 0 or int(id_eliminar) > len(productos):
                print(f"{COLOR_ERROR}Error: Ingresar un número válido (1 a {len(productos)}) o 0 para cancelar{COLOR_RESET}")
                id_eliminar = input("Número de producto a eliminar: ").strip()

            opcion_eliminar = int(id_eliminar)

            if opcion_eliminar == 0:
                print(f"\n{COLOR_EXITO}Operación cancelada. No se eliminó ningún producto.{COLOR_RESET}")
            else:
                posicion = opcion_eliminar - 1
                eliminado = productos.pop(posicion)
                print(f"{COLOR_EXITO}✓ Se eliminó el producto: {eliminado[0]}{COLOR_RESET}")

        input("\nPresionar Enter para continuar...")

    elif opcion == "5":
        print(f"\n{COLOR_EXITO}¡Gracias por usar nuestro sistema!{COLOR_RESET}\n")
        break

    else:
        print(f"{COLOR_ERROR}Opción inválida. Ingrese una opción entre 1 y 5.{COLOR_RESET}")
        input("\nPresione Enter para continuar...")