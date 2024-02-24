# Step 1: Import libraries
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Step 2: Load crime data from Excel
crime_data = pd.read_excel("/Users/wangtiles/ISTE782/ISTE782_VisualAnalytics/Chicago_HeatMap/crime_conc_ward.xlsx")

# Step 3: Load GeoJSON file
geojson_file = "/Users/wangtiles/ISTE782/ISTE782_VisualAnalytics/Chicago_HeatMap/ward_boundaries.geojson"
geo_data = gpd.read_file(geojson_file)

# Step 4: Convert 'ward' column in geo_data to int64
geo_data['ward'] = geo_data['ward'].astype('int64')

# Step 5: Convert 'Ward' column in crime_data to int64
crime_data['Ward'] = crime_data['Ward'].astype('int64')

# Step 6: Merge crime data with GeoDataFrame
merged_data = geo_data.merge(crime_data, how='left', left_on='ward', right_on='Ward')

# Step 7: Visualize the heatmap
fig, ax = plt.subplots(1, 1, figsize=(10, 10))
merged_data.plot(column='Crime_Concentration', cmap='Reds', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)

# Defining the ward numbers selected with special highlighting
highlight_ward_numbers = [3, 46, 1, 25, 34]

# Add ward numbers to the center of each ward
for idx, row in merged_data.iterrows():
    ward_number = row['ward']
    centroid = row['geometry'].centroid
    color = 'green' if ward_number in highlight_ward_numbers else 'black'
    ax.text(centroid.x, centroid.y, str(ward_number), fontsize=8, ha='center', va='center', color=color)

plt.title('Crime Concentration Heatmap by Ward')
plt.show()
