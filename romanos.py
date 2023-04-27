class RomanNumber:
    """
        Crear una clase nueva de números. RomanNumber.
        Debe permitir crear este tipo de número pudiendo tener
        valores y realizar las operaciones principales.

        Clase ----> Programación O.O.
        Crear:
            - Número natural entre 1 y 3999
            - Cadena de caracteres "I" y "MMMCMXCIX"
        str() → el número en romano
        .valor = su valor como entero (sistema decimal)

        + → sumar
        - → restar
        / → dividir
        * → producto
        ** → potencia
        // → división entera
        % → resto

        a = RomanNumber(1)      a.valor-->1  str(a) "I"
        b = RomanNumber("I")    b.valor-->1  str(b) "I"
    """

    def __init__(self, entrada):
        if isinstance(entrada, int):
            self.valor = entrada
            self.cadena = self.convertir_en_romano()
        elif isinstance(entrada, str):
            self.cadena = entrada
            self.valor = self.convertir_en_numero()
        else:
            raise TypeError("Solo puedo aceptar enteros y cadenas")

    def __str__(self) -> str:
        return self.cadena

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, otro):
        if isinstance(otro, RomanNumber):
            return self.valor == otro.valor
        elif isinstance(otro, int):
            return self.valor == otro
        elif isinstance(otro, str):
            return self.cadena == otro
        raise TypeError(
            f"{otro} debe ser un número romano, un entero o una cadena")

    def __add__(self, sumando):
        if isinstance(sumando, RomanNumber):
            return self.valor + sumando.valor
        elif isinstance(sumando, int):
            return self.valor + sumando
        elif isinstance(sumando, str):  # sumando = "IV"
            return self.valor + RomanNumber(sumando).valor
            # return RomanNumber(sumando) + self.valor
        raise TypeError("No puedo comparar eso con un número romano")

    def __radd__(self, sumando):
        return self + sumando

    def convertir_en_romano(self):
        numero = self.valor
        if not isinstance(numero, int):
            raise TypeError("ERROR: No has introducido un número entero")

        if numero < 1 or numero > 3999:
            raise ValueError(
                "ERROR: debe ser un valor entre 1 y 3999 (incluidos)")

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

    def convertir_en_numero(self):
        romano = self.cadena
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
