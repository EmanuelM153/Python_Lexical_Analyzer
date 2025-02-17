import sys

texto = sys.stdin.readlines()

espacio_blanco = [' ', '\t']

lexema = ""
for numero_linea, linea in enumerate(texto):
    inicio = 1
    for numero_char, char in enumerate(linea):
        noEsEspacio = not(char in espacio_blanco)
        esSaltoLinea = char == '\n'
        if noEsEspacio and not esSaltoLinea:
            lexema += char
        elif esSaltoLinea:
            numero_linea += 1
        else:
            inicio += 1

        if numero_char + 1 < len(linea):
            siguienteCaracter = linea[numero_char + 1]
            if ((siguienteCaracter in espacio_blanco and noEsEspacio) or siguienteCaracter == '\n'):
                print(f"<{lexema},{numero_linea + 1},{inicio}>")
                inicio = numero_char + 2
                lexema = ""
