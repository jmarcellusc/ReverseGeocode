import os, sys
import pandas as pd
import time
from geopy.geocoders import Nominatim, OpenCage
import googlemaps


##############################################################
def exit_program(exit_message: str):
    """Exits the Python program."""
    print(exit_message)
    sys.exit()


#############################################################
##############################################################
class DataProcessor:
    def __init__(self, export_filepath: str, export_csv_file_name: str, geocoding_service: str = "opencage"):
        self.df = None
        self.export_filepath = export_filepath
        self.export_csv_file_name = export_csv_file_name
        self.geocoding_service = geocoding_service

    ##############################################
    def run_geocoding(self, address_field_name: str):
        print(" >> Running Geocoding...")
        time.sleep(2)
        if self.geocoding_service == "opencage":
            self.run_opencage_geopy_iterator(address_field_name)
        elif self.geocoding_service == "googlemaps":
            self.run_googlemaps_iterator(address_field_name)
        else:
            print("Invalid geocoding service specified.")

    ##############################################
    def check_read_address_dataframe(self, data_filename: str, address_field_name: str) -> pd.DataFrame:
        ## Checks if the Address Field is present

        try:
            self.df = pd.read_csv(data_filename)
            if address_field_name in self.df.columns or address_field_name.lower() in self.df.columns or address_field_name.upper() in self.df.columns:
                time.sleep(1)
                print(" >> CSV File Check")
                return self.df
            else:
                print(f"Warning: CSV file '{data_filename}' does not have an 'Address' or 'address' column.")
        except FileNotFoundError:
            print(f"Error: File '{data_filename}' not found.")
        except Exception as e:
            print(f"Error: An error occurred while processing the file: {e}")

    ##############################################
    def check_and_create_lat_lon(self):
        ## Checks for 'latitude' and 'longitude' columns in the DataFrame, Creates them if they don't exist.

        if 'latitude' not in self.df.columns:
            self.df['Latitude'] = None  # Or fill with default value or calculate from other columns
            print(" >> Latitude Field Created")
        else:
            print(" >> Latitude Field Exist, Data Will be Overwritten")
        if 'longitude' not in self.df.columns:
            self.df['Longitude'] = None  # Or fill with default value or calculate from other columns
            print(" >> Longitude Field Created")
        else:
            print(" >> Longitude Field Exist, Data Will be Overwritten")

    ##############################################
    def print_console_df(self):
        ## Prints to Console DataFrame

        print(self.df.head())

    ##############################################
    def run_opencage_geopy_iterator(self, address_field_name: str):
        ## Runs through a for loop

        from Open_Cage_API_KEY import OPEN_CAGE_API_KEY

        if not OPEN_CAGE_API_KEY:
            exit_program("NO - Open Cage API Key Found")

        geolocator = OpenCage(api_key=OPEN_CAGE_API_KEY)

        for index, string_item in enumerate(self.df[address_field_name]):
            cleaned_string_item = string_item.strip()  # Trims all leading and trailing spaces
            location = geolocator.geocode(cleaned_string_item) # Revs. Geo-locates

            if location:
                self.df.loc[index, 'Latitude_OpenCage'] = str(location.latitude)
                self.df.loc[index, 'Longitude_OpenCage'] = str(location.longitude)

                # Score Method
                confidence = location.raw['confidence']
                self.df.loc[index, 'Score_OpenCage'] = confidence
            else:
                print(f"Geocoding failed for address: {cleaned_string_item}")
        time.sleep(1)
        print(" >> Process Complete")
        self.export_df_to_csv(self.export_filepath, self.export_csv_file_name)

    ##############################################
    def run_googlemaps_iterator(self, address_field_name: str):
        """
        Google Maps API Coding Location Types:

        ROOFTOP: Indicates a precise geocode for a specific building or address.
        RANGE_INTERPOLATED: Indicates an approximate location interpolated between two precise points.
        GEOMETRIC_CENTER: Indicates a location representing the center of a given area, such as a neighborhood or city.
        APPROXIMATE: Indicates an approximate location with a lower level of precision.
        """

        from Google_Map_API_Key import GMAP_API_KEY

        if not GMAP_API_KEY:
            exit_program("NO - Google Maps API Key Found")

        gmaps = googlemaps.Client(key=GMAP_API_KEY)

        for index, string_item in enumerate(self.df[address_field_name]):
            cleaned_string_item = string_item.strip()  # Trims all leading and trailing spaces
            geocode_result = gmaps.geocode(cleaned_string_item)

            if geocode_result:
                latitude, longitude = geocode_result[0]['geometry']['location']['lat'], geocode_result[0]['geometry']['location'][
                    'lng']
                self.df.loc[index, 'Latitude_GoogleMaps'] = str(latitude)
                self.df.loc[index, 'Longitude_GoogleMaps'] = str(longitude)

                location_type = geocode_result[0]['geometry']['location_type']
                confidence_level = 0.8  # Default confidence
                if location_type == 'ROOFTOP':
                    confidence_level = 1.0
                elif location_type == 'RANGE_INTERPOLATED':
                    confidence_level = 0.7
                elif location_type == 'GEOMETRIC_CENTER':
                    confidence_level = 0.5
                elif location_type == 'APPROXIMATE':
                    confidence_level = 0.3

                self.df.loc[index, 'Score_GoogleMaps'] = confidence_level
            else:
                self.df.loc[index, 'Score_GoogleMaps'] = 0.0

        time.sleep(1)
        print(" >> Process Complete")
        self.export_df_to_csv(self.export_filepath, self.export_csv_file_name)

    ##############################################
    def export_df_to_csv(self, export_filepath: str, export_csv_file_name: str):

        export_filepath = os.path.join(export_filepath, export_csv_file_name)
        self.df.to_csv(export_filepath, index=False, encoding='utf-8')
        print(" >> Geocode File Created.\n\n")