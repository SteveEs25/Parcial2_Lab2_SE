import time
import numpy as np


inicio = time.time()


num_aleatorio = np.random.normal(500, 30, 10000000)


sumatoria = np.sum(num_aleatorio, where = (num_aleatorio <= 500000))
 	


print('La sumatoria de los puntos es: ' + str(sumatoria))
print('Duracion: {} segundos'.format(time.time() - inicio))
