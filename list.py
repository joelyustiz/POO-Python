my_list = [1,2,3]

double = [i * 2for i in my_list]

print(double)

my_list = list(range(100)) #lista de 0 a 99
print(my_list)

double = [doblar_valor * 2for doblar_valor in my_list]
print(f'double= {double}')

pares = [numpar for numpar in my_list if numpar % 2 == 0]
print(f'pares= {pares}')



"""
append()
Añade un ítem al final dela lista:

Código

lista = [1,2,3,4,5]
lista.append(6)
lista
Resultado
---------------------------------------------------------
clear()
Vacía todos los ítems de una lista:

Código

lista.clear()
lista
Resultado
--------------------------------------------------
extend()
Une una lista a otra:

Código

l1 = [1,2,3]
l2 = [4,5,6]
l1.extend(l2)
l1
Resultado

---------------------------------------------------------
count()
Cuenta el número de veces que aparece un ítem:

Código

["Hola", "mundo", "mundo"].count("Hola")
Resultado
-----------------------------------------------------------

index()
Devuelve el índice en el que aparece un ítem (error si no aparece):

Código

["Hola", "mundo", "mundo"].index("mundo")
Resultado
---------------------------------------------------------------
insert()
Agrega un ítem a la lista en un índice específico:

Primera posición (0):

Código

l = [1,2,3]
l.insert(0,0)
l
Resultado
------------------------------------------------------------
Penúltima posición (-1):

Código

l = [5,10,15,25]
l.insert(-1,20) 
l
Resultado
----------------------------------------------------------
Última posiciónen una lista con len():

Código

l = [5,10,15,25]
n = len(l)
l.insert(n,30)
l
Resultado

------------------------------------------------------------------
Una posición fuera de rango añade el elemento al final de la lista (999):

Código

l.insert(999, 35)
l
Resultado
pop()
Extrae un ítem dela lista y lo borra:

Código

l = [10,20,30,40,50]
print(l.pop())
print(l)
Resultado
-------------------------------------------
Podemos indicarle un índice con el elemento a sacar (0 es el primer ítem):

Código

print(l.pop(0))
print(l)
Resultado

----------------------------------------------
remove()
Borra el primer ítem dela lista cuyo valor concuerde con el que indicamos:

Código

l = [20,30,30,30,40]
l.remove(30)
print(l)
Resultado
---------------------------------------------------------
reverse()
Le da la vuelta a la lista actual:

Código

l.reverse()
print(l)
Resultado
Las cadenas no tienen el método .reverse() pero podemos simularlo haciendo unas conversiones:

Código

lista = list("Hola mundo")
lista.reverse()
cadena = "".join(lista)
cadena    
Resultado

-----------------------------------------------------------------------
sort()
Ordena automáticamente los ítems de una lista por su valor de menor a mayor:

Código

lista = [5,-10,35,0,-65,100]
lista.sort()
lista
Resultado

--------------------------------------------------------------------

Podemos utilizar el argumento reverse=True para indicar que la ordene del revés:

Código

lista.sort(reverse=True)
lista
"""