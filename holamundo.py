# mi_nombre = "Cesar"
# mi_edad = "19"
# print ("Mi nombre es", mi_nombre)
# print ("Mi edad es", mi_edad)



# lado = 5
# area = lado * lado
# print ("EL área del cuadrado es", area)

# edad = 16
# es_adulto = edad >=18
# print("¿Es adulto?", es_adulto)


#edad = input ("Introduce tu edad: ")
#edad = int(edad)
#edad_futura = edad + 10
#print("En 10 años tendras", edad_futura, "años")
# a = 5
# b = 3
# resultado = a + b
# print(resultado)

#numero = int(input ("Introduce un numero"))


#nombre = "Cesar"
#apellido = "Rios"
#nombre_completo = nombre + " " + apellido
#print (nombre_completo)

# frase = "Python"
# letra = frase[0]
# print(letra)

# frase = "Python"
# longitud = len(frase)
# print(longitud)

# mi_lista = [1,2,3,4,5]
# print(mi_lista)

# mi_lista =["manzana", "banana"]
# # print(mi_lista[1])
# mi_lista.append("cereza")
# print(mi_lista)

# mi_lista =["manzana", "banana", "cereza"]
# mi_lista.remove("banana")
# print(mi_lista)

# edad = int(input("Dime tu edad:"))
# if edad >= 18: 
#     print("Eres mayor de edad")
# else: 
#     print("Eres menor de edad")

# nota = int(input("Dime tu nota"))
# if nota >= 90: 
#     print("Eres sobresaliente")
# elif nota >= 80:
#     print("Eres notable")
# elif nota >= 70:
#     print("Eres bueno")
# else: 
#     print("Eres suficiente o menos")

# edad = int(input("Dime tu edad"))
# if edad < 5:
#     print("Enhorabuena, entras gratis")
# elif edad >=5 and edad <= 12:
#     print("Tu entrada cuesta 5 euros")
# elif edad >=13 and edad <= 17:
#     print("Tu entrada cuesta 7 euros")
# else:
#     print("Tu entrada cuesta 10 euros") 

# nota = int(input("¿Que nota has sacado?")) 
# match nota:
#     case 90:
#         print("Excelente")  
#     case 85:
#         print("Muy bien")
#     case 70:
#         print("Aprobado")
#     case _:
#         print("Mejor suerte la proxima vez")   
#     Si ponemos una nota que no sea exactamente 
#       90 u 85 etc el programa no nos dira la rsepuesta correctamente

# nota = int(input("Dime tu nota"))
# if nota >= 90 and nota <100: 
#     print("Tu calificacion es A")
# elif nota >=80 and nota <90:
#     print("Tu calificacion es B")
# elif nota >=70 and nota <80:
#     print("Tu calificacion es C")
# elif nota >60 and nota <70:
#     print("Tu calificacion es D")
# else:
#     print("Tu calificacion es F")


# dia = int(input("Dime un número entre 1 y 7"))
# match dia:
#     case 1:
#         print("Lunes")
#     case 2:
#         print("Martes")
#     case 3:
#         print("Miércoles")
#     case 4: 
#         print("Jueves")
#     case 5:
#         print("Viernes")
#     case 6:
#         print("Sábado")
#     case 7: 
#         print("Domingo")
#     case _: 
#         print("El número es inválido")



# edad = int(input("Dime tu edad"))
# if edad < 12:
#     print(" Eres un niño")
# elif edad >= 12 and edad <= 17:
#     print("Eres un adolescente")
# elif edad >=18 and edad <= 59:
#     print("Eres un adulto")
# else:
#     print("Eres un adulto mayor")


# idioma = input("Selecciona idioma")
# match idioma:
#     case "es":
#         print("Buenos días")
#     case "en":
#         print("Good morning")
#     case "fr":
#         print("bonjour")
#     case _:
#         print("Idioma no soportado")



# vehiculo = str(input("Dime el tipo de vehículo"))
# vehiculo_entero = vehiculo.lower
# if vehiculo_entero == "coche":
#     print("El Vehículo es de 4 ruedas")
# elif vehiculo_entero == "moto":
#     print("El vehiculo es de 2 ruedas")
# elif vehiculo_entero == "bicicleta":
#     print("Vehículo no motorizado")
# else:
#     print("Vehículo no reconocido")


# color = str(input("Dime tu color favorito"))
# color_entero = color.lower
# match color_entero:
#     case "rojo":
#             print("Has seleccionado el rojo")
#     case "azul":
#         print("Has seleccionado el azul")
#     case "verde":
#         print("Has seleccionado el verde")

