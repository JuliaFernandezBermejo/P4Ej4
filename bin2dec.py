Python 3.10.7 (v3.10.7:6cc6b13308, Sep  5 2022, 14:02:52) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # ------------------------------------------------------
... # Convierte un número binario a decimal.
... # El binario es un string e.g. "101"
... # ------------------------------------------------------
... def bin2dec(numero_binario):
...     numero_decimal = 0
... 
...     j = len(numero_binario) - 1
...     for i in range(len(numero_binario)-1):
...         numero_decimal = numero_decimal + 2 ** i * int(numero_binario[j])
...         j -= 1
... 
...     if numero_binario[0] == "1":
...         numero_decimal -= 2**(len(numero_binario)-1)
...     return numero_decimal
... 
... # ----------------------------------------
... # MAIN
... # ----------------------------------------
... if __name__ == "__main__":
...     # Pide al usuario el número binario a convertir 
...     # Como el número binario es un string, no hace falta usar int()
...     numero_binario = input("Escribe el número en binario que quieres convertir: ")
... 
...     # se llama a la función bin2dec() para hacer la conversión
...     numero_decimal = bin2dec(numero_binario)
... 
...     # Muestra por pantalla el resultado.
...     # Para imprimir un entero es necesario convertirlo a string con str()
