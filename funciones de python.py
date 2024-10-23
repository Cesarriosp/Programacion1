#funciones de python
#para definir funcionemos utilizamos la palabra reservada "def"

# def saluda():
#     print("Hola")
# saluda()

# def suma():
#     suma = 2 + 1
#     print("La suma es", suma)

# def resta():
#     resta = 2 - 3
#     print("La resta es", resta)

# def multiplicacion():
#     multiplicacion = 2 * 3
#     print("La multiplicacion es", multiplicacion)

# def division():
#     division = 2 / 3
#     print("La division es", division)

# #Aqui empieza el codigo pricipal
# print("Vamos a ir ejecutando ")


# suma()
# division()


# #Las funciones pueden recibir parametros
# #Los parametros son variables que la funcion podra utilizar

# def sumapro(numero1, numero2):
#     suma = numero1 + numero2
#     print(f"La suma es {suma}")

# #iniciamos programa

# num1 = int(input("Dame el numero 1:"))
# num2 = int(input("Dame el numero 2:"))
# sumapro(num1, num2)


# def restapro(numero1, numero2):
#     resta = numero1 - numero2
#     print(f"La resta es {resta} ")


# num1 = int(input("Dame el numero1: "))
# num2 = int(input("Dame el numero 2:"))
# restapro(num1, num2)




#PAra que un numero sea primo tiene que ser mayor que 1, y ser divisible por 1 y por el mismo únicamente, si se divide por cualquier otro número el resto será mayor que 0
def es_primo(numero):
    if numero > 1:
        if numero % numero+1 == 0:
            print('No es primo')
        elif (numero % 1 == 0) and (numero % numero == 0):
            print('Es primo')
    else:
        print ('Menor que 1, el número no puede ser primo')


##Programa principal empieza aqui
numero = int(input("Introduce un número entero para averiguar si el número es primo o no, (utilizando '0' como el número final): "))

es_primo(numero)

##############################################
#Solucion con return en la funcion es_primo
############################################
def es_primo(numero):
    valor_devuelto = False
    if numero > 1:
        if numero % numero+1 == 0:
            valor_devuelto = False
        elif (numero % 1 == 0) and (numero % numero == 0):
            valor_devuelto = True
    else:
        valor_devuelto = False
    return valor_devuelto

##Programa principal empieza aqui
numero = int(input("Introduce un número entero para averiguar si el número es primo o no, (utilizando '0' como el número final): "))

valor_funcion = es_primo(numero)

if valor_funcion == True:
    print('Es primo')
else:
    print('No es primo')