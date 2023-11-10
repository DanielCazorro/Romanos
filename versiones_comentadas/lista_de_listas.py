def convertir_en_romano(numero):
    # Lista de listas que contiene los símbolos romanos para cada posición
    conversores = [
        ["", "M", "MM", "MMM"],
        ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
        ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
        ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    ]

    # Validación de entrada: asegurarse de que el número sea un entero positivo entre 1 y 3999
    if not isinstance(numero, int):
        return "ERROR: No has introducido un número entero"
    if numero < 1 or numero > 3999:
        return "ERROR: Debe ser un valor entre 1 y 3999 (incluidos)"

    # Lista de divisores correspondientes a las unidades, decenas, centenas y millares
    divisores = [1000, 100, 10, 1]

    resultado = ""
    contador = 0

    # Iterar a través de los divisores
    for divisor in divisores:
        cociente = numero // divisor  # Calcular el cociente de la división entera
        numero %= divisor  # Actualizar el número para el próximo divisor
        resultado += conversores[contador][cociente]  # Agregar el símbolo romano al resultado
        contador += 1  # Moverse al siguiente conversor

    return resultado

# Ejemplos de uso
print(convertir_en_romano("56t"))  # ERROR: No has introducido un número entero
print(convertir_en_romano("56"))   # ERROR: No has introducido un número entero
print(convertir_en_romano(-3))      # ERROR: Debe ser un valor entre 1 y 3999 (incluidos)
print(convertir_en_romano(4000))    # ERROR: Debe ser un valor entre 1 y 3999 (incluidos)
print(convertir_en_romano(1123))    # Funciona correctamente: MCXXIII
print(convertir_en_romano(2746))    # Funciona correctamente: MMMDCCXLVI
print(convertir_en_romano(11))      # Funciona correctamente: XI
