"""Instructions to input and save files
#Raw.mf4
#Database file
#Trigger.mf4
#Database file
#Location to save 1st extracted file and name
#Location to save file required to be manipulated and name
#Location to save 2nd extracted file and name
#Location to save final manipulated file and name"""

import asammdf as m
import sys
import pandas as pd
import numpy as np
import mdf_toolbox as l
import mdfconverter as mf
# from mdfconverter import mdf
# from mdf_toolbox import mdf
# import mdfreader as j
import pymeasure
import tkinter as tk
from tkinter import filedialog
#from pymeasure.file.mdf import MDF
#from pyMeasure import MDF
# from mdfreader import 

"""mdf_file =m.mdf("C:/Users/Madhav Gupta/OneDrive - Indian Institute of Technology Bombay/Desktop/API/demo18.MF4")
channels = mdf_file.get_channel_names()

# print the list of channels
print(channels)

df = pd.read_csv("C:/Users/Madhav Gupta/OneDrive - Indian Institute of Technology Bombay/Desktop/API/demo18.MF4")
new_df = df[['Cell1', 'Cell2', 'Cell3', 'Cell4']]
new_df.to_csv("C:/Users/Madhav Gupta/OneDrive - Indian Institute of Technology Bombay/Desktop/API/demo19.MF4", index=False)"""
def readMDF1():
    #mrequired_channels = ["t", "VectorBlfEvent", "VectorBlfEvent.ObjectType"] #["Channel group 0 (CAN2 - message Front_CAN 0x68)"]
    mdfile1_path = filedialog.askopenfilename()
    mdfile1 = m.MDF(mdfile1_path) #channels=required_channels)
    #mdf_filter = mdf.filter([('CAN_DataFrame.Flags',1,3)])
    #mdf_select = mdf.select([('CAN_DataFrame.Flags',1,3)])
    #mdf._extract_can_logging
    #mdff = mdf.get(name="VectorBlfEvent")
    #mdf = m.MDF(r"D:/IITB Racing/DAQ/Raw MDF/2022-04-13_01-38-33/TriggerF001.MF4")
    databasefile1_path = filedialog.askopenfilename()
    databases1 = {
    "CAN": [(databasefile1_path,0)]
    }
    return [mdfile1,databases1]

def readMDF2():
    mdfile2_path = filedialog.askopenfilename()
    mdfile2 = m.MDF(mdfile2_path)
    databasefile2_path = filedialog.askopenfilename()
    databases2 = {
    "CAN": [(databasefile2_path,0)]
    }
    return [mdfile2,databases2]
mdfile1,databases1 = readMDF1()
mdfile2,databases2 = readMDF2()
extracted1 = mdfile1.extract_bus_logging(database_files = databases1)
extracted1_file_save_location = filedialog.asksaveasfilename(defaultextension=".mf4",
                                         filetypes=[("All Files", "*.*")])
extracted1.save(extracted1_file_save_location, overwrite=True)
required_channels = ['sens_1_MSB', 'sens_1_LSB', 'sens_2_MSB', 'sens_2_LSB', 'sens_3_MSB', 'sens_3_LSB', 'sens_4_MSB', 'sens_4_LSB', 'Acc_Y_axis', 'Acc_X_Axis', 'Yaw_ang_accln', 'Yaw_rate_1', 'Susp_RL', 'Susp_RR', 'Susp_FL', 'Susp_FR', 'Susp_FL_LSB', 'Susp_FR_LSB', 'Cell1', 'Cell2', 'Cell3', 'Cell4', 'Cell5', 'Cell6', 'Cell7', 'Cell8', 'Cell9', 'Cell10', 'Cell11', 'Cell12','Cell13', 'Cell14', 'Cell15', 'Cell16']
mdfile = m.MDF(extracted1_file_save_location, channels = required_channels)
mdfile_save_location = filedialog.asksaveasfilename(defaultextension=".mf4",
                                         filetypes=[("All Files", "*.*")])
mdfile.save(mdfile_save_location, overwrite=True)
#mdfile.export(fmt='csv', filename='C:/Users/Madhav Gupta/OneDrive - Indian Institute of Technology Bombay/Desktop/API/fchannels_new_1.csv')

extracted2 = mdfile2.extract_bus_logging(database_files = databases2)
extracted2_file_save_location = filedialog.asksaveasfilename(defaultextension=".mf4",
                                         filetypes=[("All Files", "*.*")])
extracted2.save(extracted2_file_save_location, overwrite=True)

