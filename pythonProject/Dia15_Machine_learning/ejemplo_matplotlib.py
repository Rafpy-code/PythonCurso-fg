'''Práctica de la librería Matplotlib
En este notebook, se desarrollarán una serie de tareas utilizando la librería Matplotlib, empleada para la visualización de datos mediante gráficos.

Se proponen y documentan posibles formas de resolver los ejercicios, pero pueden existir varias formas de lograr los mismos resultados.

Siempre es una buena idea verificar la Documentación Oficial de Matplotlib, donde es posible encontrar todo tipo de información referida a esta librería. Y si te quedas trabado, busca en Google "como hacer [algo] con Matplotlib". Hay enormes probabilidades de que esa pregunta ya haya sido respondida!

Por ejemplo, si quieres crear un gráfico con plt.subplots(), puedes buscar directamente en Google plt.subplots()
'''

# Importamos el módulo de Matplotlib como plt
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
# La siguiente linea nos permite ver los gráficos directamente al ejecutarlos en el notebook COLAB
#%matplotlib inline

# Creamos un gráfico utilizando plt.plot()
plt.plot()
plt.title("Mi Gráfico de Ejemplo plt.plot()")
plt.show()

# Graficamos una lista de números
a = [1,5,3,8,7,15]
plt.plot(a)
plt.title("Graficamos una lista de números")
plt.show()

# Creamos dos listas, x e y. Llenamos a la lista x de valores del 1 al 100.
x = list(range(101))
# Los valores de y van a equivaler al cuadrado del respectivo valor en x con el mísmo índice
y = []
for numero in x:
  y.append(numero ** 2)

# Graficamos ambas listas creadas
plt.plot(x, y)
plt.title("Graficamos dos listas, x e y")
plt.show()

# Creamos el gráfico utilizando plt.subplots()
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set(title='Gráfico utilizando plt.subplots()',
       xlabel='Eje X',
       ylabel='Eje Y')
plt.show()

# Veamos cómo sería un flujo de trabajo en Matplotlib
# Importar y preparar la librería
import matplotlib.pyplot as plt
#%matplotlib inline

# Preparar los datos
x = list(range(101))
y = []
for numero in x:
  y.append(numero ** 2)

# Preparamos el área del gráfico (fig) y el gráfico en sí (ax) utilizando plt.subplots()
fig, ax = plt.subplots()

# Añadimos los datos al gráfico
ax.plot(x, y)

# Personalizamos el gráfico añadiendo título al gráfico y a los ejes x e y
ax.set(title='Gráfico de casos de COVID-19 en Latam', 
       xlabel='Días',
       ylabel='Casos confirmados')
plt.show()

# Guardamos nuestro gráfico empleando fig.savefig()
fig.savefig('pythonProject/Dia15_Machine_learning/ejemplo_grafico_covid.png')

#creamos un nuveo set de datos utilizando la librería Numpy
import numpy as np

x_1 = np.linspace(0, 100, 20)
y_1 = x_1**2

# Creamos el gráfico de dispersión de x vs y
fig, ax = plt.subplots()
ax.scatter(x_1, y_1)
plt.title('Creamos el gráfico de dispersión de x vs y')
plt.show()

# Visualizamos ahora la función seno, utilizando np.sin(X)
fig, ax = plt.subplots()

x_2 = np.linspace(-10, 10, 100)
y_2 = np.sin(x_2)

ax.scatter(x_2, y_2)
plt.title('Visualizamos ahora la función seno, utilizando np.sin(X)')
plt.show()

# Veamos ahora otro tipo de gráfico. Por ejemplo, un gráfico de barras, que por lo general asocia resultados numéricos a variables categóricas (categorías)

# Creemos un diccionario con tres platos y su respectivo precio
# Las claves del diccionario serán los nombres de las comidas, y los valores asociados, su precio
comidas = {'cuy': 23.75, 'yahuarlocro':8.50, 'hornado': 15}

# Crearemos un gráfico de barras donde el eje x está formado por las claves del diccionario,
# y el eje y contiene los valores.
fig, ax = plt.subplots()
ax.bar(comidas.keys(), comidas.values())

# Añadimos los títulos correspondientes
ax.set(title='Precio comidas',
       xlabel='Comidas',
       ylabel='Precio por plato')
plt.show()

# Probemos a continuación con un gráfico de barras horizontales
fig, ax = plt.subplots()
ax.barh(list(comidas.keys()),
        list(comidas.values()))
ax.set(title='Precio de las comidas',
       ylabel='Comidas',
       xlabel='Precio por plato')
plt.show()

# Un gráfico semejante es un histograma. Podemos generar números aleatorios que siguen una distribución normal (que se acumulan en torno a un valor central), con la función randn:

# Creamos una distribución de 1000 valores aleatorios distribuidos normalmente
x = np.random.randn(1000)

# Creamos el histograma
fig, ax = plt.subplots()
ax.hist(x)
plt.title('Histograma')
plt.show()

# Veamos ahora un caso más complejo, trabajando con subplots, o figuras que cotienen varios gráficos:

# Creamos una figura con 4 subgráficos (2 por fila)
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2)
                                             
# Añadimos datos a cada uno de los gráficos (axes)

# Creamos la misma disposición de gráficos, con un tamaño de figura de 10x5
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(10,5))

# Para nuestro primer gráfico, tomamos el conjunto x_1, y_1, y generamos un gráfico de líneas
ax1.plot(x_1, y_1)

# Para nuestro segundo gráfico, tomamos el conjunto x_2, y_2, y generamos un gráfico de dispersión
ax2.scatter(x_2, y_2)

# Creamos un gráfico con los precios de tres comidas en la esquina inferior izquierda
ax3.bar(comidas.keys(), comidas.values())

# El gráfico de la esquina inferior derecha será un histograma de valores aleatorios con distribución normal
ax4.hist(np.random.randn(1000))

# Mostramos los 4 gráficos
plt.show()

# Matplotlib tiene un conjunto de varios estilos disponibles, podemos verificarlos de la siguiente manera:

# Verificamos estilos disponibles
estilos_disponibles = plt.style.available
#print(estilos_disponibles)

# Cambiamos el estilo predeterminado por "seaborn-whitegrid"
plt.style.use('Solarize_Light2')

# Habiendo cambiado el estilo (el cambio más evidente que veremos será una grilla en el fondo de cada gráfico), cambiaremos también los colores de las líneas, puntos y barras en cada uno de los gráficos por códigos hex a nuestra preferencia:

# Copiamos los valores de los gráficos anteriores
# Creamos la misma disposición de gráficos, con un tamaño de figura de 10x5
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(10,5))

# Para nuestro primer gráfico, tomamos el conjunto x_1, y_1, y generamos un gráfico de líneas
ax1.plot(x_1, y_1, color='#acca03')

# Para nuestro segundo gráfico, tomamos el conjunto x_2, y_2, y generamos un gráfico de dispersión
ax2.scatter(x_2, y_2, color='#fcba03')

# Creamos un gráfico con los precios de tres comidas en la esquina inferior izquierda
ax3.bar(comidas.keys(), comidas.values(), color='#03c6fc')

# El gráfico de la esquina inferior derecha será un histograma de valores aleatorios con distribución normal
ax4.hist(np.random.randn(1000), color='#fc036b')

# Mostramos los 4 gráficos
plt.show()
