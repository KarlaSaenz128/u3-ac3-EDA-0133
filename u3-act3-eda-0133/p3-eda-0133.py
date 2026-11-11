from pickle import FALSE
import pandas as pd
import matplotlib.pyplot as plt

# 1. Crear diccionario con datos de empleados
empleados = {
    'id_empleado': [101, 102, 103, 104, 105, 106],
    'nombre': ['Carlos', 'Maria', 'Jose', 'Ana', 'Luis', 'Sofia'],
    'edad': [25, 32, 28, 40, 35, 29],
    'departamento': ['Produccion', 'Calidad', 'Mantenimiento', 'Produccion', 'Calidad', 'Mantenimiento'],
    'puesto': ['Operador', 'Inspector', 'Tecnico', 'Supervisor', 'Inspector', 'Tecnico'],
    'salario': [12000, 15000, 13500, 22000, 16000, 14500],
    'antiguedad': [2, 6, 4, 12, 8, 3],
    'horas_trabajadas': [48, 40, 45, 40, 42, 48],
    'capacitaciones': [2, 5, 3, 8, 6, 4],
    'desempeno': [80, 95, 85, 98, 90, 88]
} 

print("Analisas Explorario de datos EDA")
print("Exploratoryry data analysis por Karla Saenz NC 0133")
print("5.Crear rl diccionario con 10 listas y 6 elemntos")
# 2. convierte direccionario en DataFrame
df= pd.DataFrame(empleados)
print("'n-- TABLA ORIGINAL DE EMPLEADOS---")
print(df)


# 3. Explortar losdatos a CSV
print("-+-+-+- convertir el DataFrame en archivo csv-+-+")
df.to_csv("empleados_indutria_0133.csv",
          index=FALSE,
          encoding="utf-8-sig")
