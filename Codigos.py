import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
from sympy import symbols, diff, lambdify
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
def menu_principal(args):
    if args.opcion == '1':
        print("\nMétodo de Bisección:")
        funcion = args.funcion
        a = args.a
        b = args.b
        raiz, datos = biseccion(funcion, a, b)
        if raiz is not None:
            print("\nTabla de iteraciones:")
            headers = ["a", "b", "Xr", "f(Xa)", "f(Xr)", "f(a)*f(r)", "Aproximación"]
            print(tabulate(datos, headers=headers, floatfmt=".6f"))
            graficar_funcion(funcion, a, b, raiz)
    
    elif args.opcion == '2':
        print("\nMétodo de Regula Falsi:")
        funcion = args.funcion
        a = args.a
        b = args.b
        raiz, datos = regula_falsi(funcion, a, b)
        if raiz is not None:
            print("\nTabla de iteraciones:")
            headers = ["Iteración", "a", "b", "xr", "f(a)", "f(b)", "f(xr)", "f(a)*f(xr)"]
            print(tabulate(datos, headers=headers, floatfmt=".6f"))
            graficar_funcion(funcion, a, b, raiz)
    
    elif args.opcion == '3':
        print("\nMétodo de Newton-Raphson:")
        funcion = args.funcion
        x0 = args.x0
        raiz, datos = newton_raphson(funcion, x0)
        if raiz is not None:
            print("\nTabla de iteraciones:")
            headers = ["Iteración", "xn", "f(xn)", "f'(xn)", "f(xn)/f'(xn)"]
            print(tabulate(datos, headers=headers, floatfmt=".6f"))
            a = x0 - 1 if x0 > 1 else 0
            b = x0 + 1 if x0 < 0 else x0 + 1
            graficar_funcion(funcion, a, b, raiz)
    
    elif args.opcion == '4':
        print("\nMétodo de Secante:")
        funcion = args.funcion
        x0 = args.x0
        x1 = args.x1
        raiz, datos = secante(funcion, x0, x1)
        if raiz is not None:
            print("\nTabla de iteraciones:")
            headers = ["x1", "x0", "f(x1)", "f(x0)", "x2", "Error Relativo"]
            print(tabulate(datos, headers=headers, floatfmt=(".6f", ".6f", ".6f", ".6f", ".6f", ".6e")))
            a = min(x0, x1)
            b = max(x0, x1)
            graficar_funcion(funcion, a, b, raiz)
    
    elif args.opcion == '5':
        print("Saliendo del programa...")
    
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Programa para encontrar raíces de funciones utilizando varios métodos.")
    parser.add_argument('--opcion', type=str, required=True, help='Método de resolución (1-5)')
    parser.add_argument('--funcion', type=str, required=False, help='Función matemática a resolver')
    parser.add_argument('--a', type=float, required=False, help='Extremo inferior del intervalo (para métodos de Bisección y Regula Falsi)')
    parser.add_argument('--b', type=float, required=False, help='Extremo superior del intervalo (para métodos de Bisección y Regula Falsi)')
    parser.add_argument('--x0', type=float, required=False, help='Valor inicial x0 (para métodos de Newton-Raphson y Secante)')
    parser.add_argument('--x1', type=float, required=False, help='Valor inicial x1 (para método de Secante)')
    args = parser.parse_args()
    menu_principal(args)