#EJERCICIO 1 

# num1 = float(input("Dame el primer número"))
# num2 = float(input("Dame el segundo número"))

# operacion =str(input("¿que operacion quieres hacer?"))

# if operacion == "suma":
#    resultadosuma = num1 + num2 
#    print("la suma es", resultadosuma)
# elif operacion =="resta":
#     resultadoresta = num1 - num2
#     print("La resta es", resultadoresta)
# elif operacion =="multiplicacion":
#     resultadomulti = num1 * num2
#     print("El resultado es", resultadomulti)

# else:
#     print("No has mas operaciones")   


# if operacion =="division" and num2 == 0:
#     print("ERROR")
# elif operacion == "division":
#     resultadodivi = num1 / num2
#     print("La multiplicaión es", resultadodivi)

# #EJERCICIO 2

# numero = int(input("Dime un número"))
# if numero % 2 == 0:
#     print("El número es par")
# else:
#     print("El número es impar")


# #EJERCIO 3
# numero = int(input("Dime un número"))
# suma = 0
# for i in range(1, numero +1 ) :
#     suma = suma + i
# print("La suma de los números es", suma)

# #EJECICIO 4

# vocales = str(input("Escribe una cadena de texto"))
# vocales_mas = vocales.lower

# #EJERCICIO 5

# num = 30
# adivinar = int(input("Adivina el numero"))
# while adivinar != num:
#         if adivinar < num:
#             print("El número es mas alto")
#         elif adivinar > num:
#             print("El número es más bajo")
#         adivinar = int(input("Adivina el número"))

# print("Lo has adivinado")



# numero = int(input("Dime un numero"))
# suma = 0
# for i in range(1, numero +1):
#     suma += i
#     print(suma % 2 == 0)
   

# lista1 = [1,2,3,4]

# tupla1 = (1,2,3,4)
# print ("valor de la lista", lista1)
# print("valor de la tupla", tupla1)

# lista1[0] = 10

# print(lista1)

# tupla1[0] = 10
# print(tupla1)



# dic1 = {}

# nombre = input("introduce el nombre del nuevo contacto:")
# tlf = input("Introduce el nuevo número:")

# dic1[nombre] = tlf
# print(dic1)

# print("Vamos a modificar el teléfono de un contacto")
# nombre_busqueda = input("Dame el nuevo nombre del usuario:").lower()
# tlf_busqueda = input("Dame el nuevo número:")

# dic1[nombre_busqueda] = tlf_busqueda
# print(dic1)


# print("Añade tus canciones favoritas")
# num_musica = int(input("Dime el número de canciones que vas a añadir"))
# print("Añade las canciones:")
# playlist =[]
# for canciones in range(0, num_musica):
#     canciones2 = [[input("Dime una canción")]]
#     playlist.append(canciones2)
#     print("Has añadido:", canciones2, "a tu lista de reproducción" )

    
# lista_reproduccion =[]

# #tengo que permitir introducir canciones hasta que ponga fin

# cancion = input("Dam el nombre de una canción")

# while cancion != "fin":
#     lista_reproduccion. append(cancion)
#     cancion = input("Dame otra canción").lower()

# # while True:
# #     cancion = input("Dame el nombre de una canción")
# #     if cancion != "fin":
# #         lista_reproduccion.append(cancion)
# #     else:
# #         break

# print(lista_reproduccion)



# #mostrar mi lista de rep y permitir al usuario introducir el numero de la
# #cancion que quiere escuchar

# for i in range (len(lista_reproduccion)):
#     print(f"{i}.- {lista_reproduccion[i]}")

# cancion_a_reproducir = int(input("Dime el número de canción que desead escuchar"))

# print(f"Estas escuchando la cancioón: {lista_reproduccion[cancion_a_reproducir]}")



#Esto es una lista
lista_reproduccion = []
print("Crea tu lista de reproducción")

#Se usa cuando no se cuantas veces se va a repetir el codigo, por ejemplo
#como en este caso no se cuantas canciones va a añadir usamos while true
#Es un bucle infinito que se detiene con un break cuando se cumple la
#condicion que queremos
while True:
    cancion = input("Ingresa el mombre de la canción, cuando termines escribe 'fin' ")

    if cancion.lower() == "fin":
        break
    else:
        lista_reproduccion.append(cancion)

#Ahora mostramos la lista de las canciones 
print("\n", lista_reproduccion)

indice = 1

for cancion in lista_reproduccion:
#Esto es lo mismo escrito de distinta forma
    # print(indice," ", cancion)
    # print(f"{indice}. {cancion}")
    print(f"{indice}. {cancion}")
