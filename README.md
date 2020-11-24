# Prueba_Hipotesis
Ejercicio del prueba de hipotesis

## Intrucciones del ejercicio
Actividad:

Trabajo en equipo y por las puertas que ya se tenía asignadas: (a nosotros nos tocó la puerta de Laredo)
1. Obtener la media de 9 años (2000,1,2,3,4,5,6,7,8) de peatones en enero, graficar (grafica de línea) y proponer 
cuál sería el ingreso en enero de 2019, a partir del valor real; esto sería la hipótesis alternativa y validarla con 
un nivel de significancia del 10%. En base al resultado determinar una nueva tolerancia, la cual puede ser 
mayor si es que no alcanzó, o menor si es que quedó sobrada.
2.Repetir el proceso pero ahora para febrero, con la tolerancia obtenida del caso anterior, generar una nueva 
hipótesis y volver a validar. La tolerancia fue efectiva?
3.Repetir el proceso para marzo ajustando la tolerancia en base al resultado del mes anterior.
4.¿Cual es la conclusión o resultados?

## Resultados
Tomamos dos muestras, en la primera tomamos los años de 2000 a 2008 y en base a eso analizamos 2019.
En esta obtuvimos que la hipotesis de enero fue rechazada ya que en nivel de tolerancia era de 0.1 y obtuvimos un valor para enero de 2019 de:  10.943638912722324, siendo este el nuevo nivel de tolerancia. Con este la hipótesis de febrero fue aceptada con un valor para febrero de 2019 de:  5.637925478415888 con el que la hipótesis de marzo tambien fue aceptada por tener un valor de:  2.789567868401843.

La segunda fue de 2002 a 2008 y analizamos el año 2009 ya que este en este periodo se presentó más constante el flujo de Pedestrians por la puerta de Laredo.
Los resultados fueron los siguentes:
La hipótesis para enero con un valor de  -4.719823235149332 fue rechazada; el nuevo valor de toleranciaes de:  -4.719823235149332
La hipotesis de febrero de 2009 también fue rechazada con un valor de:  4.9074783210944
La hipotesis en marzo fue aceptada, con un valor  de:  2.0510180636079456


## Librerías
Necesitarás las siguientes librerias y se importan de la siguiente manera

```bash
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as ss
from scipy.special import ndtri
import datetime as dt
```
## Contribuciones
Pablo Velázquez y Sofía Perznegron

## Bibliografía
"fronteras.csv"
Obtenido en:
https://www.kaggle.com/akhilv11/border-crossing-entry-data 
