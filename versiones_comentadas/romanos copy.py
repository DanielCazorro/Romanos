"""
I - Uno
V - Cinco
X - Diez
L - Cincuenta
C - Cien
D - Quinientos
M - Mil
"""


def convertir_en_romano(numero):
    """
    Restricciones:
      - Es un número natural
      - El número está entre 1 y 3999 (incluidos)
        - No es negativo (es positivo)
        - No es mayor que 3999
    Resultado es una cadena que contiene (I, V, X, L, C, D, M)

    1. Validar el dato de entrada
        - Es un número entero
        - Entre 1 y 3999
    2a. Si no es válido: muestro mensaje de error
    2b. Si es válido: lo convierto

    Ideas para comprobar si una variable es un número entero:
        - isinstance(valor, tipo)
        - convertir a int y, si no se puede (excepción), retornar el error
    """

    if not isinstance(numero, int):
        return "ERROR: No has introducido un número entero"

    if numero < 1 or numero > 3999:
        return "ERROR: debe ser un valor entre 1 y 3999 (incluidos)"

    """
    1. Descomponer el número según el sistema posicional en base 10
       millares, centenas, decenas, unidades

       numero // 1000
       numero %  1000   // 100
       numero %  1000    % 100    // 10
       numero %  1000    % 100     % 10   // 1
    """

    # i_millares = numero // 1000 # 1
    # i_centenas = numero % 1000 // 100 # 1
    # i_decenas = numero % 1000 % 100 // 10 # 2
    # i_unidades = numero % 1000 % 100 % 10 // 1 # 3

    # i_millares = numero // 1000
    # a = numero % 1000

    # i_centenas = a // 100
    # b = a % 100

    # i_decenas = b // 10
    # c = b % 10

    # i_unidades = c // 1
    # # c % 1-----> deshecho

    divisores = [1000, 100, 10, 1]
    indices = []

    for divisor in divisores:
        indices.append(numero // divisor)
        numero = numero % divisor

    print("La descomposición del número es:", indices)

    """
    2. Con cada dígito, usar la lista adecuada para la conversión
       utilizando el dígito como índice
    """

    millares = ["", "M", "MM", "MMM"]
    centenas = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    decenas = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    unidades = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

    # resultado = []
    # resultado.append(millares[indices[0]])
    # resultado.append(centenas[indices[1]])
    # resultado.append(decenas[indices[2]])
    # resultado.append(unidades[indices[3]])

    # conversores = [
    #     ["", "M", "MM", "MMM"]
    #     ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    #     ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    #     ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    # ]

    # resultado = []
    # resultado.append(conversores[0][indices[0]])
    # resultado.append(conversores[1][indices[1]])
    # resultado.append(conversores[2][indices[2]])
    # resultado.append(conversores[3][indices[3]])

    # for i in range(4):
    #     resultado.append(conversores[i][indices[i]])

    resultado = millares[indices[0]] + \
        centenas[indices[1]] + \
        decenas[indices[2]] + \
        unidades[indices[3]]

    return resultado


print(convertir_en_romano("56t"))
print(convertir_en_romano("56"))
print(convertir_en_romano(-3))
print(convertir_en_romano(4000))
print(convertir_en_romano(1123))
print(convertir_en_romano(2746))
print(convertir_en_romano(11))
