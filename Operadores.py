#operadores aritmeticos
print(3+2) #suma
print(3-2) #resta
print(3*2) #multiplicacion
print(3/2) #division
print(3 % 2) #modulo (residuo de la division)
print(3 ** 2) #exponenciacion (elevar a la potencia)
print(3 // 2) #division entera (dividir y redondear al entero mas cercano) 
print(3 + 2 * 5 ** 4 // 1) #se pueden hacer operaciones matematicas con los operadores en un solo print 

print("Hola " + "Mundo") #concatenacion de strings
print("Hola " * 3) #repetir un string
print("Hola " * 3 + "Mundo") #concatenacion y repetir un string
print("Hola " + str(3)) #convertir un numero a string (Con el Str podemos convertir cualquier tipo de dato a string)
print(3 + int("3")) #convertir un string a numero (Con el Int podemos convertir cualquier tipo de dato a numero)

my_flooat = 2.5 * 2 #multiplicar un float por un int
print(my_flooat) 
my_flooat = 2.5 * 2.5 #multiplicar un float por un float
print(my_flooat)
print("Hola " * int(my_flooat)) #convertir un float a int (No se puede convertir un float a int)

"""
podemos pasar un flooat a un numero entero ya que este flooat es un numero no entero que quiere decir esto  
que si tenemos un numero como 2.5 y lo multiplicamos por 2 nos dara un numero entero 5.0
pero si lo pasamos a un (Int) este lo pasara a un numero entero (5)
"""

#operadores de comparacion
print(3 == 2) #igualdad
print(3 != 2) #diferente
print(3 > 2) #mayor que
print(3 < 2) #menor que
print(3 >= 2) #mayor o igual que
print(3 <= 2) #menor o igual que
print("Hola" <  "mundo") #comparar strings compara el orden alfabetico de las letras
print(len("Hola")<= len("hola")) #va a comparar la longitud de las palabras que quiere decir que va a contar cuantas letras tiene cada palabra

#operadores logicos
#AND
print(True and True) #and (y) si las dos expresiones son verdaderas entonces sera verdadero
print(True and False) #si una de las expresiones es falsa entonces sera falso
print(False and False) #si las dos expresiones son falsas entonces sera falso
#OR
print(True or True) #or (o) si una de las expresiones es verdadera entonces sera verdadero
print(True or False) #si las dos expresiones son verdaderas entonces sera verdadero
print(False or False) #si las dos expresiones son falsas entonces sera falso
#NOT
print(not True) #not (no) si la expresion es verdadera entonces sera falsa
print(not False) #si la expresion es falsa entonces sera verdadera
print(not (4 < 2))
print(len("Hola")and len("Hola"))

"""
Escribe un programa que solicite al usuario dos números y luego realice las siguientes operaciones:

Suma
Resta
Multiplicación
División
Módulo
Exponenciación
División entera
Además, realiza las siguientes comparaciones y operaciones lógicas:

Comprueba si el primer número es mayor que el segundo.
Comprueba si el primer número es igual al segundo.
Comprueba si el primer número es diferente del segundo.
Utiliza el operador and para verificar si ambos números son positivos.
Utiliza el operador or para verificar si al menos uno de los números es positivo.
Utiliza el operador not para invertir el resultado de una comparación.

"""

num_1 = int(input("Ingrese u primer numero: "))
num_2 = int(input("Ingrese su segundo numero: "))

print("La suma de los numeros ingresados es: ", num_1 + num_2)
print("La suma de los numeros ingresados es: ", num_1 - num_2)
print("La suma de los numeros ingresados es: ", num_1 * num_2)
print("La suma de los numeros ingresados es: ", num_1 / num_2)
print("La suma de los numeros ingresados es: ", num_1 % num_2)
print("La suma de los numeros ingresados es: ", num_1 ** num_2)

print(num_1 > num_2)
print(num_1 < num_2)
print(num_1 == num_2)
print(num_1 != num_2)
print(num_1 >= num_2)
print(num_1 <= num_2)

print(num_1 > 0 and num_2 > 0) #si los dos numeros son positivos entonces sera verdadero
print(num_1 > 0 or num_2 > 0) #si uno de los dos numeros es positivo entonces sera verdadero
print(not num_1 > 0) #si el numero es positivo entonces sera falso
print(not num_2 > 0) #si el numero es positivo entonces sera falso
