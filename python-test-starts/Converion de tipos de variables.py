# Conversion de tipos de variables
# En este ejemplo, se muestra como convertir tipos de variables en Python usando las funciones int() y str().

print("¿Cual es tu edad?")
edad = int(input()) #Aqui se espera que el usuario ingrese su edad usando int() para convertir el valor ingresado a un numero entero
print("Tienes " + str(edad) + " años.") #Aqui se muestra un mensaje con la edad ingresada. Usamos str() para convertir el numero a cadena y poder concatenarlo con el mensaje.
mitad_edad = edad / 2
print("La mitad de tu edad es " + str(mitad_edad) + " años.") #Aqui se muestra un mensaje con la mitad de la edad ingresada.

#En el siguiente ejemplo muestra la diferencias al convertir los valores recinbidos por la funcion input() a diferentes tipos de datos.

edadPadre = input("¿Cual es la edad de tu padre? ") #Aqui se espera que el usuario ingrese la edad de su padre como una cadena
edadMadre = int(input("¿Cual es la edad de tu madre? ")) #Aqui se espera que el usuario ingrese la edad de su madre como un numero entero
estaturaHermano = float(input("¿Cual es la estatura de tu hermano en metros? ")) #Aqui se espera que el usuario ingrese la estatura de su hermano como un numero decimal
print(type(edadPadre)) #Aqui se muestra el tipo de dato de la variable edadPadre, que es str
print(type(edadMadre)) #Aqui se muestra el tipo de dato de la variable edadMadre, que es int
print(type(estaturaHermano)) #Aqui se muestra el tipo de dato de la variable estaturaHermano, que es float
print(edadPadre)
print(edadMadre)
print(estaturaHermano)

#Ahora haremos otro ejemplo y enseñarles un poco mas sobre la conversion de tipos de variables en Python.
print("¿Como te llamas?")
nombre = input()
print("¿Cual es tu edad?")
edad = input() 
print("Eres estudiante o trabajador?")
estado = input()
print("Hola " + nombre + ", tienes " + edad + " años y eres " + estado + ".")
