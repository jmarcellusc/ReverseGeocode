"""
Tool:               Reverse Geocoder V1
Source Name:        ReverseGeocode
Version:            1.0
Author:             Juan-Marcel Campos
Usage:              String Address Reverse Geocoding
Required Arguments: CSV File with Headers and Entries

Optional Arguments: <parameter2>
                    <parameter3>
Description:        Will preform various reverse geocoding methods.
"""

import os, sys
import importlib
import re
import time

from Geocode_Libraries import Geocode_System_Functions as GSF
from Geocode_Libraries import Geocode_Class as GC

# ! Front Matter
#########################################################################
#########################################################################
VERSION_R_GEOCODE = 1.0


# * Starting Project:
#  GitHub Repo: Reverse Geocode
# v1.0 -  Initial Creation of Script (Not yet commited)


#########################################################################
def extract_module_name(module_str):
    match = re.search(r"module '(.+?)'", module_str)
    if match:
        return match.group(1)
    return None


#########################################################################
def check_library(library_name: str) -> None:
    """Checks if a library is installed. If not, informs the user and exits."""
    try:
        module = importlib.import_module(library_name)
        module_name = extract_module_name(str(module))
        return module, module_name
    except ImportError:
        print(f"\n >> ERROR: The '{library_name}' library is not installed.")
        print(f"Please install it using 'pip install {library_name}' and try again.")
        print("Ending...\n\n")
        exit(1)


#########################################################################
def library_inspection(module_inspection: str) -> None:
    """ Runs both the check_library and extract_module_name Functions"""

    module_inspect, module_name = check_library(module_inspection)
    try:
        version = module_inspect.__version__
        print(f"Library: {module_name} Installed - Version:{str(version)}")
        time.sleep(0.5)
    except AttributeError:
        version = "Version Not Specified"
        print(f"Library: {module_name} Installed - {str(version)}")


#########################################################################
#########################################################################
print("\n")
library_inspection("pandas")
library_inspection("geopy")
library_inspection("tkinter")
library_inspection("googlemaps")
print("\n\n\n")




## ==> Functions
##############################################################
def select_reverse_geocode_method() -> str:

    print("\n============================================")
    print("Please Select the Geocode System to Utilize:")
    time.sleep(1)
    print("1. Open Cage")
    time.sleep(0.5)
    print("2. Google Maps V3")
    time.sleep(0.5)
    print("3. Exit")
    time.sleep(0.7)

    choice = input("\nEnter your choice (1/2/0): ")

    if choice == "1":
        print('\n >> \"Open Cage\" Method Selected.\n')
        return "opencage"
    elif choice == "2":
        print('\n >> \"Google Maps\" Method Selected.\n')
        return "googlemaps"
    elif choice == "0":
        print("Exiting...")
        exit_program("\n Selected to End Program. Ending...")
    else:
        print("Invalid choice. Please try again.")
        time.sleep(1)
        select_reverse_geocode_method()

##############################################################
def exit_program(exit_message: str):
    """Exits the Python program."""
    print(exit_message)
    sys.exit()






##=================================================
## >>>          _Main Script Process_           <<<
##=================================================
# ! Pandas Format
if __name__=="__main__":
    #####################################################################################
    # ! Introduction
    time.sleep(5)
    print("#####################################################")
    print("   | ---      Reverse GeoCode Toolkit          --- |   ")
    print("   | ---        \"Attribution Series\"         --- | ")
    print("#####################################################")
    time.sleep(1)
    print(f"__Version: {VERSION_R_GEOCODE}\n")

    # Methodology Selection Process
    GEOCODE_METHOD: str = select_reverse_geocode_method()

    # Main Variables
    FIELD_NAME: str = "Address"
    EXPORT_FILE_NAME: str = "Geocode.csv"


    # Reads File and Root Directory
    file_path = GSF.select_csv_file()  # Select CSV File
    if not file_path:
        exit_program("\n\n >> No File Selected. Ending...\n\n")
    time.sleep(1)

    # Gets filename and root directory
    root_directory, target_file_name = GSF.get_root_and_filename(file_path)
    if root_directory and target_file_name:
        print(f"   __ Selected File: \"{target_file_name}\"")
    else:
        exit_program(" >> ERROR Reading File. Ending...\n\n")
    time.sleep(1)

    # Selects the Address Field
    FIELD_NAME = GSF.select_field_name(file_path)

    # Creates export file
    time.sleep(1)
    EXPORT_FILE_NAME = GSF.process_directory_csv_read(root_directory)
    default_export_file = os.path.join(root_directory, EXPORT_FILE_NAME)
    print(" __ Creating Export File")
    print(f" >> Export Geocode File: \"{EXPORT_FILE_NAME}\"\n\n")
    time.sleep(1)

    # Checks if CSV is Empty
    if GSF.df_is_empty(file_path):
        exit_program("\n CSV File is Empty or Contains an Error. \nPlease Check Data. Ending...")
    time.sleep(1)


    # Initial Class Processor
    print(" >> Initializing Geocoding")
    time.sleep(0.5)
    processor = GC.DataProcessor(root_directory, EXPORT_FILE_NAME, GEOCODE_METHOD)
    processor.check_read_address_dataframe(file_path, FIELD_NAME) # Check if "Address" field exist
    time.sleep(1)
    processor.run_geocoding(FIELD_NAME)  # Check and Create Latitude and Longitude Fields
    time.sleep(1)
    #processor.print_console_df()  # Check and Create Latitude and Longitude Fields
    print(f"  __File: {EXPORT_FILE_NAME}")
    print("All Geocode Processes Complete. \n\n")

