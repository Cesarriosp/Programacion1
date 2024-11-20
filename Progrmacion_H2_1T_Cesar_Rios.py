import pandas as pd
import mysql.connector                          #usuario: 'root'  y   #contraseña: 'curso'
                                                
#Mediante esta funcion accederemos a la base de datos
def conectar_basedatos():
    return mysql.connector.connect(host='localhost', user='root', password='curso', database='HITOPROG2')


#Esta funcion mostrara los productos, clientes, pedidos
def registrar_usuario():
    try:
        conexion_bd = conectar_basedatos()
        cursor_bd = conexion_bd.cursor()
        nombre_usuario = str(input('Por favor, ingrese su nombre completo: ')).title()
        direccion_usuario = input('Por favor, ingrese su dirección: ')
        telefono_usuario = int(input('Por favor, ingrese su número de teléfono: '))
#Solicitamos los datos del usuario
        cursor_bd.execute('INSERT INTO cliente (nombre,direccion,tlf) VALUES (%s,%s,%s)', (nombre_usuario, direccion_usuario, telefono_usuario))
#Usamos el execute para insertar los datos en la base de datos
        conexion_bd.commit()
#Hacemos commit para que se guarden los cambios en la base de datos
        id_usuario = cursor_bd.lastrowid
#Recogemos el ID del usuario automáticamente con lastrowid
        print(f'Bienvenido {nombre_usuario}, su ID de usuario es {id_usuario}')
    except:
        print('Hubo un error durante el registro.')
    finally:
        conexion_bd.close()
        cursor_bd.close()

#Si existe el usuario, iniciamos sesión
def iniciar_sesion_usuario():    
    try: 
        conexion_bd = conectar_basedatos()
        cursor_bd = conexion_bd.cursor()
        id_usuario = int(input('Introduce tu ID de usuario: '))
        cursor_bd.execute("SELECT * FROM cliente WHERE idcliente = %s", (id_usuario,))
        resultados = cursor_bd.fetchall()
#Gracias a fetchall, obtenemos los resultados e imprimimos el nombre del usuario
        if resultados:
            for usuario in resultados:
                print(f"Bienvenido/a {usuario[1]}")
#Usuario[1] es el nombre del cliente
            cursor_bd.close()
            conexion_bd.close()
        else:
            print("No se ha encontrado ese ID de usuario.") 
    finally:
        cursor_bd.close()
        conexion_bd.close()

def realizar_pedido():
    respuesta_cliente = int(input('¿Eres cliente? Presiona 1.- Para registrarte o 2.- Para ingresar tu ID de usuario: '))
    
    if respuesta_cliente == 1:
        registrar_usuario()  
    elif respuesta_cliente == 2:
        iniciar_sesion_usuario()  
#Comprobamos que el usuario sea válido
    
    try:
        conexion_bd = conectar_basedatos()
        cursor_bd = conexion_bd.cursor()

#Pedimos el ID del usuario para asociar el pedido a su ID
        id_usuario = int(input("Introduce tu ID de usuario: "))
        cursor_bd.execute("SELECT * FROM cliente WHERE idcliente = %s", (id_usuario,))
        usuario = cursor_bd.fetchone()
#Con el cursor.fetchone, obtenemos el primer resultado  para comprobar si existe
        
        if not usuario:
            print("Usuario no encontrado.")
#Si no se encuentra, usamos if not y return para que pare el proceso
            return
        
#Creamos el pedido asociando el ID de usuario con el pedido y obtenemos su ID con lastrowid
        cursor_bd.execute("INSERT INTO pedido (idcliente) VALUES (%s)", (id_usuario,))
        id_pedido = cursor_bd.lastrowid

#Mostramos los productos, mediante pandas para mostrar la tabla de productos
        cursor_bd.execute("SELECT * FROM producto")
        productos = cursor_bd.fetchall()

        df_productos = pd.DataFrame(productos, columns=['idproducto', 'nombre', 'medida', 'precio', 'stock'])
        print("\n***** Listado de productos disponibles *****")
        print(df_productos)

#Debemos escribir 0 para que finalice el pedido y se añada a la tabla detalles
        while True:
            id_producto = input("Introduce el ID del producto deseado (o 0 para finalizar): ")
            if id_producto == "0":
                break
            unidades = int(input("Cantidad: "))
            cursor_bd.execute("SELECT precio FROM producto WHERE idproducto = %s", (id_producto,))
            precio = cursor_bd.fetchone()[0] 
            
