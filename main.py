import pandas as pd
from helpers.crearTablasHTML import crearTabla

todos = pd.read_csv('./data/Siembras.csv')
# tablaSantaFeA = pd.DataFrame()
# tablaCaucasia = pd.DataFrame()
# tablaBelmira = pd.DataFrame()
# tablaBello = pd.DataFrame()
# tablaCaramanta = pd.DataFrame()

# Yarumal=todos.query('')
Ciudades = todos['Ciudad']
# info = crearTabla(Yarumal, "TablaYarumal")
print(Ciudades)