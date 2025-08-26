### Listas ###
# Listas son estructuras de datos que permiten almacenar múltiples valores en una sola variable.
# Se pueden almacenar diferentes tipos de datos en una misma lista.
# Se pueden almacenar listas dentro de listas.
mi_lista = [1,2,3,4,5]
print(mi_lista)
print(len(mi_lista)) # Longitud de la lista
print(type(mi_lista)) # Tipo de la lista

lista_nombres = [19, 1.70, "Johan", "Garcia"] # Diferentes tipos de datos en una misma lista
print(type(lista_nombres))
print(lista_nombres)
print(len(lista_nombres))
print(lista_nombres[0]) # Acceder al primer elemento de la lista esto quiere decir que siempre se empieza a contar desde el numero 0 
print(lista_nombres[1])  
print(lista_nombres[2]) 
print(lista_nombres[3])
print(lista_nombres[-3]) # Tambien podemos empezar desde la parte desde atras de la lista en este caso vamos a llamar al elemento de la lista que es la altura 
print(lista_nombres[-2])
print(lista_nombres[-1]) 
print(lista_nombres[0]) 

nombres = lista_nombres[0] # vamos a guardar el dato de la lista 
print(nombres) # Imprimimos el dato guardado en la variable nombres



number = [1,2,3,4,5,6,7,8,9,10] # Creamos una lista con los numeros del 1 al 10
number_1, number_2, number_3, number_4, number_5, number_6, number_7, number_8, number_9, number_10, *rest = number # Desempaquetamos la lista en diferentes variables
print(number_1) # Imprimimos el resto de la lista que no se ha desempaquetado

# Unir dos listas
lista1 = [1,2,3,4,5]
lista2 = [6,7,8,9,10]
print(lista1 + lista2)

my_list = [1, 2, 3, 4, 5]
new_list = [6, 7, 8, 9, 10]
my_list.append(11) # Lo que hace append es agregar un solo elemento al final de la lista
my_list.insert(0, 0) # Lo que hace insert es agregar un elemento en la posicion que le indiquemos
my_list.extend(new_list) # Lo que hace extend es agregar varios elementos al final de la lista
my_list.remove(3) # Lo que hace remove es eliminar la primera ocurrencia del valor
my_list.pop() # Lo que hace pop es eliminar el ultimo elemento de la lista
my_list.clear() # Lo que hace clear es eliminar todos los elementos de la lista

print(my_list)
print(type(my_list))

my_list = [1, 2, 3, 4, 5]

copy_list = my_list.copy() # Copia toda la lista que se le indica 
print(copy_list)

my_list.reverse() # Invierte el orden de la lista original
print(my_list)

my_list.sort() # Ordena la lista original en orden ascendente
print(my_list)
