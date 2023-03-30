import os
import argparse
import sys
import glob
from ruamel.yaml import YAML
import subprocess
import time
import keyboard
import pandas as pd


# Makes sure the path we are saving data capture too exists #
def get_excel_data(path):

        # If the path to store data into exists run the following code #
	if os.path.exists(path):
                

		# data = pd.read_excel(path, engine='openpyxl') #
		data = pd.read_csv(path)
		return data



        
# Sets up the proper data path and location in the computer for us to save the data too #
def parse_args():
    # Argparse is a library for passing command line arguments easier and more flexiable #
    # For when the user is capturing data, the command arguments are being specififed #
    parser = argparse.ArgumentParser(description= 'type path number number and capture type')
    parser.add_argument('--datacapture_excel',default='/home/alpha1/Desktop/data_capture2/result.xlsx',type=str,help='path to excel sheet')
    parser.add_argument('--capture_number',default=1,type=int,help='enter capture number between 1 to 270')
    args = parser.parse_args()
    return args

# Outlines how the data should be captured and what exact data is being captured #
def data_captured( useful_data ):
    # No idea what is happening #
    print('Object: {}'.format(useful_data['Object'].to_string(index = False).strip()))
    print('z_param: {}'.format( useful_data['z_param(mm/in)'].to_string(index = False).strip()  ))
    print('Location: {}'.format( useful_data['Location'].to_string(index=False).strip()  ))
    print('Offset: {} '.format( useful_data['Offset(in)'].to_string(index=False).strip() ))

# Main function 
def main():

        # Calls the arguments from the parse argument procedure # 
	args = parse_args()

	# Defines all of the arguments, how and where they should be called #
	excelsheet_path = args.datacapture_excel
	capture_number = args.capture_number
	look_up_data = get_excel_data(excelsheet_path)
	useful_data = look_up_data[look_up_data['Unnamed: 0']== (capture_number)]
	capture_type = useful_data['Person_Pose'].to_string(index=False).strip()

        # If the following data is being captured #
	if capture_type =='Walking' or capture_type == 'Facing'or capture_type == 'Standstill' or capture_type == 'Step_Placement' or capture_type == 'Turntable_Standstill' or capture_type =='Standstill_Walking' or capture_type =='Standstill_Facing':
		remaining_path = useful_data['Exp_Name'].to_string(index = False).strip()+'/'+str(capture_number)
	else:
		print('Unknown Person_Pose')

        # This data is being #
	default_save_time = 0.0
	output_path = ''
	output_path_capture = ''
	output_path_recorder = ''
	fpga_path = ''
	yaml = YAML()
	yaml.explicit_start = True
	yaml.indent(mapping=4)
	yaml.preserve_quotes = True

        # Dependent on what data we are capturing, certain commands are followed #
	if capture_type == 'Standstill' or capture_type == 'Standstill_Walking' or capture_type=='Standstill_Facing':

                # Determines where the data is being saved #
		with open(r'/data/config/parameters.yml','r') as file:

                        # Saves data as a YAML file and specifies how the data is being saved #
			config_list = yaml.load(file)
			default_save_time = config_list['Capture']['SaveInterval'] 
			output_path_capture = config_list['Capture']['OutputPath']
			output_path_recorder = config_list['Recorder']['OutputDir']
			file.close()

		final_path = os.path.join(output_path_recorder,remaining_path )

		# If the path to save doesn't exist, make it #
		if not os.path.exists(final_path):
			os.makedirs(final_path,exist_ok=False)

		# If it does exist, saves the data to that file #
		if os.path.exists(final_path):
                        # Determines where the data is being saved and specifies how it is being saved #
			with open(r'/data/config/parameters.yml','w') as file:
				config_list['Capture']['OutputPath']  = final_path
				config_list['Recorder']['OutputDir']  = final_path
				config_list['Capture']['SaveInterval']  = 0.5
				yaml.dump(config_list,file)
				file.close()
				
			process1 = subprocess.Popen(['curl','localhost:8123/api/recording-on'], preexec_fn=os.setpgrp)
			time.sleep(1)
			process2 = subprocess.Popen(['curl','localhost:8123/api/recording-off'], preexec_fn=os.setpgrp)
                        # Returns the number of files saved #
			print('\n Number of files saved: {} \n '.format( len(os.listdir(final_path))))
			data_captured( useful_data )
			# Determines where the data is being saved #
			with open(r'/data/config/parameters.yml','w') as file:
				config_list['Capture']['OutputPath']  =  output_path_capture
				config_list['Capture']['SaveInterval'] = default_save_time
				config_list['Recorder']['OutputDir'] = output_path_recorder

				yaml.dump(config_list,file)
				file.close()
                # Else, the path is unusable #
		else:
			print("Path error check the parameters file")
        # If this type of data is being captured, follow the below code #
	elif capture_type == 'Walking' or capture_type == 'Turntable_Standstill'or capture_type == 'Facing' or capture_type =='Step_Placement':
		with open(r'/data/config/parameters.yml','r') as file:
			config_list = yaml.load(file)
			default_save_time = config_list['Capture']['SaveInterval'] 
			output_path_capture = config_list['Capture']['OutputPath']
			output_path_recorder = config_list['Recorder']['OutputDir']
			file.close()
		final_path = os.path.join(output_path_recorder,remaining_path )
		if not os.path.exists(final_path):
			os.makedirs(final_path,exist_ok=False)
		if os.path.exists(final_path):
			with open(r'/data/config/parameters.yml','w') as file:
				config_list['Capture']['OutputPath']  = final_path
				config_list['Recorder']['OutputDir']  = final_path
				config_list['Capture']['SaveInterval']  = 0
				yaml.dump(config_list,file)
				file.close()
				time.sleep(2)
				print("Start {}".format(capture_type))
			process1 = subprocess.Popen(['curl','localhost:8123/api/recording-on'])
			timeout = time.time() + 60*4
			# This is what the user sees on the interactive console when they are actively capturing data #
			while True:
				try:
                                        # If 'c' is pressed #
                                        if keyboard.is_pressed('c'):

                                                # Actual data capture, calls the data_captured function and passes useful data as a parameter
                                                print('\nYou Pressed Key c!')
						process2 = subprocess.Popen(['curl','localhost:8123/api/recording-off'])
						print('\n Number of files saved: {} \n '.format( len(os.listdir(final_path))))
						data_captured( useful_data )
						break  # finishing the loop
				# If control c is pressed then it returns the number of files saved to the user, still captures data #
				except KeyboardInterrupt:
					process2 = subprocess.Popen(['curl','localhost:8123/api/recording-off'])
					print('\n Number of files saved: {} \n '.format( len(os.listdir(final_path)) )) 
					data_captured( useful_data )
					break


			# If the specific path exists then run the following code 
			with open(r'/data/config/parameters.yml','w') as file:

                                # Specifies exactly how the data should be saved and what parameters to account for #
				config_list['Capture']['OutputPath']  =  output_path_capture
				config_list['Capture']['SaveInterval'] = default_save_time
				config_list['Recorder']['OutputDir'] = output_path_recorder
				yaml.dump(config_list,file)
				file.close()
				# time.sleep(2)
				print('Capture_done')
		else:
                        # Error message for the path not existing
			print("path does not exists ",final_path)

	else:
                # Error message for wrog capture number
		print('Wrong capture_number')






if __name__ == '__main__':
    main()
