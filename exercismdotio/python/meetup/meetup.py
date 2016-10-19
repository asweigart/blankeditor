import datetime, calendar

class MeetupDayException(Exception):
	pass

def dayToStr(dayNumber):
	return {0: 'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}[dayNumber]

def meetup_day(year, month, day, which):
	assert which in ('1st', '2nd', '3rd', '4th', '5th', 'teenth', 'last')
	assert day in ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
	
	if which != 'last':
		# start current day on the 1st of the month:
		curDay = datetime.date(year, month, 1) 
	elif which == 'last':
		# start current day on the last day of the month:
		curDay = datetime.date(year, month, calendar.monthrange(year, month)[1])

	timesDaySeen = 0
	while curDay.month == month:
		# test to see if curDay matches the day we're looking for
		if dayToStr(curDay.weekday()) == day:
			timesDaySeen += 1
			
			# handle '1st', '2nd', '3rd', '4th', '5th' cases
			if timesDaySeen == 1 and which == '1st':
				return curDay
			if timesDaySeen == 2 and which == '2nd':
				return curDay
			if timesDaySeen == 3 and which == '3rd':
				return curDay
			if timesDaySeen == 4 and which == '4th':
				return curDay
			if timesDaySeen == 5 and which == '5th':
				return curDay
			
			# handle 'teenth' case:
			if which == 'teenth' and (13 <= curDay.day <= 19):
				return curDay

			# handle 'last' case:
			if which == 'last':
				return curDay


		# increment/decrement day
		if which != 'last':
			curDay += datetime.timedelta(days=1) # change curDay to next day
		elif which == 'last':
			curDay -= datetime.timedelta(days=1)
	raise MeetupDayException

