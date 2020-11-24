
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as ss
from scipy.special import ndtri
import datetime as dt

df = pd.read_csv('fronteras.csv')
Port = df['PortName']=='Laredo'
Measure = df['Measure']=='Pedestrians'
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y %H:%M')
df = df[Port & Measure]
print('\n\n\n')
#Ejercicio 1
enero = df["Date"].dt.strftime("%m") == "01"
year = df["Date"].dt.strftime("%Y").isin(["2000","2001","2002","2003","2004","2005","2006","2007","2008"])
df_enero = df[enero & year]
#print(df_enero)
df_enero.plot('Date','Value')
plt.title("Enero" , fontdict=None, loc='center', pad=None)
plt.show()

media_enero = df_enero.Value.mean()
desv_enero = df_enero.Value.std()

year_2019 = df["Date"].dt.strftime("%Y") == "2019"
df_enero_2019 = df[enero & year_2019]
hipotesis_enero = df_enero_2019.Value.mean()

valor_prueba_enero = (media_enero - hipotesis_enero)/(desv_enero/3)
print("Valor para poner en funcion de la normal en enero", valor_prueba_enero)

if (valor_prueba_enero <= .1) & (valor_prueba_enero >= -.1):
    print('La hipotesis ha sido aceptada. Con un valor para enero de 2019 de: ', valor_prueba_enero)
    signif = .1
else:
    print('La hipotesis ha sido rechazada. Con un valor para enero de 2019 de: ', valor_prueba_enero)
    signif = valor_prueba_enero

#Ejercicio 2
febrero = df["Date"].dt.strftime("%m") == "02"
df_febrero = df[febrero & year]

media_febrero = df_febrero.Value.mean()
desv_febrero = df_febrero.Value.std()

year_2019 = df["Date"].dt.strftime("%Y") == "2019"
df_febrero_2019 = df[febrero & year_2019]
hipotesis_febrero = df_febrero_2019.Value.mean()

df_febrero.plot('Date','Value')
plt.title("Febrero" , fontdict=None, loc='center', pad=None)
plt.show()

valor_prueba_febrero = (media_febrero - hipotesis_febrero)/(desv_febrero/3)
print("Valor para poner en funcion de la normal en febrero", valor_prueba_febrero)
if signif < 0:
    signif = (signif)*(-1)

if (valor_prueba_febrero <= signif) & (valor_prueba_febrero >= -signif):
    print('La hipotesis ha sido aceptada. Con un valor para febrero de 2019 de: ', valor_prueba_febrero)
    if valor_prueba_febrero < signif:
        print('El nuevo valor de significancia ahora es ', valor_prueba_febrero, 'ya que es menor al de enero')
        signif = valor_prueba_febrero
    else:
        print('El valor de significancia es el mismo que en enero', valor_prueba_febrero)
else:
    print('La hipotesis ha sido rechazada. Con un valor para febrero de 2019 de: ', valor_prueba_febrero)
    signif = valor_prueba_febrero

#Ejercicio 3
marzo = df["Date"].dt.strftime("%m") == "03"
df_marzo = df[marzo & year]

media_marzo = df_marzo.Value.mean()
desv_marzo = df_marzo.Value.std()

year_2019 = df["Date"].dt.strftime("%Y") == "2019"
df_marzo_2019 = df[marzo & year_2019]
hipotesis_marzo = df_marzo_2019.Value.mean()

df_marzo.plot('Date','Value')
plt.title("Marzo" , fontdict=None, loc='center', pad=None)
plt.show()


valor_prueba_marzo = (media_marzo - hipotesis_marzo)/(desv_marzo/3)
print("Valor para poner en funcion de la normal en marzo", valor_prueba_marzo)

if signif < 0:
    signif = (signif)*(-1)

if (valor_prueba_marzo <= signif) & (valor_prueba_marzo >= -signif):
    print('La hipotesis ha sido aceptada. Con un valor para marzo de 2019 de: ', valor_prueba_marzo)
    if valor_prueba_marzo < signif:
        print('El nuevo valor de significancia ahora es ', valor_prueba_marzo, 'ya que es menor al de febrero')
        signif = valor_prueba_marzo
    else:
        print('El valor de significancia es el mismo que en febrero', valor_prueba_marzo)