#csv = extracted.export(fmt='csv', filename='C:/Users/Madhav Gupta/OneDrive - Indian Institute of Technology Bombay/Desktop/API/four.csv')
#extracted.append
#mdff = k.Mdf("C:/Users/Madhav Gupta/OneDrive - Indian Institute of Technology Bombay/Desktop/API/demofinal.MF4")
#mdfile.iter_groups
# using asmmdf to get channels
"""mdf_file = MDF('C:/Users/Madhav Gupta/OneDrive - Indian Institute of Technology Bombay/Desktop/API/demofinal.MF4')
existing_channel = mdf_file.get_channel('sens_1_MSB')
new_channel_data = existing_channel.data*2
mdf_file.add_channel('channel_new_new', new_channel_data, existing_channel.unit, existing_channel.description)
mdf_file.save('C:/Users/Madhav Gupta/OneDrive - Indian Institute of Technology Bombay/Desktop/API/demofinaloperated.MF4')"""
new_mdfile_1 = m.MDF(mdfile_save_location)#r"C:/Users/Madhav Gupta/OneDrive - Indian Institute of Technology Bombay/Desktop/API/Extracted_channels_only_for_manipulation_1.MF4")
new_mdfile_2 = m.MDF(extracted2_file_save_location)#r"C:/Users/Madhav Gupta/OneDrive - Indian Institute of Technology Bombay/Desktop/API/Extracted_channels_2.MF4")
df  = new_mdfile_1.to_dataframe()
df2  = new_mdfile_2.to_dataframe()
df["APPS"] = ((df["sens_1_LSB"] + df["sens_1_MSB"]*4) + (df["sens_2_LSB"] + df["sens_2_MSB"]*4))/2 #(np.bitwise_xor(df["sens_2_LSB"].values, df["sens_2_MSB"].values))/2  # Don't know the exact formulas so just demo
df["Steering"] = (df["sens_3_LSB"] + df["sens_3_MSB"]*4)
df["Susp_FL_net"] = (df["Susp_FL"]*4 + df["Susp_FL_LSB"])
df["Susp_FR_net"] = (df["Susp_FR"]*4 + df["Susp_FR_LSB"]) 
df = df.drop(['sens_1_MSB', 'sens_1_LSB', 'sens_2_MSB', 'sens_2_LSB', 'sens_3_MSB', 'sens_3_LSB', 'sens_4_MSB', 'sens_4_LSB', 'Susp_FL', 'Susp_FR', 'Susp_FL_LSB', 'Susp_FR_LSB', 'Cell1', 'Cell2', 'Cell3', 'Cell4', 'Cell5', 'Cell6', 'Cell7', 'Cell8', 'Cell9', 'Cell10', 'Cell11', 'Cell12','Cell13', 'Cell14', 'Cell15', 'Cell16'], axis =1)
df["Current"] = df2["Current"]
#df2 =df2.drop([])
#df = pd.concat([df, df2])
print(df)
print("Channels:", new_mdfile_1.get_channel_name(index = 1, group = 3))
# new_mdfile.delete_channels(group = 1, index = 1)
#m.write_dataframe(df, 'C:/Users/Madhav Gupta/OneDrive - Indian Institute of Technology Bombay/Desktop/API/Manipulated_Channels.MF4')
#new_mdfile.append(df)
#new_mdfile.save('C:/Users/Madhav Gupta/OneDrive - Indian Institute of Technology Bombay/Desktop/API/Manipulated_Channels.MF4', overwrite=True) # Loocation to save the final file

required_channels_final = []
final_mdf = m.MDF(extracted1_file_save_location, channels = required_channels_final)
    

final_mdf.append(df)
final_mdf_path_save = filedialog.asksaveasfilename(defaultextension=".mf4",
                                         filetypes=[("All Files", "*.*")])
final_mdf.save(final_mdf_path_save, overwrite = True)#'C:/Users/Madhav Gupta/OneDrive - Indian Institute of Technology Bombay/Desktop/API/Manipulated_Channels.MF4', overwrite=True) # Loocation to save the final file

"""mdf_file = mdf.read("C:/Users/Madhav Gupta/OneDrive - Indian Institute of Technology Bombay/Desktop/API/demofinal.MF4")
existing_channel = mdf_file.get('sens_1_MSB')

new_channel = mdf.make_channel('new_channel_name', existing_channel.data, existing_channel.unit, existing_channel.comment)
mdf_file.add(new_channel)

# Save the new mdf file
mdf_file.save('C:/Users/Madhav Gupta/OneDrive - Indian Institute of Technology Bombay/Desktop/API/demofinaloperated.MF4')"""

# mdf toolbox
"""mdfg = l.("C:/Users/Madhav Gupta/OneDrive - Indian Institute of Technology Bombay/Desktop/API/demofinal.MF4")

# Get the data from the existing channels
channel1_data = mdf.select(channel='channel1')
channel2_data = mdf.select(channel='channel2')

# Create the new channel by multiplying the data from the existing channels
new_channel_data = channel1_data * channel2_data

# Add the new channel to the MDF file
mdf.append(channel_data=new_channel_data, channel_name='new_channel')

# Save the MDF file with the new channel
mdf.save("C:/Users/Madhav Gupta/OneDrive - Indian Institute of Technology Bombay/Desktop/API/demofinaloperated.MF4")"""

# mdf reader
"""data_1 = mdf.get('sens_1_MSB')
data_2 = mdf.get('sens_2_MSB')
new_data = data_1 * data_2
new_channel_group = l.ChannelGroup()
new_channel_group.add_channel(name='new_channel', unit='-', conversion=1, data=new_data)
mdf.add_channel_group(new_channel_group)
mdf.save('C:/Users/Madhav Gupta/OneDrive - Indian Institute of Technology Bombay/Desktop/API/demonewgroup.MF4', overwrite=True)"""

#mdf_object = m.MDF('C:/Users/Madhav Gupta/OneDrive - Indian Institute of Technology Bombay/Desktop/API/demo11.MF4')
#signals_to_keep = ['Yaw_ang_accln']
#mdf_to_plot = mdf_object.filter(signals_to_keep).cut(start=100, stop=240)
#mdf_dataframe = mdf_to_plot.to_dataframe()
#ax = mdf_dataframe.plot(figsize=(20, 10), title='Test', grid=True)
#ax.figure.savefig("D:/IITB Racing/DAQ/Scripts/firstplot.png")"""
