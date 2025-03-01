# ordenacion_matriz.py

def ordenar_fila(matriz, fila_index):
    """
    Ordena una fila especifica de una matriz bidimensional usando Bubble Sort.

    Args:
        matriz: La matriz bidimensional.
        fila_index: El índice de la fila a ordenar.
    """
    fila = matriz[fila_index]
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]

# Ejemplo de matriz
matriz = [[9, 2, 3], [4, 1, 6], [7, 8, 5]]

fila_a_ordenar = 2

print("Matriz original:", matriz)

ordenar_fila(matriz, fila_a_ordenar)

print(f"Matriz con la fila {fila_a_ordenar} ordenada:", matriz)