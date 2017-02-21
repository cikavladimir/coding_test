""" This program will parse a log file and extract needed information and summarize per minute intervals.
	Code should be run along with input log. Example of run: 
	python logs_aggregation.py fixture.log > out.txt
"""

import fileinput
import sys

temp_minute = -1

for line in fileinput.input([sys.argv[1]]):
    ##################################################
    # Prepare local Dictionary for each line:
    ##################################################
    line_dict = {}
    line_array = line.split()
    for el in line_array:
    	if "=" in el:
    		key = el.split("=")[0]
    		value = el.split("=")[1]
    		value = value.replace('"','')
    		line_dict[key] = value

    ##################################################
    # Check if Key is in Dict (add Key if is not):
    ##################################################
    if 'service' in line_dict:
    	line_dict['service'] = line_dict['service'].replace('ms','')
    if 'connect' in line_dict:
    	line_dict['connect'] = line_dict['connect'].replace('ms','')

	##################################################
    # Parse date/time - prepare minute:
    ##################################################
    date_time = line_array[0]
    time_array = date_time.split(':')
    time_for_print = date_time.split('.')[0]
    time_for_print = time_for_print[:-2]
    time_for_print = time_for_print + "00"
    current_minute = time_array[1]

	##################################################
    # Main logic:
    ##################################################
    if temp_minute < 0:
    	minute_dict = {}  # Initialize Dictionary

    	minute_dict[line_dict['host']] = {} # Create Key in dictionary
    	minute_dict[line_dict['host']]['min'] = line_dict['service'] # Initialize Minimum
    	minute_dict[line_dict['host']]['max'] = line_dict['service'] # Initialize Maximum
    	minute_dict[line_dict['host']]['count'] = 1 # Initialize Count
    	minute_dict[line_dict['host']]['total'] = int(line_dict['service']) # Initialize Total
    	temp_minute = current_minute # Record temp value of a minute so we can use it for comparison later.
    elif temp_minute != current_minute:  # First time see new minute
    	for key in sorted(minute_dict):
    		print time_for_print + "," + key + "," + str(minute_dict[key]['count']) + "," + str(minute_dict[key]['total']) + "," + str(minute_dict[key]['min']) + "," + str(minute_dict[key]['max'])

    	minute_dict = {}
    	minute_dict[line_dict['host']] = {}
    	minute_dict[line_dict['host']]['min'] = line_dict['service']
    	minute_dict[line_dict['host']]['max'] = line_dict['service']
    	minute_dict[line_dict['host']]['count'] = 1
    	minute_dict[line_dict['host']]['total'] = int(line_dict['service'])
    	
    	temp_minute = current_minute
    else:
    	if line_dict['host'] in minute_dict:
    		if (minute_dict[line_dict['host']]['min'] > line_dict['service']):
    			minute_dict[line_dict['host']]['min'] = line_dict['service']
    		if (minute_dict[line_dict['host']]['max'] < line_dict['service']):
    			minute_dict[line_dict['host']]['max'] = line_dict['service']
    		minute_dict[line_dict['host']]['count'] += 1
    		minute_dict[line_dict['host']]['total'] += int(line_dict['service'])
    	else:
    		minute_dict[line_dict['host']] = {}
    		minute_dict[line_dict['host']]['min'] = line_dict['service']
    		minute_dict[line_dict['host']]['max'] = line_dict['service']
    		minute_dict[line_dict['host']]['count'] = 1
    		minute_dict[line_dict['host']]['total'] = int(line_dict['service'])

if temp_minute == current_minute:
	for key in sorted(minute_dict):
		print time_for_print + "," + key + "," + str(minute_dict[key]['count']) + "," + str(minute_dict[key]['total']) + "," + str(minute_dict[key]['min']) + "," + str(minute_dict[key]['max'])
