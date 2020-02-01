import numpy as np
import matplotlib.pyplot as plt
moneyarray = 100*np.ones(100)
for i in range(30000):
    if(i%1000 == 0):
        print(i)
    for j in range(100):
        #if moneyarray[j]>0:
            moneyarray[j] = moneyarray[j] -1
            winnernumber = np.random.randint(0,100)
            moneyarray[winnernumber] = moneyarray[winnernumber]+1
moneyarray.sort()
x = np.arange(100)



plt.figure()
plt.bar(x,moneyarray)
plt.show()
