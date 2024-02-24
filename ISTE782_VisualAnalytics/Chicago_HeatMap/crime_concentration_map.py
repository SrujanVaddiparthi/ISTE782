# Step 1: Import libraries
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Step 2: Load crime data from Excel
crime_data = pd.read_excel("/Users/wangtiles/ISTE782/ISTE782_VisualAnalytics/Chicago_HeatMap/crime_conc_ward.xlsx")

# Step 3: Load GeoJSON file
geojson_file = "/Users/wangtiles/ISTE782/ISTE782_VisualAnalytics/Chicago_HeatMap/ward_boundaries.geojson"
geo_data = gpd.read_file(geojson_file)

# Checking for datatypes of 'ward' column in geo_data and 'Ward' column in crime_data
print("Data type of 'ward' column in geo_data:", geo_data['ward'].dtype)
print("Data type of 'Ward' column in crime_data:", crime_data['Ward'].dtype)

# Convert 'ward' column in geo_data to string
geo_data['ward'] = geo_data['ward'].astype('str')

# Convert 'Ward' column in crime_data to string
crime_data['Ward'] = crime_data['Ward'].astype('str')

# Convert 'ward' column in geo_data to int64
geo_data['ward'] = geo_data['ward'].astype('int64')

# Convert 'Ward' column in crime_data to int64
crime_data['Ward'] = crime_data['Ward'].astype('int64')

# Step 4: Merge crime data with GeoDataFrame
merged_data = geo_data.merge(crime_data, how='left', left_on='ward', right_on='Ward')

# Step 5: Visualize the heatmap
fig, ax = plt.subplots(1, 1, figsize=(10, 10))
merged_data.plot(column='Crime_Concentration', cmap='Reds', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)
plt.title('Crime Concentration Heatmap by Ward')
plt.show()
