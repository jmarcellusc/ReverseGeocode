# Reverse Geocoding 

This program coding project will read in a CSV containing address and reverse geocode to produce latitudes and longitudes.
It can utilize various geocoding services which are listed below

### List of Geocode Services
*  Open Cage
*  Google Maps V3

## Requirements
For each geocode service, its API key is required in a separate python file. Please update manually and enforce API key read.

## Methods
Under the Geocode_Libraries, there are two python files: "Geocode_Class.py" and "Geocode_System_Functions"
To introduce a new service, the coding should be introduced in the Main Class method of Geocode_Class.py
Please run the "Main.py" to initiate the program.

### Steps in Program
1.  Select the Geocoding Service
2.  Select the CSV file with an Explorer Picker
3.  Select the Field containing the complete address 

#### Notes:
* The program will generate a "Geocode_#.csv" export file
* Latitude and Longitude fields will be autofill, if a location exist
* Score field will be populated depending on the service available.


## Geocode Services and Score Methods
### Open Cage
OpenCage is a free and open-source geocoding API that provides geocoding and reverse geocoding 
Map, to provide accurate and reliable results.
* Score Method; 0-10

### Google Map V3
Google Maps Geocoding API V3 is a powerful tool for converting addresses into geographic coordinates (latitude and longitude) and vice versa. 
It's a key component of many web and mobile applications that rely on location-based services.
* Score Method; 0-1


## Future Plans and Modifications
* Add new services

