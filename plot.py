import pandas as pnd 
import matplotlib.pyplot as plt

data = pnd.read_csv('dataResult/CUBIC_LL_SK2.csv')

x = data.iloc[1:, 1]
y = data.iloc[1:, 7]
print(x)
print(y)
plt.plot(x,y)
plt.ylabel('Window Size Value')
plt.xlabel('Time')
plt.autoscale(enable=True, axis='x',tight=True)
plt.grid()
plt.show()

#plt.savefig('picResult/BBR_LL_SK2.png')

