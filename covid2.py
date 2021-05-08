import os
import time
#os.system('spd-say "your program has finished"')

from cowin_api import CoWinAPI

pin_code = ['412202',"411027", "411007", '411057', '411044', '411033']
date = '09-05-2021'  # Optional. Default value is today's date
min_age_limit = 18  # Optional. By default returns centers withut filtering by min_age_limit

while(True):
	cowin = CoWinAPI()
	for i in pin_code:
		available_centers = cowin.get_availability_by_pincode(i, date, min_age_limit)
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
				os.system('spd-say "SLOTS AVAILABLE BOOK FAST"')
		print('##########################################')
	#time.sleep(5)
			
	

