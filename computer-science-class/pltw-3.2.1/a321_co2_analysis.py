import matplotlib.pyplot as plt
import pandas as pd
import math

co2_data = pd.read_csv("pltw-3.2.1\\co2_data.csv", header=0)
print(co2_data)#view default
co2_data['Average'] = co2_data['Average'].replace(-99.99, math.nan)
print(co2_data)#view after replaceing
co2_data.dropna(subset=['Average'], inplace=True)
print(co2_data)#view droping effect
plt.plot(co2_data['Year'], co2_data['Average'], color='red')
plt.ylabel('co2 Anomalies in Celsius')
plt.xlabel('Years')
plt.title('Change in co2')
plt.show()