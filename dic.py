"""

colores = { "amarillo":"yellow", "azul":"blue", "verde":"green" }
get()
Busca un elemento a partir de su clave y si no lo encuentra devuelve un valor por defecto:

Código

colores.get('negro','no se encuentra')
Resultado

------------------------------------------

keys()
Genera una lista en clave de los registros del diccionario:

Código

colores.keys()
Resultado

------------------------------------------

values()
Genera una lista en valor de los registros del diccionario:

Código

colores.values()
Resultado
------------------------------------------
items()
Genera una lista en clave-valor de los registros del diccionario:

Código

colores.items()
Resultado

------------------------------------------

Código

for clave, valor in colores.items():
    print(clave, valor)
Resultado

------------------------------------------

pop()
Extrae un registro de un diccionario a partir de su clave y lo borra, acepta valor por defecto:

Código

colores.pop("amarillo", "no se ha encontrado")
Resultado

------------------------------------------

Código

colores.pop("negro","no se ha encontrado")
Resultado

------------------------------------------

clear()
Borra todos los registros de un diccionario:

Código

colores.clear()
colores
Resultado

"""