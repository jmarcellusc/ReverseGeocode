# Reverse Geocoding 

This program coding project will read in a CSV containing address and reverse geocode to produce latitudes and longitudes.
It can multi-utilize various geocoding services which are listed beloew

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
   * The program will generate a "Geocode_#.csv" export file
   * Latitude and Longitude fields will be autofilled, if a location exist
   * Score field will be populated depending on the service availabe.


