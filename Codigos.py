import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
from sympy import symbols, diff, lambdify
import os
import argparse

# Función para evaluar una expresión matemática dada una variable x
def f(x, funcion):
    return eval(funcion)

# Método de Bisección
def biseccion(funcion, a, b, tol=1e-6, max_iter=100):
    if f(a, funcion) * f(b, funcion) >= 0:
        print("El intervalo no es válido. La función debe cambiar de signo en el intervalo.")
        return None, None
    datos = []
    xr_anterior = None
    for i in range(max_iter):
        c = (a + b) / 2
        f_a = f(a, funcion)
        f_c = f(c, funcion)
        f_a_f_c = f_a * f_c
        if xr_anterior is not None:
            aproximacion = abs((c - xr_anterior) / c)
        else:
            aproximacion = None
        datos.append([a, b, c, f_a, f_c, f_a_f_c, aproximacion])
        if abs(f_c) < tol:
            break
        elif f_a * f_c < 0:
            b = c
        else:
            a = c
        xr_anterior = c
    if abs(f(c, funcion)) < tol:
        print(f"La raíz aproximada por Bisección es: {c}")
    else:
        print("El método de Bisección no converge después de", max_iter, "iteraciones.")
    return c, datos

# Método de Regula Falsi
def regula_falsi(funcion, a, b, tol=1e-6, max_iter=100):
    if f(a, funcion) * f(b, funcion) >= 0:
        print("El intervalo no es válido. La función debe cambiar de signo en el intervalo.")
        return None, None
    datos = []
    for i in range(max_iter):
        c = (a * f(b, funcion) - b * f(a, funcion)) / (f(b, funcion) - f(a, funcion))
        datos.append([i, a, b, c, f(a, funcion), f(b, funcion), f(c, funcion), f(a, funcion) * f(c, funcion)])
        if abs(f(c, funcion)) < tol:
            break
        elif f(a, funcion) * f(c, funcion) < 0:
            b = c
        else:
            a = c
    if f(a, funcion) * f(c, funcion) < tol:
        print(f"La raíz aproximada por Regula Falsi es: {c}")
    else:
        print("El método de Regula Falsi no converge después de", max_iter, "iteraciones.")
    return c, datos

# Método de Newton-Raphson
def newton_raphson(funcion, x0, tol=1e-6, max_iter=100):
    x = symbols('x')
    f = lambdify(x, funcion, 'numpy')
    f_diff = lambdify(x, diff(funcion, x), 'numpy')
    datos = []
    xn = x0
    for i in range(max_iter):
        fxn = f(xn)
        dfxn = f_diff(xn)
        datos.append([i, xn, fxn, dfxn, fxn / dfxn])
        if abs(fxn) < tol:
            break
        xn_nuevo = xn - fxn / dfxn
        if abs(xn_nuevo - xn) < tol:
            break
        xn = xn_nuevo
    if abs(f(xn)) < tol:
        print(f"La raíz aproximada por Newton-Raphson es: {xn}")
    else:
        print("El método de Newton-Raphson no converge después de", max_iter, "iteraciones.")
    return xn, datos

# Método de la Secante
def secante(funcion, x0, x1, tol=1e-6, max_iter=100):
    datos = []
    for i in range(max_iter):
        fx0 = f(x0, funcion)
        fx1 = f(x1, funcion)
        if fx1 - fx0 == 0:
            print("Error: La función no cambia de signo en el intervalo proporcionado.")
            return None, None
        x2 = x1 - fx1 * (x0 - x1) / (fx0 - fx1)
        if i > 0:
            error_relativo = abs((x2 - x1) / x2)
        else:
            error_relativo = None
        datos.append([x1, x0, fx1, fx0, x2, error_relativo])
        if abs(f(x2, funcion)) < tol:
            break
        x0, x1 = x1, x2
    if abs(f(x2, funcion)) < tol:
        print(f"La raíz aproximada por Secante es: {x2}")
    else:
        print("El método de Secante no converge después de", max_iter, "iteraciones.")
    return x2, datos

# Función para graficar una función matemática en un intervalo dado
def graficar_funcion(funcion, a, b, raiz=None):
    x_vals = np.linspace(a, b, 100)
    y_vals = [f(x_i, funcion) for x_i in x_vals]
    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, y_vals)
    plt.axhline(0, color='black')
    if raiz is not None:
        plt.axvline(raiz, color='red', linestyle='--', label='Raíz')
        plt.plot(raiz, f(raiz, funcion), 'ro')
    plt.title(f"Gráfica de la función: {funcion}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()
    plt.show()

# Función principal que muestra un menú interactivo
def menu_principal(opcion):
    if os.getenv('CI'):
        print(f"Seleccionando automáticamente la opción {opcion} en entorno CI/CD")
    while True:
        print("\nMenú Principal:")
        print("1. Método de Bisección")
        print("2. Método de Regula Falsi")
        print("3. Método de Newton-Raphson")
        print("4. Método de Secante")
        print("5. Salir")
        
        if not os.getenv('CI'):
            opcion = input("Seleccione un método (1-5): ")
        
        if opcion == '1':
            print("\nMétodo de Bisección:")
            funcion = input("Ingrese la función (use x como variable): ")
            a = float(input("Ingrese el límite inferior del intervalo: "))
            b = float(input("Ingrese el límite superior del intervalo: "))
            raiz, datos = biseccion(funcion, a, b)
            if raiz is not None:
                print("\nTabla de iteraciones:")
                headers = ["a", "b", "Xr", "f(Xa)", "f(Xr)", "f(a)*f(r)", "Aproximación"]
                print(tabulate(datos, headers=headers, floatfmt=".6f"))
                graficar_funcion(funcion, a, b, raiz)
        
        elif opcion == '2':
            print("\nMétodo de Regula Falsi:")
            funcion = input("Ingrese la función (use x como variable): ")
            a = float(input("Ingrese el límite inferior del intervalo: "))
            b = float(input("Ingrese el límite superior del intervalo: "))
            raiz, datos = regula_falsi(funcion, a, b)
            if raiz es not None:
                print("\nTabla de iteraciones:")
                headers = ["Iteración", "a", "b", "xr", "f(a)", "f(b)", "f(xr)", "f(a)*f(xr)"]
                print(tabulate(datos, headers=headers, floatfmt=".6f"))
                graficar_funcion(funcion, a, b, raiz)
        
        elif opcion == '3':
            print("\nMétodo de Newton-Raphson:")
            funcion = input("Ingrese la función (use x como variable): ")
            x0 = float(input("Ingrese el valor inicial x0: "))
            raiz, datos = newton_raphson(funcion, x0)
            if raiz es not None:
                print("\nTabla de iteraciones:")
                headers = ["Iteración", "xn", "f(xn)", "f'(xn)", "f(xn)/f'(xn)"]
                print(tabulate(datos, headers=headers, floatfmt=".6f"))
                a = x0 - 1 if x0 > 1 else 0
                b = x0 + 1 if x0 < 0 else x0 + 1
                graficar_funcion(funcion, a, b, raiz)
        
        elif opcion == '4':
            print("\nMétodo de Secante:")
            funcion = input("Ingrese la función (use x como variable): ")
            x0 = float(input("Ingrese el valor inicial x0: "))
            x1 = float(input("Ingrese el valor inicial x1: "))
           

