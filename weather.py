# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

#Load weather data From .txt file in the same Dictonarie
data_arr = np.loadtxt("SBEns_03.03.18_month.txt",skiprows = 5)
np.savetxt("data.txt",data_arr,delimiter=" ")



#TXX: max. Temp. 2 meter over soil
txx = data_arr[0:len(data_arr),6]
#RR: Total Rainfalls
rr = data_arr[0:len(data_arr),10]
#Column Numbers as x-axes
x = np.arange(1,len(data_arr)+1,1)

#Plot Temprature
fig , ax1 = plt.subplots()
ax1.plot(x,txx,color='red', label="Temprature" )
ax1.set_ylim(-20,40,5)
ax1.set_xlabel('Measurement')
ax1.set_ylabel('Temprature')
ax1.tick_params('y',color='red')
ax1.legend(loc = 2)
#Plot Rainfalls
ax2 = ax1.twinx()
ax2.scatter(x,rr,color = 'blue',marker='.',label="Rainfalls")
ax2.set_ylabel('Rainfalls')
ax2.tick_params('y',color='blue')
ax2.set(title='Saarbrücken Ensheim 03.03.18')
ax2.legend()
plt.savefig('grap.png')
plt.show()