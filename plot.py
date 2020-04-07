import pandas as pnd 
import matplotlib.pyplot as plt

data = pnd.read_csv('examine2_cubic_noscenario.csv')

prin = data.iloc[1:, 6]

print(prin)
plt.plot(prin)
plt.ylabel('Window Size Value')
plt.xlabel('Time')
plt.autoscale(enable=True, axis='x',tight=True)
plt.grid()
plt.show()

plt.savefig('examine2_cubic_noscenario.png')

