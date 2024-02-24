# import geopandas as gpd
# import pandas as pd 
# import matplotlib.pyplot as plt 


# #Loading the GeoJSON data of Chicago wards
# wards = gpd.read_file("/Users/wangtiles/ISTE782/ISTE782_VisualAnalytics/Chicago_HeatMap/ward_boundaries.geojson")

# #Loading crime concentraion data at ward level from excel
# crime_data = pd.read_excel("/Users/wangtiles/ISTE782/ISTE782_VisualAnalytics/Chicago_HeatMap/crime_conc_ward.xlsx")

# #merging crim concentraion data with ward boundaries
# wards_with_crime = wards.merge(crime_data, on = "Ward", how = "left")

# #Plot wards colored by crime concentraion
# fig, ax = plt.subplots(figsize = (10,8))
# wards_with_crime.plot(column = "Crime_Concentraion", cmap = "Reds", ax = ax, legend = True)
# ax.set_title("Chicago wards by Crime Concentraion")
# plt.show()



# Step 1: Import libraries
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Step 2: Load crime data from Excel
crime_data = pd.read_excel("/Users/wangtiles/ISTE782/ISTE782_VisualAnalytics/Chicago_HeatMap/crime_conc_ward.xlsx")

# Step 3: Load GeoJSON file
geojson_file = "/Users/wangtiles/ISTE782/ISTE782_VisualAnalytics/Chicago_HeatMap/ward_boundaries.geojson"
geo_data = gpd.read_file(geojson_file)

# Step 4: Merge crime data with GeoDataFrame
merged_data = geo_data.merge(crime_data, how='left', left_on='ward', right_on='Ward')

# Step 5: Visualize the heatmap
fig, ax = plt.subplots(1, 1, figsize=(10, 10))
merged_data.plot(column='Crime_Concentration', cmap='Reds', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)
plt.title('Crime Concentration Heatmap by Ward')
plt.show()
