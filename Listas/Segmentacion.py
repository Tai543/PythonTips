'''
@author Tai543
Listas: Indices
'''
# Definamos la lista 'python'
python = ['P','Y','T','H','O','N']
# Los indices de los elementos de la lista 
# 'python' se pueden leer de las siguientes formas 
'''
+---+---+---+---+---+---+
| P | Y | T | H | O | N |
+---+---+---+---+---+---+           indices
| 0 | 1 | 2 | 3 | 4 | 5 | <<-- izquierda a derecha
+---+---+---+---+---+---+           indices
|-6 |-5 |-4 |-3 |-2 |-1 | <<-- derecha a izquierda
+---+---+---+---+---+---+
'''
# Mostremos el primer elemento de la lista 'python'
# usando ambos tipos de indices 😎👩🏻‍🏫👩🏻‍💻
print(python[0])
# Resultado: P
print(python[-6])
# Resultado: P

'''
@author Tai543
Listas: Segmentacion
'''
# La segmentacion es una propiedad muy cool de las 
# listas en python 😎👩🏻‍🏫👩🏻‍💻 para usarla solo tenemos 
# que seguir la siguiente notacion '[inicio:fin]' 
# 'inicio' --  indice donde inicia el segmento
# 'fin' -- indice donde finiliza el segmento + 1    
# Vamos a definir la lista 'python'  
python = ['P','Y','T','H','O','N']
print(python)
# Resultado: ['P', 'Y', 'T', 'H', 'O', 'N']
# Vamos a mostrar solo los dos primeros elementos 
# de la lista 'python' para esto el indice de 
# 'inicio' sera 0 y indice de 'fin' sera 2 '[0:2]'
print(python[0:2])
# Resultado: ['P', 'Y']
# Como el indice de 'inicio' es 0 tambien podemos 
# mostrar los elementos de la siguiente forma '[:2]'
print(python[:2])
# Resultado: ['P', 'Y']
