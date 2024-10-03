"""Metodo de ordenacion: burbuja"""


def burbuja(nombres, votos, comparacion=None):
    if len(nombres) != len(votos):
        raise ValueError(
            "Las listas nombres y votos deben tener la misma longitud.")

    n = len(votos)

    def comparar(a, b):
        if comparacion is None:
            return a < b
        return comparacion(a, b) < 0

    def intercambiar(i, j):
        nombres[i], nombres[j] = nombres[j], nombres[i]
        votos[i], votos[j] = votos[j], votos[i]

    for i in range(n - 1):
        intercambiado = False
        for j in range(0, n - i - 1):
            if comparar(votos[j], votos[j + 1]):
                intercambiar(j, j + 1)
                intercambiado = True

        if not intercambiado:
            break

    return nombres, votos
