import pandas as pd
import matplotlib.pyplot as plt

def crearTorta(dataframe,NombreComun,CantidadArboles,nombreTorta):
   # Agrupar por nombre común y sumar las cantidades de árboles
    agrupado = dataframe.groupby('Nombre comun')['Arboles'].sum().reset_index()

    # Obtener los nombres comunes y las cantidades de árboles
    nombre_comun = agrupado['Nombre comun']
    cantidad_arboles = agrupado['Arboles']

    # Crear la gráfica de torta
    plt.figure()
    plt.pie(cantidad_arboles, labels=nombre_comun, autopct='%1.1f%%')

    plt.title('Distribución de Árboles Plantados')

    plt.savefig(f'./assets/imgs/{nombreTorta}.png')
    plt.close()  # Cerrar la figura para liberar memoria