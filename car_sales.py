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


## manipulate data

print(df["Make"].str.lower())

df["Make"] = df["Make"].str.lower()
print(df["Make"])



print(df)

seats = pd.Series([5, 5, 5, 5, 5])

df["Seats"] = seats

print(df)

# from a list

fuel = [5.3,4.4 ,6.2,5.9,4.8, 4.5, 5.0, 6.1, 5.7, 4.9] #from a list should be same length as the dataframe

df["fuel"] = fuel

print(df)

df["total fuel"]= df["Odometer (KM)"] /100 * df["fuel"]

print(df)

df = df.drop("total fuel", axis=1)

print(df)

#shuffle the data

df = df.sample(frac=1)

print(df)

#only select a percentage of the data

df = df.sample(frac=0.9)
print(df)

df = df.reset_index(drop=True)
print(df)