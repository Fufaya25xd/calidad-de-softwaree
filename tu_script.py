import pandas as pd
import matplotlib.pyplot as plt

def leer_datos(ruta_archivo):
    """Lee datos de un archivo CSV."""
    datos = pd.read_csv(ruta_archivo)
    return datos

def procesar_datos(datos):
    """Realiza cálculos simples con los datos."""
    datos['Promedio'] = datos.mean(axis=1)
    return datos

def generar_grafico(datos, columna, salida_grafico):
    """Genera un gráfico de la columna especificada y guarda como imagen."""
    plt.figure(figsize=(10, 6))
    plt.plot(datos[columna])
    plt.title(f'Gráfico de {columna}')
    plt.xlabel('Índice')
    plt.ylabel(columna)
    plt.savefig(salida_grafico)

def main():
    ruta_archivo = 'datos.csv'
    salida_grafico = 'grafico.png'

    # Leer datos
    datos = leer_datos(ruta_archivo)
    
    # Procesar datos
    datos_procesados = procesar_datos(datos)
    
    # Generar gráfico
    generar_grafico(datos_procesados, 'Promedio', salida_grafico)
    
if __name__ == "__main__":
    main()
