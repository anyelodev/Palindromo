def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    palabraInvertida = palabra[::-1]
    if palabra == palabraInvertida:
        return True
    else:
        return False


def run():
    palabra =  input("Escribe una frase o palabra: ")
    esPalindromo = palindromo(palabra)
    
    if esPalindromo == True:
        print(palabra + "... Es un palindromo")
    else:
        print(palabra + "... No es palindromo")


if __name__ == '__main__':
    run()