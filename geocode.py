import pandas as pd
from geopy.geocoders import Nominatim
import time

# Function to geocode counties
def geocode_county(county_name, state_name):
    geolocator = Nominatim(user_agent="your_app_name")
    location = geolocator.geocode(f"{county_name}, {state_name}")
    if location:
        return location.latitude, location.longitude
    return None, None

# Load the data
file_path = r'C:\Users\LENOVO\OneDrive - Texas State University\Desktop\Texas_EV\counties-ev.xlsx'
df = pd.read_excel(file_path)

# Filter out the 'Grand Total' row
df = df[df['County'] != 'Grand Total']

# Initialize latitude and longitude columns
df['Latitude'] = None
df['Longitude'] = None

state_name = 'Texas'  # Assuming all counties are in Texas

# Geocode counties
for i, row in df.iterrows():
    latitude, longitude = geocode_county(row['County'], state_name)
    df.at[i, 'Latitude'] = latitude
    df.at[i, 'Longitude'] = longitude
    time.sleep(1)  # To avoid hitting the geocoding API rate limit

# Save the geocoded data to a new CSV file
output_file_path = 'county_ev.csv'
df.to_csv(output_file_path, index=False)

print(f"Geocoded data saved to {output_file_path}")
