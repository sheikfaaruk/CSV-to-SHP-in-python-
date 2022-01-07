import pandas as pd
import geopandas as gpd
import fiona
import matplotlib.pyplot as plt

# Read the .csv file using Pandas
airport_data = pd.read_csv('wind.csv')

# Creating GeoPandas GeoDataFrame using the Pandas Dataframe
airport_gdf = gpd.GeoDataFrame(airport_data, geometry = gpd.points_from_xy(airport_data['Nor'],airport_data['Eas'] ))
airport_gdf.plot()

#Display details AxesSubplot
airport_gdf.plot(markersize = 1.5, figsize = (10,10))

#converting .csv to .shp 
airport_gdf.to_file(filename= 'air.shp')

#Displaying .shp data in Matplotlib 
gdf = gpd.read_file('air.shp')
print(gdf.shape)
print(gdf.head())
gdf.plot()
plt.show()