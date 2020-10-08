import time
import numpy as np


inicio = time.time()
sumatoria = 0

num_aleatorio = np.random.normal(500, 30, 10000000)


for numeros in num_aleatorio:
	if int(numeros) <= 500000:
		sumatoria = int(sumatoria) + int(numeros)



print('La sumatoria de los puntos es: ' + str(sumatoria))
print('Duracion: {} segundos'.format(time.time() - inicio))

