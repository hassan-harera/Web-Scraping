import pandas as pd

df = pd.read_csv("spinneys.json",
                 names=["name", "unit", "price", "category", "productPictureUrl"], encoding="utf-8")

df = df["name"]

compression_opts = dict(method='zip', archive_name='products_out.csv')
df.to_csv('products_out.zip', index=False, compression=compression_opts)
