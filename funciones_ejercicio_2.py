
def registrar_talleres(talleres):
    print("[REGISTRAR TALLER]")
    while True:
        try:
            cod_taller = int(input("Ingrese el código del taller: "))
            flag = False
            for taller in talleres:
                if cod_taller == taller["codigo"]:
                    flag = True
                    break
            if flag == True:
                print("El código ingresado ya existe. Intente nuevamente.")
            else:
                break
        except ValueError:
            print("Valor ingresado es inválido. Intente nuevamente.")
    
        
    while True:
        nom_taller = input("Ingrese el nombre del taller: ").strip()
        docente = input("Ingrese el nombre del docente responsable del taller: ").strip()
        if len(nom_taller) == 0 or len(docente) == 0:
            print("El nombre o docente no puede estar vacío. Intente nuevamente.")
        else:
            nom_taller = nom_taller.lower().title()
            docente = docente.lower().title()
            break

    while True:
        try:
            cupos = int(input("Ingrese el número de cupos máximos: "))
            if cupos > 0:
                break
            elif cupos <= 0:
                print("Los cupos no pueden ser menor o igual a 0.")
        except ValueError:
            print("Valor ingresado no es correcto. Intente nuevamente.")
    
    talleres_dicc = {"codigo": cod_taller,
                     "nombre": nom_taller,
                     "docente": docente,
                     "cupos": cupos}
    
    talleres.append(talleres_dicc)
    print("Taller registrado correctamente.")

def listar_talleres(talleres):
    print("[LISTA DE TALLERES]")
    if len(talleres) == 0:
        print("No hay ningún taller registrado.")
        return
    
    for taller in talleres:
        print(f"CÓDIGO: {taller["codigo"]}")
        print(f"NOMBRE DEL TALLER: {taller["nombre"]}")
        print(f"DOCENTE RESPONSALBE: {taller["docente"]}")
        print(f"CUPOS MÁXIMOS: {taller["cupos"]}")
        print("=========================================")

def buscar_taller(talleres):
    print("[BUSCADOR DE TALLERES REGISTRADOS]")
    try:
        cod = int(input("Ingrese el código del taller a buscar: "))
    except ValueError:
        print("El valor ingresado no es válido. Intente nuevamente.")
        return
    
    for taller in talleres:
        if cod == taller["codigo"]:
            print("Taller encontrado.")
            print(f"CÓDIGO: {taller["codigo"]}")
            print(f"NOMBRE DEL TALLER: {taller["nombre"]}")
            print(f"DOCENTE RESPONSALBE: {taller["docente"]}")
            print(f"CUPOS MÁXIMOS: {taller["cupos"]}")
            print("=========================================")
            return
    
    print("No se ha encontrado ningún taller con ese código.")
        
def actualizar_taller(talleres):
    print("[ACTUALIZAR TALLER]")
    while True:
        try:
            cod = int(input("Ingresa el código del taller a actualizar: "))
            break
        except ValueError:
            print("El valor ingresado es inválido. Intente nuevamente.")
            return
    
    for taller in talleres:
        if cod == taller["codigo"]:
            print("Taller encontrado.")
            while True:
                nom_nuevo = input("Ingrese el nuevo nombre para el taller: ").strip()
                docente_nuevo = input("Ingrese el nuevo docente responsable: ").strip()
                if len(nom_nuevo) == 0 or len(docente_nuevo) == 0:
                    print("El nombre o docente responsable, no puede estar vacío. Intente nuevamente.")
                else:
                    break

            while True:
                try:
                    cupos_nuevos = int(input("Ingrese los nuevos cupos máximos: "))
                    if cupos_nuevos > 0:
                        break
                    elif cupos_nuevos <= 0:
                        print("Los cupos no pueden ser menor o igual a 0.")
                except ValueError:
                    print("El valor ingresado es inválido. Intente nuevamente.")
            
            taller["nombre"] = nom_nuevo.lower().title()
            taller["docente"] = docente_nuevo.lower().title()
            taller["cupos"] = cupos_nuevos
            print("Taller actualizado correctamente.")
            return
        
    print("No se ha encontrado ningún taller con ese código asociado.")

def eliminar_taller(talleres):
    print("[ELIMINAR TALLER]")
    try:
        cod = int(input("Ingresa el código del taller a eliminar: "))
    except ValueError:
        print("El valor ingresado no es válido. Intente nuevamente.")
    
    for taller in talleres:
        if cod == taller["codigo"]:
            print("Taller encontrado.")
            print(f"CÓDIGO: {taller["codigo"]}")
            print(f"NOMBRE DEL TALLER: {taller["nombre"]}")
            print(f"DOCENTE RESPONSALBE: {taller["docente"]}")
            print(f"CUPOS MÁXIMOS: {taller["cupos"]}")
            print("=========================================")

            op = input("¿Quieres elimanar el taller?(s/n): ").lower()
            if op == "s":
                talleres.remove(taller)
                print("Taller eliminado satisfactoriamente.")
                return
            elif op == "n":
                print("Operación cancelada.")
                return
            else:
                print("Debe ingresar un (s) para sí o (n) para no. Intente nuevamente.")

    print("No se ha encontrado ningún taller con el código ingresado.")