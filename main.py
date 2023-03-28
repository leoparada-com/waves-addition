import numpy as np
import matplotlib.pyplot as plt

# Frecuencias de los 4 tonos
f1 = 440 # La
f2 = 523 # Do
f3 = 659 # Mi
f4 = 880 # La

# Duración de cada tono en segundos
duration = 0.01

# Cantidad de puntos por segundo
sampling_freq = 44100

# Generamos los 4 tonos puros
t = np.linspace(0, duration, int(duration * sampling_freq), False)
tone1 = np.sin(f1 * 2 * np.pi * t)
tone2 = np.sin(f2 * 2 * np.pi * t)
tone3 = np.sin(f3 * 2 * np.pi * t)
tone4 = np.sin(f4 * 2 * np.pi * t)

# Sumamos los 4 tonos
sum_tones = tone1 + tone2 + tone3 + tone4

# Creamos la figura y los ejes
fig, ax = plt.subplots()

# Graficamos los 4 tonos y la suma
ax.plot(t, tone1, color='red', label='Tono 1')
ax.plot(t, tone2, color='green', label='Tono 2')
ax.plot(t, tone3, color='blue', label='Tono 3')
ax.plot(t, tone4, color='orange', label='Tono 4')
ax.plot(t, sum_tones, color='black', label='Suma')

# Configuramos los ejes y la leyenda
ax.set_xlabel('Tiempo (segundos)')
ax.set_ylabel('Amplitud')
ax.legend(loc='upper right')

# Mostramos la gráfica
plt.show()
