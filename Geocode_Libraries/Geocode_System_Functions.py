import os
import time

import pandas as pd
import tkinter as tk
from tkinter import filedialog


##############################################################
def select_csv_file():
    time.sleep(1)
    print(" >> Initializing CSV File Selector (Please Minimize All Windows)")
    root = tk.Tk()
    root.withdraw()
    return filedialog.askopenfilename(filetypes=[('CSV Files', '*.csv')])

##############################################################
def get_root_and_filename(csv_file_path: str):

    root_dir, filename = os.path.split(csv_file_path)
    return root_dir, filename

##############################################################
def check_file_exists(check_file_path: str):
    return os.path.isfile(check_file_path)

##############################################################
def process_directory_csv_read(directory_path: str) -> str:
    new_filename = "Geocode_1.csv"

    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".csv"):
                if file == "Geocode_1.csv":
                    # Find the highest number in existing Geocode_#.csv files
                    highest_num = 1
                    for f in files:
                        if f.startswith("Geocode_") and f.endswith(".csv"):
                            num = int(f.split("_")[1].split(".")[0])
                            highest_num = max(highest_num, num)

                    # Create a new filename with the incremented number
                    new_filename = f"Geocode_{highest_num + 1}.csv"
    return new_filename

##############################################################
def df_is_empty(empty_csv_file: str) -> bool:
  ## Checks if a Pandas DataFrame is empty.
  empty_df = pd.read_csv(empty_csv_file)

  return empty_df.empty

##############################################################
def select_field_name(csv_file_select_field: str) -> str:
  ## Prompts the user to select a field name from a DataFrame.

  field_select_df = pd.read_csv(csv_file_select_field)
  print("\n-----------------------------------------")
  print("Please Select the Complete Address Field:")
  for i, field in enumerate(field_select_df.columns, 1):
      print(f"{i}. {field}")
      time.sleep(0.3)

  while True:
      try:
          choice = int(input("\nEnter the number of the Address field you want to select: "))
          if 1 <= choice <= len(field_select_df.columns):
              print("\n")
              return str(field_select_df.columns[choice - 1])
          else:
              print("Invalid choice. Please try again.")
      except ValueError:
          print("Invalid input. Please enter a number.")
