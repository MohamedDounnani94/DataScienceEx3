# LEGGE DEI GRANDI NUMERI, CALCOLARE LA MEDIA TRA N NUMERI GENERATI RANDOMICAMENTE TRA 1 E 10
import inline as inline
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

results = []

for n in range(1, 10000):
    # generazione numeri casuali da 1 a 10
    nums = np.random.randint(low=1, high=10, size=n)
    # calcolo media
    mean = nums.mean()
    results.append(mean)

# creazione dataframe delle medie raccolte
df = pd.DataFrame({'means': results})

# stampare le prima osservazioni
print df.head()

# stampare le ultime osservazioni -> piu i numeri crescono piu la media e' stabile, legge dei grandi numeri
print df.tail()

df.plot(title='Law of Large Numbers')
plt.xlabel("Number of throws in sample")
plt.ylabel("Average of Sample")
plt.show()