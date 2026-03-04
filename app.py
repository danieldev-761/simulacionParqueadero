matriculas= ["QWE345","JKS432","FDF442","FDF453","IUY345"]


espacio_total= 10
nivel_de_llenado= 5
vehiculo_encontrado= False

tiene_minus= False
digito= False


i=nivel_de_llenado

for i in range(espacio_total):


    while i <= nivel_de_llenado:
        print("""
        ---------------- MENÚ PARQUEADERO ----------------
        1. Ingresar vehículo
        2. Retirar vehículo
        3. Ver estado del parqueadero
        4. Salir
        
        """)

        opcion= int(input("Ingrese una opción del menú anterior: "))

        match opcion:

            case 1:
                if nivel_de_llenado < espacio_total:
                    matricula= input("Ingrese la matrícula del vehículo: ")

                    for char in range(len(matricula)):
                        if matricula[char].islower():
                            tiene_minus= True
                            
                            
                        if matricula[char].isdigit():
                            digito= True

                    if tiene_minus == True:
                        print("La matrícula no puede contener letras minúsculas. Regresando al menú anterior.")
                        continue

                    elif digito == False:
                        print("La matrícula debe contener al menos un dígito. Regresando al menú anterior.")
                        continue

                   
                        
                    nivel_de_llenado+=1
                    matriculas.append(matricula)
                    print(f"Vehículo con placa {matricula} agregado exitosamente.")


            case 2: 
                if nivel_de_llenado <= espacio_total:
                    matricula= input("Ingrese la matrícula del vehículo: ")

                    for i in range(len(matriculas)):
                        if matricula == matriculas[i]:
                            vehiculo_encontrado= True
                            print("Vehiculo encontrado")
                         
                    if vehiculo_encontrado:
                        nivel_de_llenado-=1
                        matriculas.remove(matricula)
                        print(f"Vehículo con placa {matricula} eliminado exitosamente.")

                    else:
                        print("NO se ha podido encontrar el vehiculo. Regresando al menú anterior")

                    


            case 3:
                print(f"Estado del parqueadero: {nivel_de_llenado} de {espacio_total} espacios ocupados.")
                print(f"Vehículos en parqueadero: {matriculas}")

            case 4:

                print("Saliendo...")
                exit()

            case _:
                print("Opción no válida. Por favor, ingrese una opción del menú.")

    print("Parqueadero lleno. No se puede agregar más vehículos.")


    
