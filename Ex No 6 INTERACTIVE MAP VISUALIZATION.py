# Install required libraries
import pyecharts
print(pyecharts.__version__)

import pandas as pd
from pyecharts.charts import Map
from pyecharts import options as opts
import os

# Change Directory
os.chdir(r"C:\edu\DATA VISUALIZATION")  # Set your folder path

# Read dataset
data = pd.read_excel(r"C:\Users\saran\Downloads\GDP.xlsx")
province = list(data["province"])
gdp = list(data["2019_gdp"])
data_list = [list(z) for z in zip(province, gdp)]

# Create Map Visualization
c = (
    Map(init_opts=opts.InitOpts(width="1000px", height="600px"))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="2019 Provinces GDP Distribution (Unit: 100 million yuan)"),
        visualmap_opts=opts.VisualMapOpts(max_=110000, is_piecewise=True)
    )
    .add("GDP", data_list, maptype="china")
)

# Save the map
c.render("GDP_MAP.html")
print("Map Saved Successfully ✅")
