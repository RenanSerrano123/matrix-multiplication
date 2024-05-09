def multiplicar_matrizes(matriz1, matriz2):
    m = len(matriz1)
    n = len(matriz1[0])
    p = len(matriz2[0])
    resultado = [[0 for _ in range(p)] for _ in range(m)]
    for i in range(m):
        for j in range(p):
            for k in range(n):
                resultado[i][j] += 3 * matriz1[i][k] * matriz2[k][j]
    return resultado
def ler_matriz():
    linhas = int(input())
    colunas = int(input())
    matriz = []
    for _ in range(linhas):
        linha = list(map(int, input().split()))
        matriz.append(linha)
    return matriz
def imprimir_matriz(matriz):
    for linha in matriz:
        print(*linha)
matriz_a = ler_matriz()
matriz_b = ler_matriz()
if len(matriz_a[0]) != len(matriz_b):
    print("As matrizes não podem ser multiplicadas.")
else:
    resultado = multiplicar_matrizes(matriz_a, matriz_b)
    imprimir_matriz(resultado)