#Ahora realizaremos algunos ejercicios teoricos para comprender mejor el uso de la funcion type(). 
#¿De que tipo es cada una de las siguientes variables?
totalDeuda = 1450.7
nombreProducto = "Comeder"
lunas = 7
motores = "4"
#Solucion:
print(type(totalDeuda))  # float
print(type(nombreProducto))  # str
print(type(lunas))  # int
print(type(motores))  # str (aunque representa un número, es una cadena de texto por que está entre comillas)


#Ahora analizaremos el siguiente codigo y debeiamos encontrar el error que contiene:
edad gato = 7
correo_electronico = "prueba@gmail.com"
copiaCorreo = correo_electronico
#Solucion: 
# El error está en la primera línea, ya que no se pueden usar espacios en los nombres de las variables.
# La línea correcta sería: edad_gato = 7

#Ahora realizaremos un ejercicio mas practico 
#Implemente un programa qen el cual defina 4 variables: en una que contenga su nombre, otra su apellido, otra su edad y otra su altura. 
#Al final, imprima por pantalla un mensaje que diga: "Hola, mi nombre es [nombre] [apellido], tengo [edad] años y mido [altura] metros."
nombre = "Juan" 
apellido = "Pérez"
edad = 30
altura = 1.75
print(f"Hola, mi nombre es {nombre} {apellido}, tengo {edad} años y mido {altura} metros.")
#Usammos los {} para indicar que queremos que se reemplace por el valor de la variable.
