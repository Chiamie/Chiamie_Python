#4.5 (Fill in the Missing Code?)
def seconds_since_midnight(hour, minutes, seconds):
	hour_in_seconds = 60 * 60 * hour
	minute_in_seconds = 60 * minutes
	return hour_in_seconds + minute_in_seconds + seconds




print(seconds_since_midnight(5, 18, 43))
print(seconds_since_midnight(13, 30, 45))
