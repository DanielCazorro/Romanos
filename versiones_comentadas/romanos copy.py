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
    Convierte un número entero en su representación en números romanos.

    Restricciones:
      - Es un número natural
      - El número está entre 1 y 3999 (incluidos)
        - No es negativo (es positivo)
        - No es mayor que 3999

    Args:
        numero (int): Número entero a convertir.

    Returns:
        str: Representación del número en números romanos.

    1. Validar el dato de entrada:
        - Es un número entero
        - Entre 1 y 3999
    2a. Si no es válido: mostrar mensaje de error
    2b. Si es válido: convertir

    Ideas para comprobar si una variable es un número entero:
        - isinstance(valor, tipo)
        - convertir a int y, si no se puede (excepción), retornar el error
    """

    # Validación de entrada
    if not isinstance(numero, int):
        return "ERROR: No has introducido un número entero"

    if numero < 1 or numero > 3999:
        return "ERROR: Debe ser un valor entre 1 y 3999 (incluidos)"

    """
    1. Descomponer el número según el sistema posicional en base 10
       millares, centenas, decenas, unidades

       numero // 1000
       numero %  1000   // 100
       numero %  1000    % 100    // 10
       numero %  1000    % 100     % 10   // 1
    """

    # Descomposición del número
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

    # Construcción del resultado
    resultado = millares[indices[0]] + \
        centenas[indices[1]] + \
        decenas[indices[2]] + \
        unidades[indices[3]]

    return resultado

# Ejemplos de uso
print(convertir_en_romano("56t"))  # ERROR: No has introducido un número entero
print(convertir_en_romano("56"))   # ERROR: No has introducido un número entero
print(convertir_en_romano(-3))      # ERROR: Debe ser un valor entre 1 y 3999 (incluidos)
print(convertir_en_romano(4000))    # ERROR: Debe ser un valor entre 1 y 3999 (incluidos)
print(convertir_en_romano(1123))    # Funciona correctamente: MCXXIII
print(convertir_en_romano(2746))    # Funciona correctamente: MMMDCCXLVI
print(convertir_en_romano(11))      # Funciona correctamente: XI
