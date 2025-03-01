# busqueda_matriz.py

def busca_valor(matriz, valor):
    """
    Busca un valor en una matriz bidimensional.

    Args:
        matriz: La matriz bidimensional.
        valor: El valor a buscar.

    Returns:
        Una tupla con la posicion del valor (fila, columna) si se encuentra, o None si no.
    """
    for fila_index, fila in enumerate(matriz):
        for columna_index, elemento in enumerate(fila):
            if elemento == valor:
                return fila_index, columna_index
    return None

# Ejemplo de matriz
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

valor_buscado= 3

posicion = buscar_valor(matriz, valor_buscado)

if posicion:
    print(f"Valor {valor_buscado} encontrado en la posición: {posicion}")
else:
    print(f"Valor {valor_buscado} no encontrado en la matriz.")