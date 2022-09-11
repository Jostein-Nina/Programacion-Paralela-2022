#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hola Mundo");


# In[2]:


a=8+5;
print(a);


# In[3]:


import datetime
hora_fecha_actual =datetime.datetime.now()

print(hora_fecha_actual)

hora = hora_fecha_actual.time()
fecha = hora_fecha_actual.date()

print(hora)
print(fecha)

print("Hora: ",hora.hour,"Minuto: ",hora.minute,"Segundo: ",hora.second)
print(fecha.year, fecha.month, fecha.day)


# In[4]:


import multiprocessing as mp
print("Número de procesadores: ", mp.cpu_count())


# In[5]:


import numpy as np
from time import time
np.random.RandomState(100)
arr = np.random.randint(0, 10, size=[200000, 5])
data = arr.tolist()
data[:5]


# In[15]:


import pandas as pd
import numpy as np
import multiprocessing

#Se define la función
def suma_acumulada(number):
    return sum(range(1, number + 1))

valores = [10**8, 10**8, 10**8, 10**8, 10**8]


# In[16]:


get_ipython().run_cell_magic('time', '', 'resultados = []\n\nfor valor in valores:\n    resultado = suma_acumulada(valor)\n    resultados.append(resultado)\n\nresultados')


# In[ ]:


get_ipython().run_cell_magic('time', '', '\n# Aplicar la función sobre cada elemento en paralelo\npool = multiprocessing.Pool(processes=multiprocessing.cpu_count())\nresultados = pool.map(suma_acumulada, valores)\nresultados')


# In[ ]:


import threading  
import time  
  
  
def worker(num):  
    time.sleep(1)  
    print("The num is  %d" % num)  
    print(t.getName()  )
    return  
  
for i in range(20):  
    t = threading.Thread(target=worker, args=(i,), name="testThread")  
    t.start()


# In[ ]:




