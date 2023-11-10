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
    """

    # Validación de entrada
    if not isinstance(numero, int):
        return "ERROR: No has introducido un número entero"

    if numero < 1 or numero > 3999:
        return "ERROR: Debe ser un valor entre 1 y 3999 (incluidos)"

    # Descomposición del número
    divisores = [1000, 100, 10, 1]
    indices = [numero // divisor for divisor in divisores]
    numero %= 1000  # Actualizar el número para el próximo divisor

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


def convertir_en_numero(romano):
    """
    Convierte un número romano en su representación numérica.

    Args:
        romano (str): Número romano en formato de cadena.

    Returns:
        int: Representación numérica del número romano.
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

    valores_cinco = {5, 50, 500}

    if not isinstance(romano, str):
        raise TypeError("ERROR: Debe ser un número romano en formato de cadena")

    resultado = 0
    anterior = 0
    super_anterior = 0
    cuenta_repes = 1
    restado = False

    for letra in romano:
        if letra not in digitos_romanos:
            raise ValueError(f"ERROR: {letra} no es un dígito romano válido (I, V, X, L, C, D, M)")

        actual = digitos_romanos.get(letra)

        if actual == anterior and actual in valores_cinco:
            raise ValueError('ERROR: No se permiten símbolos V, L, D repetidos')

        if actual > anterior:
            if anterior in valores_cinco:
                raise ValueError("ERROR: No se pueden restar símbolos V, L, D")
            if 0 < anterior*10 < actual:
                raise ValueError("ERROR: Resta no posible")
            if 0 < super_anterior <= anterior < actual:
                raise ValueError('ERROR: No se pueden restar símbolos consecutivos')

            resultado -= anterior
            resultado += (actual - anterior)
            restado = True
        else:   # actual <= anterior
            if actual == anterior:
                cuenta_repes += 1
            else:
                cuenta_repes = 1

            if cuenta_repes > 3:
                raise ValueError('ERROR: No puede haber más de tres símbolos iguales consecutivos')

            if actual >= super_anterior > 0 and restado:
                raise ValueError("ERROR: Resta imposible")

            resultado += actual
            restado = False

        super_anterior = anterior
        anterior = actual

    return resultado


if __name__ == '__main__':
    print(convertir_en_numero('IVI'))  # ERROR: No puede haber más de tres símbolos iguales consecutivos
