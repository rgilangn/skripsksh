import pandas as pnd 
import matplotlib.pyplot as plt

dataB = pnd.read_csv('dataResult/examine3/bbr_20000_mix_LL_.csv')
dataC = pnd.read_csv('dataResult/examine3/cubic_20000_mix_LL_.csv')
dataL = pnd.read_csv('dataResult/examine3/ledbat_20000_mix_LL_.csv')


xB = dataB.iloc[1:, 1]
yB = dataB.iloc[1:, 6]
xC = dataC.iloc[1:, 1]
yC = dataC.iloc[1:, 6]
xL = dataL.iloc[1:, 1]
yL = dataL.iloc[1:, 6]

plt.figure(figsize=(14,7), dpi=150)
plt.plot(xB,yB)
plt.plot(xC,yC)
plt.plot(xL,yL)
plt.ylabel('Window Size Value')
plt.xlabel('Time')
plt.autoscale(enable=True, axis='x',tight=True)
plt.legend(['BBR', 'Cubic', 'Ledbat'])

#plt.savefig('picResults/ledbat_LL_SK2.png')
plt.show()

