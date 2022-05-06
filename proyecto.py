#PROGRAMA QUE SIMULA LA VALIDACIÓN DE UN REGISTRO E INICIO DE SESIÓN CON PYTHON

#Impotamos el módulo datetime para poder obtener la fecha de hoy
from datetime import date
import re

#Función de control en donde se llaman a las funciones que contienen el programa
def control():
    print("*******REGISTRO A LA PLATAFORMA*******")
    getDate()
    getUser()

#Función getDate en donde obtenemos la fecha de hoy y la imprimimos
def getDate():
    todayDate = date.today()
    print("Fecha de registro:",todayDate)

#Función en donde se valida el registro de usuario y su inicio de sesión
def getUser():
    validationUser = 0
    #Este ciclo nos sirve para validar que el usuario ha ingresado correctamente el usuario
    while validationUser==0:
        #Recibimos los datos del usuario
        userName = input("Nombre de usuario: ")
        userPassword = input("Constraseña: ")
        #Validamos los datos ingresados del usuario
        if not userName.isalpha():
            print("Sólo se aceptan letras para usuario, intente de nuevo")
            #Si los datos son correctos, validar nombre de usuario y contraseña
        elif userName.isalpha and sum(map(userPassword.count,['*','?','-','_','.','ñ','=',"'",'"','!','¡','¿','/','(',')','{','}','[',']'])) == 0:
            #Registro exitoso
            print("***SE HA REGISTRADO, INICIE SESIÓN***")
            validationLogin = 0
            #Ciclo para validar credenciales (LOGIN)
            while validationLogin == 0:
                #Ingreso de datos LOGIN
                validationUserName = input("Ingrese su nombre de usuario: ")
                validationUserPassword = input("Ingrese su contraseña: ")
                #Validación de coincidencia de Datos para Loguearse
                if validationUserName == userName and validationUserPassword == userPassword:
                    print(f"¡¡¡¡BIENVENIDO {userName}!!!!")
                    validationLogin = validationLogin + 1
                #En caso de ser incorrecto, manda mensaje y repite ciclo
                elif validationUser != userName or validationUserPassword != userPassword:
                    print("Credenciales no válidas, intentelo de nuevo")
                    print(validationUserName,validationUserPassword)
            validationUser = validationUser+1
        #En caso de que los datos al registrarse sean incorrectos, manda mensaje
        else:
            print("Datos no válidos, intentelo de nuevo")

    
#Llamado de función principal
control()