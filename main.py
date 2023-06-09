import pandas as pd
from helpers.crearTablasHTML import crearTabla

todos = pd.read_csv('./data/Siembras.csv')
tablaSantaFeA = pd.DataFrame()
# tablaCaucasia = pd.DataFrame()
# tablaBelmira = pd.DataFrame()
# tablaBello = pd.DataFrame()
# tablaCaramanta = pd.DataFrame()

#FILTRO1
print("FILTRO 1")
SantaFeAntioquia = todos.dropna(how='all').query('Ciudad=="Santa Fe de Antioquia"')
Filtro1 = SantaFeAntioquia.query('Arboles>250')
print(Filtro1)
print("<=================================================================================>")
#FILTRO2
print("FILTRO 2")
Filtro2 = todos.dropna(how='all').query('Ciudad=="Caucasia"')
print(Filtro2)
print("<=================================================================================>")
#Filtro3
print("FILTRO 3")
Filtro3 = todos.dropna(how='all').query('Vereda=="Rio Arriba" or Vereda=="La Salazar"')
print(Filtro3)
print("<=================================================================================>")
#Filtro4
print("FILTRO 4")
Filtro4             = todos.dropna(how='all').query('Vereda=="Quitasol" and Ciudad=="Bello"')
#ArbolesHectareas    = Filtro4['Arboles', 'Hectareas'] 
print(Filtro4)
print("<=================================================================================>")
#Filtro5
print("FILTRO 5")
CiudadCaramanta = todos.dropna(how='all').query('Ciudad=="Caramanta"')
Filtro5         = CiudadCaramanta.dropna(how='all').query('Arboles>100')
print(Filtro5)
print("<=================================================================================>")
#Filtro6
print("FILTRO 6")
Filtro6 = todos.dropna(how='all').query('Ciudad=="Yarumal" and Vereda=="Mallarino"')
print(Filtro6)
print("<=================================================================================>")

#Crear tablas

crearTabla(Filtro1,"Filtro1")
crearTabla(Filtro2,"Filtro2")
crearTabla(Filtro3,"Filtro3")
crearTabla(Filtro4,"Filtro4")
crearTabla(Filtro5,"Filtro5")
crearTabla(Filtro6,"Filtro6")

"""
#EFECTUANDO FILTROS CON PYTHON

#1. DEFINIR UNA CONDICION LOGICA
empleadosJovenesAnalistas1=tabla3.query('cargo=="analista1"')
empleadosSalarioBajo=tabla3.query('salario<5000000 and cargo=="analista2"')
empleadosADespedir=tabla3.query('edad>=50')

#2. creamos la tabla html con el dataframe del filtro
crearTabla(empleadosJovenesAnalistas1,"tablaJovenes")
crearTabla(empleadosSalarioBajo,"tablabajossalarios")
crearTabla(empleadosADespedir,"tablaoportunidaddemejora")

#3. Genera gráficas
graficarPromedioSalarial(empleadosADespedir,'cargo','salario','graficajubilados')
calcularPromedioSalariosPorEdad(empleadosJovenesAnalistas1,[20,30,40,50,60],'edad','salario','graficadetortaanalisis1')

"""