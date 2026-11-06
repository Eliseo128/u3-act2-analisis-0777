# importar librerias
import pandas as pd
import numpy as np
print("Analisis de datos Alumnos  Eliseo Nava NC=0777")

alumnos={ "Nombre": ["Alicia", "Pedro", "Carlos", "David", "Eva", "Frank"],
"Especialidad": ["Inteligencia", "Electrónica", "Mecánica", "Electrónica", "Rebotica", "Rebotica"],
"Calificacion": [90, 60, 50, 80, 40, 100],
"Edad": [14, 15, 13, 16, 18, 17]} 

df = pd.DataFrame(alumnos)
print(df)
print(" -+-+-+ Agrupar por una sola columna  especialidad-+-+-+")
agrupado= df.groupby('Especialidad')
print(agrupado)
print(" -+-+-+ promedio por especialidad-+-+-+")
# calificacion promedio por especialidad
print(agrupado['Calificacion'].mean())
print(" -+-+-+ Edad máxima-+-+-+")
# Edad máxima en cada despecialidad
print(agrupado['Edad'].max())
