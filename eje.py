import pandas as pd

# DataFrame de alumnos
alumnos = {
    'id': [1, 2, 3, 4, 5],
    'nombre': ['Ana', 'Luis', 'Maria', 'Pedro', 'Sofia'],
    'grupo': ['4A', '4A', '4B', '4B', '4A']
}

df_alumnos = pd.DataFrame(alumnos)

# DataFrame de calificaciones
calificaciones = {
    'id': [1, 2, 3, 4, 5],
    'materia': ['Python', 'Python', 'Python', 'Python', 'Python'],
    'calificacion': [95, 80, 90, 70, 100]
}

df_calificaciones = pd.DataFrame(calificaciones)

# Fusionar los DataFrames
df_final = pd.merge(
    df_alumnos,
    df_calificaciones,
    on='id',
    how='inner'
)

# Mostrar resultado
print(df_final)