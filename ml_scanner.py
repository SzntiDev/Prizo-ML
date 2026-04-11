import pandas as pd

pd.set_option('display.max_colwidth', None)
df = pd.read_csv("productos_ml.csv", encoding="utf-8-sig", dtype={'Precio': str})

#limpieza de precios
df["Precio_Num"] = pd.to_numeric(df["Precio"].str.replace(".", "", regex=False), errors='coerce')

#eliminar duplicados
df.sort_values("Precio_Num", inplace=True)
df.drop_duplicates(subset=['Título'], keep='first', inplace=True)

price_column = df["Precio_Num"] 

print("--- Estadísticas Reales (Sin duplicados) ---")
print(f"Total de productos únicos: {len(df)}")
print(f"Precio Promedio: ${round(price_column.mean(), 2)}")

if not price_column.dropna().empty:
    idx_min = price_column.idxmin()
    idx_max = price_column.idxmax()

    print("\n--- PRODUCTO MÁS BARATO ---")
    print(df.loc[idx_min, ["Título", "Precio", "Link"]])

    print("\n--- PRODUCTO MÁS CARO ---")
    print(df.loc[idx_max, ["Título", "Precio", "Link"]])

df.to_excel(
    "productos_ml.xlsx",
    index=False
)