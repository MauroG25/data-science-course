import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


heart_disease = pd.read_csv("heart-disease.csv")

print(heart_disease.head())

heart_disease["age"].plot(kind= "hist")
plt.show()

heart_disease.plot.hist(figsize=(10,30), subplots=True)
plt.show()

over50 = heart_disease[heart_disease["age"]>50]
fig, ax = plt.subplots(figsize=(10,6))
over50.plot(kind='scatter',
            x='age',
            y='chol',
            c='target',
            ax=ax)

plt.show()

fig, (ax0,ax1) =plt.subplots(nrows=2,
                             ncols=1,
                             figsize= (10,10))

scatter = ax0.scatter(x=over50["age"],
                      y=over50["chol"],
                      c=over50["target"])

scatter = ax1.scatter(x=over50["age"],
                      y=over50["thalach"],
                      c=over50["target"])

plt.show()
##