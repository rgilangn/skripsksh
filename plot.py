import pandas as pnd 
import matplotlib.pyplot as plt

data = pnd.read_csv('dataResult/BBR_LL_SK1.csv')

prin = data.iloc[1:, 7]

print(prin)
plt.plot(prin)
plt.ylabel('Window Size Value')
plt.xlabel('Time')
plt.autoscale(enable=True, axis='x',tight=True)
plt.grid()
plt.show()

plt.savefig('picResult/BBR_LL_SK1.png')

