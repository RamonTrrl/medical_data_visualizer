
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#1-Carga del data set
df = pd.read_csv('medical_examination.csv')

#print(df.head())

#2-Agregar columna de sobrepeso (overweight)
 #-Altura en metros
df['height_m'] = df['height'] / 100

 #-Calcular IMC (bmi)
df['bmi'] = df['weight'] / (df['height_m'] ** 2)


 #-Condicion de sobrepeso >25 (si=1, no=0)
df['overweight'] = (df['bmi'] >25).astype(int)

 #-Eliminar columnas usadas para calcular IMC
df.drop(['height_m', 'bmi'], axis=1, inplace=True)

print(df[['height', 'weight', 'overweight']].head())
print(df.columns)

#3-Normalizar columnas de colesterol y glucosa (0=bueno | 1=malo)
df['cholesterol'] = (df['cholestero'] > 1).astype(int)
df['glu'] = (df['glu'] > 1).astype(int)

#4-Ejecución del gráfico








