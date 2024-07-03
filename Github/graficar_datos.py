import numpy as np
import matplotlib.pyplot as plt
def graficar_funcion():
 funcion = input("Ingrese la función (use x como variable): ")
 x_min = float(input("Ingrese el valor mínimo del intervalo: "))
 x_max = float(input("Ingrese el valor máximo del intervalo: "))
 x = np.linspace(x_min, x_max, 400)
 y = eval(funcion)
 plt.figure(figsize=(8, 6))
 plt.plot(x, y)
 plt.title(f"Gráfica de la función: {funcion}")
 plt.xlabel("x")
 plt.ylabel("y")
 plt.grid(True)
 plt.show()
graficar_funcion()