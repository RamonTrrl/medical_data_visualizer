
import pandas as pd
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
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

#4-Ejecución del gráfico
 #-creaciíon de función para el gráfico categórico
def draw_cat_plot():
 
 #-creación de la función larga (melt)
    df_cat = pd.melt(df,
                    id_vars=['cardio'],
                    value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    
 #-agrupamos y contamos
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

 #-dibujamos el catplot
    fig = sns.catplot(x='variable', y='total', hue='value', col= 'cardio', data=df_cat, kind='bar', height=5, aspect=1)

 #-extraer la figura del matplotlib y devoverla
    fig = fig.fig
    return fig

if __name__ == "__main__":

   import matplotlib.pyplot as plt
   #fig = draw_cat_plot ()
   #plt.show()
   if __name__ == "__main__":
    fig = draw_cat_plot()
    fig.savefig('catplot.png')   # Guardamos en nuestro explorado de archivos de code space
    print("Gráfico guardado como 'catplot.png'")









