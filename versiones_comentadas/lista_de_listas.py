def convertir_en_romano(numero):
    conversores = [
        ["", "M", "MM", "MMM"],
        ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
        ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
        ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    ]

    if not isinstance(numero, int):
        return "ERROR: No has introducido un número entero"

    if numero < 1 or numero > 3999:
        return "ERROR: debe ser un valor entre 1 y 3999 (incluidos)"

    divisores = [1000, 100, 10, 1]

    resultado = ""
    contador = 0
    for divisor in divisores:
        cociente = (numero // divisor)
        numero = numero % divisor
        resultado = resultado + conversores[contador][cociente]
        contador = contador + 1

    return resultado


print(convertir_en_romano("56t"))
print(convertir_en_romano("56"))
print(convertir_en_romano(-3))
print(convertir_en_romano(4000))
print(convertir_en_romano(1123))
print(convertir_en_romano(2746))
print(convertir_en_romano(11))
