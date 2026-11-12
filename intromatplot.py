import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Simple Plot")
plt.show()

fig, ax = plt.subplots()
ax.plot(x, y)
