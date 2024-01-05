# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import HeatMap


print(accidents.info())

print(accidents.head())

plt.figure(figsize=(15, 10))

plt.subplot(3, 1, 1)
sns.countplot(x='road_conditions', data=accidents)
plt.title('Accidents by Road Conditions')

plt.subplot(3, 1, 2)
sns.countplot(x='weather', data=accidents)
plt.title('Accidents by Weather')

plt.subplot(3, 1, 3)
sns.countplot(x='time_of_day', data=accidents)
plt.title('Accidents by Time of Day')

plt.tight_layout()
plt.show()


map_center = [accidents['latitude'].mean(), accidents['longitude'].mean()]
accident_map = folium.Map(location=map_center, zoom_start=10)

heat_data = [[row['latitude'], row['longitude']] for index, row in accidents.iterrows()]
HeatMap(heat_data).add_to(accident_map)

accident_map.save('accident_hotspots_map.html')
