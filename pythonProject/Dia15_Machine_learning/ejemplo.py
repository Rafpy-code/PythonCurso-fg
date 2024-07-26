import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
 
# datos
x = [1, 2, 3, 4]
y = [10, 20, 30, 40]
 
# procesar datos con Numpy y Pandas
valores = pd.Series(y, index=x)
media = valores.mean()
 
# crear gráfico de líneas con Matplotlib
plt.plot(x, y)
plt.axhline(media, 
            color='r', 
            linestyle='dashed', 
            linewidth=2)
plt.title('Gráfico de líneas')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.show()