else:
    print('La hipotesis ha sido rechazada. Con un valor para  marzo de 2019 de: ', valor_prueba_marzo)



'''
Perte 2
'''
print('\n\n\n\nEjercicio parte 2\n\n\n\n')
#Ejercicio 1
enero = df["Date"].dt.strftime("%m") == "01"
year = df["Date"].dt.strftime("%Y").isin(["2002","2003","2004","2005","2006","2007","2008"])
df_enero2 = df[enero & year]
#print(df_enero2)


media_enero = df_enero2.Value.mean()
desv_enero = df_enero2.Value.std()

year_2009 = df["Date"].dt.strftime("%Y") == "2009"
df_enero_2009 = df[enero & year_2009]
hipotesis_enero = df_enero_2009.Value.mean()

df_enero.plot('Date','Value')
plt.title("Enero" , fontdict=None, loc='center', pad=None)
plt.show()

valor_prueba_enero = (media_enero - hipotesis_enero)/(desv_enero/3)
print("Valor para poner en funcion de la normal en enero", valor_prueba_enero)

if (valor_prueba_enero <= .1) & (valor_prueba_enero >= -.1):
    print('La hipotesis ha sido aceptada. Con un valor para enero de 2009 de: ', valor_prueba_enero)
    signif = .1
else:
    print('La hipotesis ha sido rechazada. Con un valor para enero de 2009 de: ', valor_prueba_enero)
    signif = valor_prueba_enero

#Ejercicio 2
febrero = df["Date"].dt.strftime("%m") == "02"
df_febrero = df[febrero & year]

media_febrero = df_febrero.Value.mean()
desv_febrero = df_febrero.Value.std()

year_2019 = df["Date"].dt.strftime("%Y") == "2019"
df_febrero_2019 = df[febrero & year_2019]
hipotesis_febrero = df_febrero_2019.Value.mean()

df_febrero.plot('Date','Value')
plt.title("Febrero" , fontdict=None, loc='center', pad=None)
plt.show()
valor_prueba_febrero = (media_febrero - hipotesis_febrero)/(desv_febrero/3)
print("Valor para poner en funcion de la normal en febrero", valor_prueba_febrero)

if signif < 0:
    signif = (signif)*(-1)
if (valor_prueba_febrero <= signif) & (valor_prueba_febrero >= -signif):
    print('La hipotesis ha sido aceptada. Con un valor para febrero de 2009 de: ', valor_prueba_febrero)
    if valor_prueba_febrero < signif:
        print('El nuevo valor de significancia ahora es ', valor_prueba_febrero, 'ya que es menor al de febrero')
        signif = valor_prueba_febrero
    else:
        print('El valor de significancia es el mismo que en enero', valor_prueba_febrero)
else:
    print('La hipotesis ha sido rechazada. Con un valor para febrero de 2009 de: ', valor_prueba_febrero)
    signif = valor_prueba_febrero

#Ejercicio 3
marzo = df["Date"].dt.strftime("%m") == "03"
df_marzo = df[marzo & year]

media_marzo = df_marzo.Value.mean()
desv_marzo = df_marzo.Value.std()

year_2019 = df["Date"].dt.strftime("%Y") == "2019"
df_marzo_2019 = df[marzo & year_2019]
hipotesis_marzo = df_marzo_2019.Value.mean()

df_marzo.plot('Date','Value')
plt.title("Marzo" , fontdict=None, loc='center', pad=None)
plt.show()

valor_prueba_marzo = (media_marzo - hipotesis_marzo)/(desv_marzo/3)
print("Valor para poner en funcion de la normal en marzo", valor_prueba_marzo)


if signif < 0:
    signif = (signif)*(-1)

if (valor_prueba_marzo <= signif) & (valor_prueba_marzo >= -signif):
    print('La hipotesis ha sido aceptada. Con un valor para marzo de 2009 de: ', valor_prueba_marzo)
    if valor_prueba_marzo < signif:
        print('El nuevo valor de significancia ahora es ', valor_prueba_marzo, 'ya que es menor al de febrero')
        signif = valor_prueba_marzo
    else:
        print('El valor de significancia es el mismo que en febrero', valor_prueba_marzo)
else:
    print('La hipotesis ha sido rechazada. Con un valor para marzo de 2009 de: ', valor_prueba_marzo)
    signif = valor_prueba_marzo
print('\n\n\n')
