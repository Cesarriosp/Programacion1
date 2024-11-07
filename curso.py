import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",  
        user="root",
        password="curso",
        database="supermercado"
    )

def crear_categoria():
    conexion = conectar()
    cursor = conexion.cursor()
    idcategoria = int(input("Ingrese el ID de la nueva categoría: "))
    nombre = str(input("Ingrese el nombre de la nueva categoría: "))
    
    cursor.execute("INSERT INTO categoria (idcategoria, nombre) VALUES (%s, %s)", (idcategoria, nombre))
    conexion.commit()
    cursor.close()
    conexion.close()

def leer_categorias():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM categoria")
    categorias = cursor.fetchall()
    if categorias:
        print("Listado de Categorías:")
        for categoria in categorias:
            print(f"{categoria[0]} - {categoria[1]}")
    else:
        print("No hay categorías disponibles.")
    cursor.close()
    conexion.close()

def actualizar_categoria():
    conexion = conectar()
    cursor = conexion.cursor()

    idcategoria = input("Ingrese el ID de la categoría a actualizar: ")
    nuevo_nombre = input("Ingrese el nuevo nombre de la categoría: ")
    
    cursor.execute("UPDATE categoria SET nombre = %s WHERE idcategoria = %s", (nuevo_nombre, idcategoria))
    if cursor.rowcount > 0:
        conexion.commit()
        print(f"[Confirmación] La categoría con ID {idcategoria} ha sido actualizada a '{nuevo_nombre}'.")
    else:
        print(f"No se encontró una categoría con ID {idcategoria}.")

    cursor.close()
    conexion.close()

def eliminar_categoria():
    conexion = conectar()
    cursor = conexion.cursor()

    idcategoria = input("Ingrese el ID de la categoría a eliminar: ")
    
    cursor.execute("DELETE FROM categoria WHERE idcategoria = %s", (idcategoria,))
    if cursor.rowcount > 0:
        conexion.commit()
        print(f"La categoría con ID {idcategoria} ha sido eliminada.")
    else:
        print(f"No se encontró una categoría con ID {idcategoria}.")

    cursor.close()
    conexion.close()

def mostrar_menu():
    while True:
        print("\n=== Gestión de Categorías ===")
        print("Seleccione una opción:")
        print("1. Crear nueva categoría")
        print("2. Leer categorías existentes")
        print("3. Actualizar una categoría")
        print("4. Eliminar una categoría")
        print("5. Salir")
        
        opcion = input("Opción: ")
        
        if opcion == "1":
            crear_categoria()
        elif opcion == "2":
            leer_categorias()
        elif opcion == "3":
            actualizar_categoria()
        elif opcion == "4":
            eliminar_categoria()
        elif opcion == "5":
            print("Saliendo de la gestión de categorías. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


mostrar_menu()