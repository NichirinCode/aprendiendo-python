#Ahora haremos unos ejercicios para practicar todo lo que hemos visto hasta ahora.

#Implemente un programa en el cual le solicite al usuario que ingrese por teclado: su nombre, su apellido y su estatura. 
#Almacene cada valor en una variable, y al finalizar imprimir por pantalla el contenido y el tipo de variable de cada una.

#Pista: para dejar un espacio en blanco use " " (comillas con un espacio en blanco entre ellas).

#RECUERDA INTENTAR RESOLVERLO POR TI MISMO ANTES DE VER LA SOLUCIÓN.

print("Hola, bienvenido al programa, dime como te llamas.")
nombre = input("Nombre: ")
apellido = input("Apellido: ")
estatura = float(input("Estatura (en metros): "))  
print("Hola " + nombre + " " + apellido + ", veo que mides " + str(estatura) + " metros.")
print(type(nombre))
print(type(apellido))
print(type(estatura))

#-------------------------------------------------------------------------------------------------------------------------------------------------
#Un cientifico loco siempre calcula mal los años en los que probablemente un asteroide impactará la tierra.
#Si el cientifico dice que caera en 10 años, es por que realmente caerá en 5 años (la mitad).
#Implemente un programa en el cual le solicite al usuario que ingrese por teclado en cuantos años cree que caerá el asteroide.(según el cientifico en formato float)
#E imprima por pantalla en cuantos años realmente caerá el asteroide.

print("Hola, bienvenido al programa, en cuantos años crees que caerá el asteroide?")
años_cientifico = float(input("Años: "))
años_reales = años_cientifico / 2
print("El asteroide caerá en " + str(años_reales) + " años.")

