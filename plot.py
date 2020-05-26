import pandas as pnd 
import matplotlib.pyplot as plt

dataB = pnd.read_csv('dataResult/examine2/bbr_SK2_0_LL_.csv')
dataC = pnd.read_csv('dataResult/examine2/cubic_SK2_0_LL_.csv')
dataL = pnd.read_csv('dataResult/examine2/ledbat_SK2_0_LL_.csv')


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
plt.suptitle('CWND Dengan Queue Size Default. Long Lived')
#plt.savefig('picResults/ledbat_LL_SK2.png')
plt.show()

