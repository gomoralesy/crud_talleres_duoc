from crud_talleres_duoc.funciones_ejercicio_2 import (registrar_talleres,
                                   listar_talleres,
                                   buscar_taller,
                                   actualizar_taller,
                                   eliminar_taller)
print("=====SISTEMA CRUD DE TALLERES ACADÉMICOS=====")
talleres = []

while True:
    print("1. Registrar talleres\n" \
    "2. Listar talleres registrados\n" \
    "3. Buscar taller registrado\n" \
    "4. Actualizar taller\n" \
    "5. Eliminar taller\n" \
    "6. Salir")
    
    op = input("Ingresa la opción a realizar: ")

    if op == "1":
        registrar_talleres(talleres)
    elif op == "2":
        listar_talleres(talleres)
    elif op == "3":
        buscar_taller(talleres)
    elif op == "4":
        actualizar_taller(talleres)
    elif op == "5":
        eliminar_taller(talleres)
    elif op == "6":
        break
    else:
        print("Escoja una opción dentro del rango 1 - 6.")

print("Gracias por usar nuestro sistema.")