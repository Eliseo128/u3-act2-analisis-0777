# importar librerias
import pandas as pd
import numpy as np
# Eliseo Nava NC 0777
print("Analisis de datos Alumnos  Eliseo Nava NC=0777")
print(False)
alumnos={ 
"Nombre": ["Alicia", "Pedro", "Carlos", "David", "Eva", "Frank"],
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

print("+-+-Eliseo+-+-+-+Segunda parte +-+-+0777-+-+-+")
print("Agregaciones múltiples")
print("mean --> promedio, sum --> suma")
print("max --> maximo, min --> minimo")
resultado_agregado = agrupado['Calificacion'].agg(['mean', 'sum', 'max', 'min'])
print(resultado_agregado)
print("Agrupación por varias columnas")
print("Agrega columna al dataframe ")
print("columna Team --> Equipo  ")
df['Equipo'] = ['A','B','A','B','A','B']
agrupado_múltiple = df.groupby(['Especialidad', 'Equipo'])['Calificacion'].mean()
print(agrupado_múltiple)

