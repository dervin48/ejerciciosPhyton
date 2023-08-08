def fibonacci():
    numero = int(input("Ingrese número para la secuencia Fibonacci:"))
    secuencia = [0, 1]

    for i in range(2, numero):
        secuencia.append(secuencia[i - 1] + secuencia[i - 2])

    return secuencia

resultado = fibonacci()
print(resultado)