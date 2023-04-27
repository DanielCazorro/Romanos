def convertir_en_romano(numero):

    if not isinstance(numero, int):
        return "ERROR: No has introducido un número entero"

    if numero < 1 or numero > 3999:
        return "ERROR: debe ser un valor entre 1 y 3999 (incluidos)"

    divisores = [1000, 100, 10, 1]
    indices = []

    for divisor in divisores:
        indices.append(numero // divisor)
        numero = numero % divisor

    millares = ["", "M", "MM", "MMM"]
    centenas = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    decenas = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    unidades = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

    resultado = millares[indices[0]] + \
        centenas[indices[1]] + \
        decenas[indices[2]] + \
        unidades[indices[3]]

    return resultado


def convertir_en_numero(romano):
    """
    XIXX --> 29? ----> XXIX
    """

    digitos_romanos = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1
    }

    valores_cinco = (5, 50, 500)

    if not isinstance(romano, str):
        raise TypeError(
            "ERROR: tiene que ser un número romano en formato cadena")

    resultado = 0
    anterior = 0
    super_anterior = 0
    cuenta_repes = 1
    restado = False
    for letra in romano:
        if letra not in digitos_romanos:
            raise ValueError(
                f"ERROR: {letra} no es un dígito romano válido (I, V, X, L, C, D, M)")

        actual = digitos_romanos.get(letra)

        if actual == anterior and actual in valores_cinco:
            raise ValueError('ERROR: no simbolos V, L, D repetidos')

        if actual > anterior:
            if anterior in valores_cinco:
                raise ValueError(
                    "ERROR: no puedes restar simbolos V, L, D")
            if 0 < anterior*10 < actual:
                raise ValueError("ERROR: resta no posible")
            if 0 < super_anterior <= anterior < actual:
                raise ValueError(
                    'ERROR: no puedes restar simbolos consecutivos')

            resultado = resultado - anterior
            resultado = resultado + (actual - anterior)
            restado = True
        else:   # actual <= anterior

            if actual == anterior:
                cuenta_repes = cuenta_repes + 1
            else:
                cuenta_repes = 1
            if cuenta_repes > 3:
                raise ValueError(
                    'ERROR: no puede haber más de tres símbolos iguales consecutivos')
            if actual >= super_anterior > 0 and restado:
                raise ValueError("ERROR: resta imposible")
            resultado = resultado + actual
            restado = False

        super_anterior = anterior
        anterior = actual

    return resultado


if __name__ == '__main__':
    print(convertir_en_numero('IVI'))
