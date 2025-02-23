my_string = "Mi string"
my_other_string = "Mi otra string"

print(len(my_string))
print(len(my_other_string))
print(my_string < my_other_string)

num_1 = input("Ingrese un numero: ")
num_2 = input("Ingrese otro numero: ")

print(num_1 > num_2)
print(num_1 < num_2)
print(num_1 == num_2)
print(num_1 >= num_2)
print(num_1 <= num_2)

salto_de_linea = "Hola\nMundo" #\n es un salto de linea
print(salto_de_linea)

tabulacion = "Hola\tMundo" #\t es una tabulacion    
print(tabulacion)

# Fomateo de strings

name, surname, age = "Johan", "Garcia", 22

print("Hola mi nombre es {} {} y tengo {} años".format(name, surname, age)) #format es un metodo que nos permite formatear un string
print("Hola mi nombre es %s %s y tengo %d años" %(name, surname, age)) # %s es para strings y %d es para numeros enteros %f es para numeros flotantes %c es para caracteres
print(f"Hola mi nombre es {name} {surname} y tengo {age} años") #f es un prefijo que nos permite formatear un string

# desempaquetado de caracteres 

lenguaje = "Python" 
a, b, c, d, e, f = lenguaje 
print(a, b, c, d, e, f)
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

#Divsion de las palabras 
lenguaje_slice = lenguaje [1:3] # Esto [1:3] quiere decir que va a tomar de las posiciones de las letras de la plabra sin contar la numero 3 
print(lenguaje_slice)

lenguaje_slice = lenguaje [1:] # En este espacio [1:] quiere decir que va a tomar la primera le letra en este caso seria 1 hasta la ultima que halla en la palabra
print(lenguaje_slice)

lenguaje_slice = lenguaje [-2] # Va a tomar la palabra y la va a contar al reves y asi no saldra la letra correspondiente
print(lenguaje_slice)

#Reversa 

reversed_lenguaje = lenguaje [::-1] # Va a pasar toda la palabra en reversa para eso es necesario los dos puntos
print(reversed_lenguaje)

#Funciones 

print(lenguaje.capitalize()) # esta funcion nos colocara la primera letra en mayuscula 
print(lenguaje.upper()) # esta funcion nos colocara toda la palabra en mayuscula 
print(lenguaje.count("t")) # esta funcion nos contara cuatas letras tiene la palabra en este caso se escogio la t
print(lenguaje.isnumeric()) # en esra funcion nos dira si la palabra escogida es un numero en este caso es FALSE 
print("1".isnumeric()) # en esta funcion nos dira si la plabara es un numero en este caso es un TRUE
print(lenguaje.lower()) # con esta funcion nos colocara toda la palabra en minuscula 
print(lenguaje.upper().isupper) # quiere decir esta funcion que si tenemos la palabra en mayuscula esta saldra que es TRUE y si no esta saldra como FALSE






#Ejercicio de suma pasar un numero de str a un numero int y asi mismo poderlos sumar 
num1 = input("Ingrese un numero: ")
num2 = input("Ingrese otro numero: ")

print("la suma de los numeros ingresados son: ", int(num1) + int(num2))



# Ejercicio 1
# Escriba un programa que pida al usuario su nombre y edad.
# El programa debe imprimir un mensaje que diga "Hola, [nombre], el año que viene tendrás [edad+1] años"

print("Hola como estas?")
name = input("Ingrese su nombre: ")
age = int(input("Ingrese su edad porfavor: "))

print("Hola, ", name, "El año que viene tendras: ", age + 1, "años")

# Ejercicio 2
# Escriba un programa que pida al usuario su nombre y edad.
# El programa debe imprimir un mensaje que diga "Hola, [nombre], el año que viene tendrás [edad+1] años"
# El programa debe imprimir un mensaje que diga "Hola, [nombre], el año pasado tenías [edad-1] años"

print("Programa realizado por Johan Garcia")
name = input("Ingrese su nombre por favor: ")
age = int(input("Ingrese su edad por favor: "))
print("Hola, ", name, "El año que viene tendras: ", age + 1, "años", "El año pasado tenias: ", age - 1, "años")