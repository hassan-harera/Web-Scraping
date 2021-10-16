from google_images_download import google_images_download
import pandas as pd

response = google_images_download.googleimagesdownload()

products = pd.read_csv("products.csv")
for product in range(0, len(products)):
    arguments = {"keywords":
                     str(products.iloc[product, 1]),
                 "limit": 20, "print_urls": True
                 }
    paths = response.download(arguments)
    print(paths)
