import geopandas as gpd
import pandas as pd 
import matplotlib.pyplot as plt 


#Loading the GeoJSON data of Chicago wards
wards = gpd.read_file("/Users/wangtiles/ISTE782/ISTE782_VisualAnalytics/Chicago_HeatMap/ward_boundaries.geojson")

#Loading crime concentraion data at ward level from excel
crime_data = pd.read_excel("/Users/wangtiles/ISTE782/ISTE782_VisualAnalytics/Chicago_HeatMap/crime_conc_ward.xlsx")

#merging crim concentraion data with ward boundaries
wards_with_crime = wards.merge(crime_data, on = "Ward", how = "left")

#Plot wards colored by crime concentraion
fig, ax = plt.subplots(figsize = (10,8))
wards_with_crime.plot(column = "Crime_Concentraion", cmap = "Reds", ax = ax, legend = True)
ax.set_title("Chicago wards by Crime Concentraion")
plt.show()