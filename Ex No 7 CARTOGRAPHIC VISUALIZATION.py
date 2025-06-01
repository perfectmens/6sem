import geopandas as gpd
import matplotlib.pyplot as plt

# File Path
fp = r"c:\edu\DATA VISUALIZATION\India_State_Boundary.shp"

# Read Shapefile
map_df = gpd.read_file(fp)
print(map_df.head())

# Plotting
map_df.plot(figsize=(12, 10), color='lightblue', edgecolor='black')
plt.title("India State Boundary Map")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.grid(True)
plt.show()
