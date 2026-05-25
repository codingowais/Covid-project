import numpy as np
import matplotlib.pyplot as plt

import random 

days = np.arange(1,31)

daily_cases = np.random.randint(500,1000,size = 30)
daily_recovered = np.random.randint(200,400,size = 30)
daily_deaths = np.random.randint(100,250,size = 30)

total_cases = np.sum(daily_cases)
total_recovered = np.sum(daily_recovered)
total_deaths = np.sum(daily_deaths)
total_active = total_cases - total_recovered - total_deaths


print(total_cases)
print(total_recovered)
print(total_deaths)
print(total_active)

plt.figure(figsize =(10,5))

plt.subplot(1,2,1)
plt.plot(days,daily_cases,marker = 'o',label = "Daily cases")
plt.plot(days,daily_recovered,marker = 'o',label = "Daily recovered")
plt.plot(days,daily_deaths,marker = 'o',label = "Daily deaths")
plt.legend(loc ='upper right')
plt.grid(color ='gray',linestyle ='--',linewidth = '0.5')
plt.title("Covid Case Report",loc ='left',fontsize =15,pad = 20)
plt.xlabel("Number of days",fontsize = 10)
plt.ylabel("Number of cases",fontsize = 10)
plt.ylim(0,1200)

plt.subplot(1,2,2)
label = ['Recovered','Deaths','Active']
values = [total_recovered,total_deaths,total_active]
plt.pie(values ,labels = label , colors = ["blue","orange","skyblue"],autopct= '%1.1f%%')
plt.title("Covid case report")


plt.tight_layout()
plt.show()
