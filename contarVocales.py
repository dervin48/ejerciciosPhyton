def contar_vocales():
    palabra = input("Ingrese una palabra: ")
    vocales = "aeiouAEIOU"
    count = 0
    for letra in palabra:
        if letra.isalpha() and letra in vocales:
            count += 1
    print("La cantidad de vocales en la palabra es", count)

contar_vocales()
