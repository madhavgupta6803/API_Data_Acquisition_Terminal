# API_Data_Acquisition_Terminal
The code provided in decoder.py is for processing data from a car's run, specifically stored in MDF (Measurement Data Format) files. It performs the following tasks:

File Input: The script allows users to select MDF files (mdfile1 and mdfile2) containing data from the car's run, along with their corresponding database files.

Data Extraction: It extracts relevant data from the selected MDF files (mdfile1 and mdfile2) based on provided database files and saves the extracted data to new MDF files (extracted1 and     extracted2).

Data Manipulation: The script reads data from the extracted MDF files into Pandas DataFrames (df and df2). It then performs various data manipulation operations, including the creation of calculated columns such as "APPS," "Steering," and "Susp_FL_net."

Channel Selection: Unnecessary channels are removed from the DataFrame.

Data Merging: Data from df2 is merged into df by adding a "Current" column.

Final MDF File Creation: A new MDF file (final_mdf) is created, and the manipulated data is appended to it.

File Output: The final MDF file is saved to a location specified by the user.

This code is a crucial part of the data analysis and processing pipeline for car run data in MDF format. It enables users to select input files, extract relevant data, perform necessary data manipulations, and save the results in a new MDF file for further analysis.