#Gracias al fetchone, recogemos el precio de los productos adquiridos, y se añade todo a la tabla detalles
            cursor_bd.execute("INSERT INTO detalle (idcliente, idpedido, idproducto, precio, unidades) VALUES (%s, %s, %s, %s, %s)", 
                              (id_usuario, id_pedido, id_producto, precio, unidades))
        
        conexion_bd.commit()
        print(f"Pedido realizado con éxito. ID del pedido: {id_pedido}")
    
    except Exception as e:
        print(f"Error al realizar la compra: {e}")
    finally:
        cursor_bd.close()
        conexion_bd.close()

def seguimiento_de_pedido():
    conexion_bd = conectar_basedatos()
    cursor_bd = conexion_bd.cursor()
    
    try:
#Pedimos el ID del pedido para hacer el seguimiento
        id_pedido = int(input('Introduce el ID del pedido para hacer su seguimiento: '))
        cursor_bd.execute('SELECT * FROM detalle WHERE idpedido = %s', (id_pedido,))
        detalles_pedido = cursor_bd.fetchall()
        
        if detalles_pedido:
            print('* Listado de productos en el pedido *')
#Para mostrar la tabla, primero escribimos dentro de la funcion detalles pedido para que recoja todo y a continuacion las columnas con los nombres que deseamos
            df = pd.DataFrame(detalles_pedido, columns=['idcliente', 'idpedido', 'idproducto', 'precio', 'unidades', 'fecha'])
            
            print(df)
        else:
            print('No se ha encontrado el pedido o no tiene detalles registrados.')
    
    except ValueError:
        print('Introduce un ID válido.')
    
    finally:
        cursor_bd.close()
        conexion_bd.close()


    


def menu_control_usuarios():
    print('\n**Has accedido a la base de datos de usuarios**\n')

    conexion_bd = conectar_basedatos()
    cursor_bd = conexion_bd.cursor()
    cursor_bd.execute('SELECT * FROM cliente')
    usuarios = cursor_bd.fetchall()

#Si existen usuarios en la base de datos, los mostramos en una tabla
    if usuarios:
        print('Listado de usuarios:')
        
        df_usuarios = pd.DataFrame(usuarios, columns=['idcliente', 'nombre', 'direccion', 'tlf'])
        print(df_usuarios)
        
        conexion_bd.close()
        cursor_bd.close()

#Ahora pedimos el ID de un usuario para ver más detalles de sus pedidos
        while True:
            id_usuario_info = int(input('Introduce el ID del usuario para acceder a sus pedidos o "0" para volver al menú principal: '))
            if id_usuario_info == 0:
                print('\nVolviendo al menú principal...')
                return
            
            conexion_bd = conectar_basedatos()
            cursor_bd = conexion_bd.cursor()
            cursor_bd.execute('SELECT idcliente FROM cliente WHERE idcliente = %s', (id_usuario_info,))
#Aseguramos que el ID del usuario existe
            usuario_id = cursor_bd.fetchone()

            if usuario_id:
#Si el usuario existe, mostramos los detalles de sus pedidos
                cursor_bd.execute('SELECT * FROM detalle WHERE idcliente = %s', (id_usuario_info,))
                pedidos_usuario = cursor_bd.fetchall()

                if pedidos_usuario:
                    print(f'Pedidos del usuario con ID {id_usuario_info}')
                    df_pedidos = pd.DataFrame(pedidos_usuario, columns=['idcliente', 'idpedido', 'idproducto', 'precio', 'unidades', 'fecha'])
                    print(df_pedidos)
                else:
                    print(f'No se encontraron pedidos para el usuario con ID {id_usuario_info}.')
            else:
                print('Introduce un ID existente.')
    else:
        print('\nNo se encontraron usuarios en la base de datos.')

#Creamos el menú principal del programa
def menu_principal():
    print(f'\n¿Qué deseas hacer? Acceder a la base de datos de usuarios o realizar/ver el estado de un pedido.')
    
    while True:
        try:
#Mostramos las opciones disponibles
            opcion = int(input(f'1.-Base de datos de Usuarios, 2.-Realizar pedido, 3.-Localizar un pedido, 4.-Salir: '))
            
            if opcion == 1:
                menu_control_usuarios()
            
            elif opcion == 2:
                realizar_pedido()
            
            elif opcion == 3:
                print('\n**Localizador de pedidos**\n')
                seguimiento_de_pedido()
            
            elif opcion == 4:
                print('\nCerrando programa.')
                break
        except ValueError:
            print('Introduzca un número válido.')

menu_principal()
