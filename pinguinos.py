import pandas as pd 
import matplotlib.pyplot as  plt 
import seaborn as sns 


penguins = sns.load_dataset('penguins')
flights = sns.load_dataset('flights')
titanic = sns.load_dataset('titanic')
car_crashes = sns.load_dataset('car_crashes')
fmri = sns.load_dataset('fmri')
diamonds = sns.load_dataset('diamonds')


#Preparacion de datos 

agrupacion_pinguinos = penguins [ ['species' , 'bill_length_mm']].groupby('species').mean().reset_index()

cantidad_vuelos =  flights [['year', 'passengers']].astype({'year': 'string'}).groupby('year').sum().reset_index()


#crear grafico de barras

plt.bar(agrupacion_pinguinos['species'],agrupacion_pinguinos['bill_length_mm'])
plt.title("pinguinos promedio por especie")
plt.show()


#crear grafico lineal 

plt.plot(cantidad_vuelos['year'], cantidad_vuelos['passengers'])
plt.title('Total de pasajeros por año')
plt.show()


