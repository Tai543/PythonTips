'''
@author Tai543
Funciones de Listas
Veamos funciones utiles para manejar listas
'''
# En 'emociones' vamos a definir una lista
emociones = list(['u_u','uwu','o_o','uwu'])
print(emociones)
# Resultado: ['u_u', 'uwu', 'o_o', 'uwu']
# Con la funcion 'count()' vamos a contar el numero 
# de veces que 'uwu' aparece en la lista 'emociones'
nro_uwus = emociones.count('uwu')
print(nro_uwus)
# Resultado: 2
# Con la funcion 'index()' vamos a obtener la posicion 
# de 'uwu' en la lista 'emociones'
posicion_uwu = emociones.index('uwu')
print(posicion_uwu)
# Resultado: 1
#🛑 Si te diste cuenta tenemos 2 'uwu' en la lista 🛑
# Si los elementos de una lista se repiten la funcion 
# 'index()' solo nos devolvera la posicion de la 
# primera aparicion del elemento 👩🏻‍🏫👩🏻‍💻

'''
@author Tai543
Funciones de Listas
Veamos funciones utiles para manejar listas
'''
# Vamos a definir dos listas de numeros
pares = [2,6,8,10]
numeros = list([1,3,5,7,9])
# Vamos a agregar un 4 despues del 2 es decir 
# en la posicion 1 en la lista 'pares' usando 
# la funcion 'insert(posicion, elemento)' 
# 👩🏻‍🏫👩🏻‍💻🛑 Las listas empiezan en la posicion 0
pares.insert(1,4)
print(pares)
# Resultado: [2, 4, 6, 8, 10]
# Ahora que los pares estan completos agregaremos 
# todos los elementos de la lista 'pares' a la 
# lista 'numeros' con la funcion 'extend()'
numeros.extend(pares)
print(numeros)
# Resultado: [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
# Ordenemos la lista para que se vea mas cool 😎
numeros.sort()
print(numeros)
# Resultado: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

'''
@author Tai543
Funciones de Listas
Veamos funciones utiles para manejar listas
'''
# Vamos a definir la listas 'awa'
awa = ['awa','de','uwu']
# En la lista 'emociones' vamos a copiar la lista 
# 'awa' usando el operador '='
emociones = awa
print(emociones)
# Resultado: ['awa', 'de', 'uwu']
# Vamos a revertir la lista emociones con la funcion 
# 'reverse()' y veremos que paso con la lista 'awa'
emociones.reverse()
print(emociones)
# Resultado: ['uwu', 'de', 'awa']
print(awa)
# Resultado: ['uwu', 'de', 'awa']
# 🛑🙀 Oh no! ambas listas fueron modificadas
# Cuando usamos el operador '=' las lista 
# involucradas se convierten en un espejo de 
# la otra 👩🏻‍🏫👩🏻‍💻🛑

'''
@author Tai543
Funciones de Listas
Veamos funciones utiles para manejar listas
'''
# Vamos a definir la listas 'uwu'
uwu = ['uwu','sin','ewe']
# En la lista 'emociones' vamos a copiar la lista 
# 'uwu' usando el la funcion 'copy()'
emociones = uwu.copy()
print(emociones)
# Resultado: ['uwu', 'sin', 'ewe']
# Vamos a vaciar la lista emociones con la funcion 
# 'clear()' y veremos que paso con la lista 'uwu'
emociones.clear()
print(emociones)
# Resultado: []
print(uwu)
# Resultado: ['uwu', 'sin', 'ewe']
# 🛑👩🏻‍🏫 Al usar la funcion 'copy()' ambas listas 
# son independientes lo que quiere decir que 
# cualquier cambio que sufra una no afecta a 
# la otra 👩🏻‍💻🛑

