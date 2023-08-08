import tkinter as tk

def saludar():
    nombre = entrada_nombre.get()
    mensaje_salida.config(text=f"Hola, {nombre}!")

# Crear una ventana
ventana = tk.Tk()
ventana.title("Ejemplo de Interfaz Gráfica")

# Etiqueta
etiqueta = tk.Label(ventana, text="Ingrese su nombre:")
etiqueta.pack(pady=10)

# Entrada de texto
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack(pady=5)

# Botón
boton_saludar = tk.Button(ventana, text="Saludar", command=saludar)
boton_saludar.pack(pady=10)

# Etiqueta para el mensaje de salida
mensaje_salida = tk.Label(ventana, text="")
mensaje_salida.pack(pady=5)

# Ejecutar el bucle de eventos
ventana.mainloop()
