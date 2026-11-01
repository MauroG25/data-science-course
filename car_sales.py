import pandas as pd
import matplotlib.pyplot as plt

series = pd.Series(["BMW", "Toyota", "Honda", "Ford", "Chevrolet"])

print(series)

colour_series = pd.Series(["Red", "Blue", "Green", "Black", "White"])

print(colour_series)

#dataframe
car_data = pd.DataFrame({
    "Car": series,
    "Colour": colour_series
})

print(car_data)

df = pd.read_csv("car-sales.csv")

print(df)   

df.to_csv("exported-car-sales.csv", index=False)

df2 = pd.read_csv("exported-car-sales.csv")

print(df2)

print(df.describe())

print(df.dtypes)

print(df.columns)

print(df.info())

print(df["Doors"].sum())

print(df.head(9))


