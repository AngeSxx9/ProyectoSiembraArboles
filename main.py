import pandas as pd
from helpers.crearTablasHTML import crearTabla
from helpers.crearBarras import crearBarras
from helpers.crearTortas import crearTorta
from unidecode import unidecode


todos = pd.read_csv('./data/Siembras.csv')
Yarumal = todos.dropna(how='all').query('Ciudad=="Yarumal"')
Caucasia = todos.dropna(how='all').query('Ciudad=="Caucasia"')
Belmira = todos.dropna(how='all').query('Ciudad=="Belmira"')
Bello = todos.dropna(how='all').query('Ciudad=="Bello"')
Caramanta = todos.dropna(how='all').query('Ciudad=="Caramanta"')

#FILTRO1 Encontrar todos los datos de santa fe de Antioquia donde se tengan siembras de + de 250 arboles
print("FILTRO 1")
SantaFeAntioquia = todos.dropna(how='all').query('Ciudad=="Santa Fe de Antioquia"')
Filtro1 = SantaFeAntioquia.query('Arboles>250')
print(Filtro1)
print("<=================================================================================>")



#FILTRO2 Filtrar todos los datos de Caucasia e interpretar sus estadísticas
print("FILTRO 2")
Filtro2 = todos.dropna(how='all').query('Ciudad=="Caucasia"')
print(Filtro2)
print("<=================================================================================>")



#Filtro3 Filtrar todos los datos de las veredas Rio arriba y la Salazar de Belmira

print("FILTRO 3")
Filtro3 = todos.dropna(how='all').query('Vereda=="Rio Arriba" or Vereda=="La Salazar"')
print(Filtro3)
print("<=================================================================================>")



#Filtro4 Encontrar los datos de las veredas Quitasol de Bello mostrando además las medias de cada ítem del dataframe

print("FILTRO 4")
Filtro4 = todos.dropna(how='all').query('Vereda=="Quitasol" and Ciudad=="Bello"')
print(Filtro4)
print("<=================================================================================>")



#Filtro5 Encontrar todos los datos de caramanta donde se tengan siembras de + de 100 arboles

print("FILTRO 5")
CiudadCaramanta = todos.dropna(how='all').query('Ciudad=="Caramanta"')
Filtro5 = CiudadCaramanta.dropna(how='all').query('Arboles>100')
print(Filtro5)
print("<=================================================================================>")



#Filtro6 Encontrar los datos de la vereda mallarino del municipio de Yarumal

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
crearTabla(Yarumal,"Yarumal")
crearTabla(SantaFeAntioquia,"SantaFeAntioquia")
crearTabla(Caucasia,"Caucasia")
crearTabla(Belmira,"Belmira")
crearTabla(Bello,"Bello")
crearTabla(Caramanta,"Caramanta")


#3. Genera gráficas
crearBarras(Yarumal,'Nombre comun','Arboles','Yarumal')
crearBarras(Caucasia,'Nombre comun','Arboles','Caucasia')
crearBarras(Bello,'Nombre comun','Arboles','Bello')
crearTorta(SantaFeAntioquia,SantaFeAntioquia['Nombre comun'], SantaFeAntioquia['Arboles'], 'SantaFeAntioquia')
crearTorta(Belmira,Belmira['Nombre comun'],Belmira['Arboles'],'Belmira')
crearTorta(Caramanta,Caramanta['Nombre comun'],Caramanta['Arboles'],'Caramanta')