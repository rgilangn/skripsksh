import pandas as pnd 
import matplotlib.pyplot as plt

dataB = pnd.read_csv('dataResult/BBR_LL_SK2.csv')
dataC = pnd.read_csv('dataResult/CUBIC_LL_SK2.csv')
dataL = pnd.read_csv('dataResult/ledbat_LL_SK2.csv')


xB = dataB.iloc[1:, 1]
yB = dataB.iloc[1:, 7]
xC = dataC.iloc[1:, 1]
yC = dataC.iloc[1:, 7]
xL = dataL.iloc[1:, 1]
yL = dataL.iloc[1:, 7]

plt.figure(figsize=(14,7), dpi=150)
plt.plot(xB,yB,)
plt.plot(xC,yC)
plt.plot(xL,yL)
plt.ylabel('Window Size Value')
plt.xlabel('Time')
plt.autoscale(enable=True, axis='x',tight=True)
plt.legend(['BBR', 'Cubic', 'Ledbat'])

#plt.savefig('picResults/ledbat_LL_SK2.png')
plt.show()

