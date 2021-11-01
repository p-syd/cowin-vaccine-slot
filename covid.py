'''
import time
import json

import requests

response  = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByPin?pincode=411027&date=09-05-2021').text
#response_info = json.loads(response)

print (response)
'''
import os
import time
#os.system('spd-say "your program has finished"')

from cowin_api import CoWinAPI

pin_code = ["411027", "411007", '411057', '411044', '411033'] #add all the pincodes where you would like to search for vaccine slots
date = '09-05-2021'  # Optional. Default value is today's date
min_age_limit = 45  # Optional. By default returns centers without filtering by min_age_limit

while(True):
	cowin = CoWinAPI()
	for i in pin_code:
		available_centers = cowin.get_availability_by_pincode(i, date, min_age_limit)
		#print(available_centers)
		if available_centers['centers'] == []:
			continue
		else:
			for i in available_centers['centers']:
				if int(i['sessions'][0]['available_capacity']) > 0:
					print('SLOTS NUM:  ', i['sessions'][0]['available_capacity'])
					#print("PINCODE:  ", i['pincode'], end='   ')
					print("NAME:  ", i['name'], end='   ')
					print('ADDRESS:  ', i['address'])
					print()
					os.system('spd-say "your program has finished"')
			print('##########################################')
	#time.sleep(5)
			
	

