import os
import time
from cowin_api import CoWinAPI

'''
Link to find district id: 

https://github.com/bhattbhavesh91/cowin-vaccination-slot-availability/blob/main/district_mapping.csv

'''

district_id = '363'
date = '09-05-2021'  # Optional. Takes today's date by default
min_age_limit = 18  # Optional. By default returns centers without filtering by min_age_limit


while(True):
	cowin = CoWinAPI()
	available_centers = cowin.get_availability_by_district(district_id, date, min_age_limit)
	#print(available_centers)
	if available_centers['centers'] == []:
		continue
	for i in available_centers['centers']:
		if i['sessions'][0]['available_capacity'] >= 0:
			print('SLOTS NUM:  ', i['sessions'][0]['available_capacity'])
			#print("PINCODE:  ", i['pincode'], end='   ')
			print("NAME:  ", i['name'], end='   ')
			print('ADDRESS:  ', i['address'])
			print()
			#os.system('spd-say "SLOTS AVAILABLE BOOK FAST"')
	print('##########################################')
	print() 
	print()
		

