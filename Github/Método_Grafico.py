import matplotlib.pyplot as plt
import numpy as np

print("Bienvenido al metodo grafico\n")
def graficar_funcion():
    try:
        # Solicitar entrada de usuario
        funcion = input("Ingrese la función (use x como variable): ")
        xmin = float(input("Ingrese el valor mínimo del intervalo: "))
        xmax = float(input("Ingrese el valor máximo del intervalo: "))
        puntos = int(input("Ingrese el número de puntos (mayor que 1): "))
        
        # Validar entrada del usuario
        if puntos <= 1:
            print("Error: Ingrese un número de puntos mayor que 1.")
            return
        
        # Generar datos para la función
        x = np.linspace(xmin, xmax, puntos)  # Generar 'puntos' puntos entre xmin y xmax
        y = eval(funcion)  # Evaluar la función ingresada por el usuario
        
        # Graficar la función
        plt.plot(x, y)
        plt.title('Gráfico de la función ingresada')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)
        plt.show()
    
    except ValueError:
        print("Error: Ingrese números válidos para los valores y puntos.")
    except NameError:
        print("Error: Función ingresada no válida.")
    except SyntaxError:
        print("Error: Sintaxis de función no válida.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {str(e)}")

# Llamar a la función principal
graficar_funcion()
