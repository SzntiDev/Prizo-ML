import pandas as pd

df = pd.read_csv("productos_ml.csv", sep=",", encoding="utf-8", decimal=".")


print(df.info())
print(df.describe())

title_column = df["Título"]
link_column = df["Link"]
price_column = df["Precio"]

price_column.astype()
