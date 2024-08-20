'''
Modulo 3 Sesion 8 - Rebound

En esta actividad trabajaremos con listas. Tomando la lista que se entrega a continuación, 
se solicita realizar las siguientes acciones en el orden indicado:

1. Eliminar los elementos duplicados.
2. Ordenar la lista resultante en orden ascendente.
'''

mi_lista = [5, 20, 15, 20, 25, 50, 20, 5, 18, 15]
setPaso = set(mi_lista)
listaNueva = list(setPaso)
listaNueva.sort()
print(listaNueva)