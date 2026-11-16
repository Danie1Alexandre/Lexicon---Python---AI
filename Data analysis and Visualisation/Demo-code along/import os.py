import os
import pandas as pd

# Hittar filen automatiskt och öppnar den med fullständig sökväg
for root, dirs, files in os.walk("."):
    if "listings.csv" in files:
        full_path = os.path.abspath(os.path.join(root, "listings.csv"))
        print("Öppnar:", full_path)
        listings_raw = pd.read_csv(full_path)
        break