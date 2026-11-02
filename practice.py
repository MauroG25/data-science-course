import pandas as pd
import matplotlib.pyplot as plt
import random


Colors = pd.Series(["Red", "Blue", "Green", "Black", "White"])
print(Colors)


cars = pd.Series(["BMW", "Toyota", "Honda", "Ford", "Chevrolet"])
print(cars)

df = pd.DataFrame({
    "Car": cars,
    "Colour": Colors
})

print(df)

df2 = pd.read_csv("car-sales.csv")
print(df2)

print(df2.describe())

print(df2.info())

numbers = pd.Series([1, 412, 23, 425,6321, 5125])

print(numbers.mean())
print(numbers.sum())

print(len(df2))

print(df2.head(5))
print(df2.tail(5))
print(df2.head(7))

print(df2.loc[3])

print(df2.iloc[3])

print(df2["Odometer (KM)"]) 

print(df2[df2["Odometer (KM)"] > 100000])

print(pd.crosstab(df2["Make"], df2["Doors"]))

print(df2.groupby(["Make"]).mean(numeric_only=True))

df2["Odometer (KM)"].plot(kind="hist")

plt.show()

df2["Price"] = df2["Price"].str.replace('[\$\,]', '', regex=True).astype(float)
df2["Price"].plot(kind="hist")
plt.show()

df2["Make"] = df2["Make"].str.lower()

df3 = pd.read_csv("car-sales-missing-data.csv")

print(df3)

df3["Odometer"].fillna(df3["Odometer"].mean(), inplace=True)

print(df3)  

df3.dropna(inplace=True)

print(df3)

df3["Seats"] = 5

print(df3)

df3["Engine Size"] = random.uniform(1.3, 4.5)

print(df3)

df3["Price"] = df3["Price"].str.replace('[\$\,]', '', regex=True).astype(float)
df3["price per km"] = df3["Odometer"] / df3["Price"]

print(df3)

df3.drop(inplace=True, axis=1, columns=["price per km"])

print(df3)

df3 = df3.sample(frac=1)
print(df3)

df3 = df3.reset_index(drop=True)
print(df3)

df3["Odometer"] = df3["Odometer"].apply(lambda x: x / 1.60934)
print(df3)

df3["Odometer (Miles)"] = df3["Odometer"]

print(df3)

df3 = df3.drop("Odometer", axis=1)
print(df3)