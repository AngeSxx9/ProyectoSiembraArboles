import matplotlib.pyplot as plt

def crearBarras(dataFrame, NombreComun, CantidadesArboles, nombreGrafica):
    colores=['green','red' ,'blue']
    resumenInformacion = dataFrame.groupby(NombreComun)[CantidadesArboles].mean()

    plt.bar(resumenInformacion.index, resumenInformacion,color=colores)
    plt.title(f'Resume Siembra {nombreGrafica}')
    plt.xlabel('Nombre Común')
    plt.ylabel('Cantidades Arboles')
    plt.savefig(f'./assets/imgs/{nombreGrafica}.png')

    # Ajustar el tamaño de la figura
    plt.figure(figsize=(10, 6))

    # Establecer manualmente los nombres de las etiquetas en el eje x
    plt.xticks(range(len(NombreComun)), NombreComun, rotation=45, ha='right')

    # Optimizar el espaciado de la gráfica
    plt.tight_layout()

    # Mostrar la gráfica
    # plt.show()
