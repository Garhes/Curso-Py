# variables
my_variable = "Hola"
print(my_variable)
print(len(my_variable))
print("Este es el valor de la variable:", (len(my_variable))) #len es una funcion que cuenta la cantidad de caracteres de una variable

#variables en una sola linea 
name, lastname, age, pais = "Johan", "Garcia", 19, "Colombia"
print(name, lastname, age, pais)
print(name)
print("Este es mi apellido:", lastname, "Tengo una edad de:", age, "Y vivo en:", pais)

#varibale con input (este signfica que el usuario puede ingresar un valor)
"""
name = input("Ingrese su nombre: ")
age = input("Cual es tu edad: ")
print("Hola", name, "Tu edad es:", age) 
print(name)
print(age)
"""

#Forzar el tipo de dato 
name = str = "Johan" # este es un tipo de dato String
name = 19 # este es un tipo de dato Int 
name = 19.5 # este es un tipo de dato Float
name = True # este es un tipo de dato Boolean
name = [10, 20, 30] # este es un tipo de dato List
name = (10, 20, 30) # este es un tipo de dato Tuple
name = {"name": "Johan", "age": 19} # este es un tipo de dato Dictionary
name = {"Johan", "Garcia"} # este es un tipo de dato Set 
print(type(name))