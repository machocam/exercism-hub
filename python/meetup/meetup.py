from calendar import monthrange
from datetime import date

def meetup_day (year, month, week_day, spec):
	base_info = monthrange(year, month)
	day = 0 
	
	#Here I introduce two dictionaries that will translate the input date into structured data
	weekday_num = {"Monday":0, "Tuesday":1, "Wednesday":2, "Thursday":3, "Friday":4, "Saturday":5, "Sunday":6}
	specs_num = {"1st":1, "2nd":2, "3rd":3, "4th":4, "5th":5, "last": "last", "teenth":"teenth"}
	
	#introuction to the logic split in two cases.
	if weekday_num[week_day] >= base_info[0]:
		if (spec != "teenth" and spec != "last"):
			day = 7*(specs_num[spec]-1) + (abs(weekday_num[week_day] - base_info[0]) + 1)
		elif spec == "teenth": 
			i = 0
			while day not in range(13,20):
				day = 7*i + (abs(weekday_num[week_day] - base_info[0]) + 1)
				i += 1
		else : 
			i = 0
			while day not in range(base_info[1]-6, base_info[1] + 1):
				day = 7*i + (abs(weekday_num[week_day] - base_info[0]) + 1)
				i += 1
	else: 
		if (spec != "teenth" and spec != "last"):
			day = 7*specs_num[spec] - (abs(weekday_num[week_day] - base_info[0]) - 1)
		elif spec == "teenth": 
			i = 0
			while day not in range(13,20):
				day = 7*i - (abs(weekday_num[week_day] - base_info[0]) - 1)
				i += 1
		else : 
			i = 0
			while day not in range(base_info[1]-6, base_info[1] + 1):
				day = 7*i - (abs(weekday_num[week_day] - base_info[0]) - 1)
				i += 1

	return date(year, month, day)
	
	

