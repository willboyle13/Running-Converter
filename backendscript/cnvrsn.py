import datetime

def convertToSecs(myTime):
	'''
	Converts standard formatted time (hh:mm:ss.ms) into seconds so it can be manipulated easily
	'''
	try:
		newTime = myTime.split(':')
		try:
			hours = int(newTime[0])*60*60
			mins = int(newTime[1])*60
			secs = float(newTime[2])
			timeInSecs = hours + mins + secs
		except:
			hours = None
			mins = int(newTime[0])*60
			secs = float(newTime[1])
			timeInSecs = mins + secs
			return timeInSecs

		else:
			return timeInSecs
	except:
		hours = None
		mins = None
		secs = float(myTime)
		timeInSecs = secs
		return timeInSecs	

def convertToMins(convertedTime):
	'''
	Converts the seconds we manipulated back into standard formatted time for the user
	'''
	seconds_input = int(convertedTime)
	final_time = str(datetime.timedelta(seconds=seconds_input))
	print(final_time)

#runner classes for advanced conversions

class eightFifteen:
	def __init__(self, time=0):
		self.time = time

	def __str__(self):
		return f'The time you want to convert is {self.time}'

	
	def eightToFifteen(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time*2.048
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 1500m time is: {final_time}')

	def fifteenToEight(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time/2.048
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 800m time is: {final_time}')

	def fifteenToThree(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time*2.183
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 3000m time is: {final_time}')

	def threeToFifteen(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time/2.183
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 1500m time is: {final_time}')

	def fifteenToFive(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time*3.849
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 5000m time is: {final_time}')

	def fiveToFifteen(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time/3.849
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 1500m time is: {final_time}')
		
	def threeToFive(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time*1.763
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 5000m time is: {final_time}')		

	def fiveToThree(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time/1.763
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 3000m time is: {final_time}')	

class eightMoreFifteen:
	def __init__(self, time=0):
		self.time = time

	def __str__(self):
		return f'The time you want to convert is {self.time}'

	
	def eightToFifteen(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time*2.034
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 1500m time is: {final_time}')

	def fifteenToEight(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time/2.034
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 800m time is: {final_time}')

	def fifteenToThree(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time*2.169
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 3000m time is: {final_time}')

	def threeToFifteen(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time/2.169
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 1500m time is: {final_time}')

	def fifteenToFive(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time*3.810
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 5000m time is: {final_time}')

	def fiveToFifteen(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time/3.810
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 1500m time is: {final_time}')
		
	def threeToFive(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time*1.756
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 5000m time is: {final_time}')		

	def fiveToThree(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time/1.756
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 3000m time is: {final_time}')	

class pureFifteen:

	def __init__(self, time=0):
		self.time = time

	def __str__(self):
		return f'The time you want to convert is {self.time}'

	
	def eightToFifteen(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time*2.020
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 1500m time is: {final_time}')

	def fifteenToEight(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time/2.020
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 800m time is: {final_time}')

	def fifteenToThree(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time*2.155
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 3000m time is: {final_time}')

	def threeToFifteen(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time/2.155
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 1500m time is: {final_time}')

	def fifteenToFive(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time*3.771
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 5000m time is: {final_time}')

	def fiveToFifteen(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time/3.771
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 1500m time is: {final_time}')
		
	def threeToFive(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time*1.750
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 5000m time is: {final_time}')		

	def fiveToThree(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time/1.750
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 3000m time is: {final_time}')

	def fiveToTen(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time*2.115
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 10000m time is: {final_time}')

	def tenToFive(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time/2.115
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 5000m time is: {final_time}')

	def fifteenToTen(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time*7.967
		seconds_input = int(finalSeconds)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 10000m time is: {final_time}')

	def tenToFifteen(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time/7.967
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 1500m time is: {final_time}')

class fifteenFive:

	def __init__(self, time=0):
		self.time = time

	def __str__(self):
		return f'The time you want to convert is {self.time}'

	
	def eightToFifteen(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time*2.000
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 1500m time is: {final_time}')

	def fifteenToEight(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time/2.000
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 800m time is: {final_time}')

	def fifteenToThree(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time*2.135
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 3000m time is: {final_time}')

	def threeToFifteen(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time/2.135
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 1500m time is: {final_time}')

	def fifteenToFive(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time*3.714
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 5000m time is: {final_time}')

	def fiveToFifteen(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time/3.714
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 1500m time is: {final_time}')
		
	def threeToFive(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time*1.740
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 5000m time is: {final_time}')		

	def fiveToThree(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time/1.740
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 3000m time is: {final_time}')

	def fiveToTen(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time*2.100
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 10000m time is: {final_time}')

	def tenToFive(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time/2.100
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 5000m time is: {final_time}')

	def fifteenToTen(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time*7.799
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 10000m time is: {final_time}')

	def tenToFifteen(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time/7.799
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 1500m time is: {final_time}')

class pureFive:

	def __init__(self, time=0):
		self.time = time

	def __str__(self):
		return f'The time you want to convert is {self.time}'

	
	def eightToFifteen(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time*1.989
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 1500m time is: {final_time}')

	def fifteenToEight(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time/1.989
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 800m time is: {final_time}')

	def fifteenToThree(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time*2.124
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 3000m time is: {final_time}')

	def threeToFifteen(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time/2.124
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 1500m time is: {final_time}')

	def fifteenToFive(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time*3.683
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 5000m time is: {final_time}')

	def fiveToFifteen(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time/3.683
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 1500m time is: {final_time}')
		
	def threeToFive(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time*1.734
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 5000m time is: {final_time}')		

	def fiveToThree(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time/1.734
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 3000m time is: {final_time}')

	def fiveToTen(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time*2.092
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 10000m time is: {final_time}')

	def tenToFive(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time/2.092
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 5000m time is: {final_time}')

	def fifteenToTen(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time*7.707
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 10000m time is: {final_time}')

	def tenToFifteen(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time/7.707
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 1500m time is: {final_time}')

class fiveTen:

	def __init__(self, time=0):
		self.time = time

	def __str__(self):
		return f'The time you want to convert is {self.time}'

	
	def eightToFifteen(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time*1.978
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 1500m time is: {final_time}')

	def fifteenToEight(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time/1.978
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 800m time is: {final_time}')

	def fifteenToThree(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time*2.113
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 3000m time is: {final_time}')

	def threeToFifteen(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time/2.113
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 1500m time is: {final_time}')

	def fifteenToFive(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time*3.652
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 5000m time is: {final_time}')

	def fiveToFifteen(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time/3.652
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 1500m time is: {final_time}')
		
	def threeToFive(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time*1.728
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 5000m time is: {final_time}')		

	def fiveToThree(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time/1.728
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 3000m time is: {final_time}')

	def fiveToTen(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time*2.084
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 10000m time is: {final_time}')

	def tenToFive(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time/2.084
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 5000m time is: {final_time}')

	def fifteenToTen(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time*7.615
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 10000m time is: {final_time}')

	def tenToFifteen(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time/7.615
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 1500m time is: {final_time}') 

class pureTen:

	def __init__(self, time=0):
		self.time = time

	def __str__(self):
		return f'The time you want to convert is {self.time}'

	
	def eightToFifteen(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time*1.968
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 1500m time is: {final_time}')

	def fifteenToEight(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time/1.968
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 800m time is: {final_time}')

	def fifteenToThree(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time*2.102
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 3000m time is: {final_time}')

	def threeToFifteen(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time/2.102
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 1500m time is: {final_time}')

	def fifteenToFive(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time*3.621
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 5000m time is: {final_time}')

	def fiveToFifteen(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time/3.621
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 1500m time is: {final_time}')
		
	def threeToFive(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time*1.722
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 5000m time is: {final_time}')		

	def fiveToThree(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time/1.722
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 3000m time is: {final_time}')

	def fiveToTen(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time*2.076
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 10000m time is: {final_time}')

	def tenToFive(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time/2.076
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 5000m time is: {final_time}')

	def fifteenToTen(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time*7.523
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 10000m time is: {final_time}')

	def tenToFifteen(myTime):
		time = convertToSecs(myTime)
		finalSeconds = time/7.523
		seconds_input = round(float(finalSeconds), 2)
		final_time = str(datetime.timedelta(seconds=seconds_input))
		print(f'Your projected 1500m time is: {final_time}') 

#Basic Conversion functions

def fifteenToMile(myTime):
	time = convertToSecs(myTime)
	finalSeconds = time*1.08
	seconds_input = round(float(finalSeconds), 2)
	final_time = str(datetime.timedelta(seconds=seconds_input))
	print(f'Your projected mile time is: {final_time}')

def mileToFifteen(myTime):
	time = convertToSecs(myTime)
	finalSeconds = time/1.08
	seconds_input = round(float(finalSeconds), 2)
	final_time = str(datetime.timedelta(seconds=seconds_input))
	print(f'Your projected 1500m time is: {final_time}')

def fifteenToSixteen(myTime):
	time = convertToSecs(myTime)
	finalSeconds = time*1.0737
	seconds_input = round(float(finalSeconds), 2)
	final_time = str(datetime.timedelta(seconds=seconds_input))
	print(f'Your projected 1600m time is: {final_time}')

def sixteenToFifteen(myTime):
	time = convertToSecs(myTime)
	finalSeconds = time/1.0737
	seconds_input = round(float(finalSeconds), 2)
	final_time = str(datetime.timedelta(seconds=seconds_input))
	print(f'Your projected 1500m time is: {final_time}')

def eightToOne(myTime):
	time = convertToSecs(myTime)
	finalSeconds = time*1.286
	seconds_input = round(float(finalSeconds), 2)
	final_time = str(datetime.timedelta(seconds=seconds_input))
	print(f'Your projected 1000m time is: {final_time}')

def oneToEight(myTime):
	time = convertToSecs(myTime)
	finalSeconds = time/1.286
	seconds_input = round(float(finalSeconds), 2)
	final_time = str(datetime.timedelta(seconds=seconds_input))
	print(f'Your projected 800m time is: {final_time}')

def sixToEight(myTime):
	time = convertToSecs(myTime)
	finalSeconds = time*1.4
	seconds_input = round(float(finalSeconds), 2)
	final_time = str(datetime.timedelta(seconds=seconds_input))
	print(f'Your projected 800m time is: {final_time}')

def eightToSix(myTime):
	time = convertToSecs(myTime)
	finalSeconds = time/1.4
	seconds_input = round(float(finalSeconds), 2)
	final_time = str(datetime.timedelta(seconds=seconds_input))
	print(f'Your projected 600m time is: {final_time}')

def threeToFour(myTime):
	time = convertToSecs(myTime)
	finalSeconds = time*1.41
	seconds_input = round(float(finalSeconds), 2)
	final_time = str(datetime.timedelta(seconds=seconds_input))
	print(f'Your projected 400m time is: {final_time}')

def fourToThree(myTime):
	time = convertToSecs(myTime)
	finalSeconds = time/1.41
	seconds_input = round(float(finalSeconds), 2)
	final_time = str(datetime.timedelta(seconds=seconds_input))
	print(f'Your projected 300m time is: {final_time}')	

#Intro to the calculator
""""
print('''
	Welcome to the running calculator!
	There are many different conversions you can do.
	Select whether you want basic or advanced conversions.

	Basic conversions are one where you don't need to enter
	an event group because conversions won't vary too much based on event group anyways.
	Examples of basic conversions are 15->mile or 1000m->800m.

	If you select advanced, you will be prompted to enter 
	your event group. Event groups are:

	800m/1500m
	800m/1500m* <-- this group is for 8/15 runners that are more on the 1500m side
	1500m
	1500m/5k 
	5k 
	5k/10k

	Enter your time using the hh:mm:ss.ms format.
	''')
"""
"""
basic_or_adv = input('\nWould you like basic or advanced conversions? ')
if basic_or_adv[0].lower() == 'b':
	print('''
		Here are the possible basic conversions:

		1500m<->1600m
		1500m<->mile
		800m<->1000m
		600m<->800m
		300m<->400m

		Enter the events you want to convert using the following format:
		ex) 1500m-mile or mile-1600m

		Do not leave spaces between the dash!

		''')

	while True:

		while True:
			basicprompt = input('What events do you want to convert? ')

			if basicprompt == '1500m-mile':
				try:
					fifteenToMile(input('Enter your 1500m time: '))
				except:
					print("Sorry, that's not a valid time. Please try again.")
					continue
				else:
					break
			elif basicprompt == 'mile-1500m':
				try:
					mileToFifteen(input('Enter your mile time: '))
				except:
					print("Sorry, that's not a valid time. Please try again.")
					continue
				else:
					break
			elif basicprompt == '1500m-1600m':
				try:
					fifteenToSixteen(input('Enter your 1500m time: '))
				except:
					print("Sorry, that's not a valid time. Please try again.")
					continue
				else:
					break
			elif basicprompt == '1600m-1500m':
				try:
					sixteenToFifteen(input('Enter your 1600m time: '))
				except:
					print("Sorry, that's not a valid time. Please try again.")
					continue
				else:
					break
			elif basicprompt == '800m-1000m':
				try:
					eightToOne(input('Enter your 800m time: '))
				except:
					print("Sorry, that's not a valid time. Please try again.")
					continue
				else:
					break
			elif basicprompt == '1000m-800m':
				try:
					oneToEight(input('Enter your 1000m time: '))
				except:
					print("Sorry, that's not a valid time. Please try again.")
					continue
				else:
					break
			elif basicprompt == '600m-800m':
				try:
					sixToEight(input('Enter your 600m time: '))
				except:
					print("Sorry, that's not a valid time. Please try again.")
					continue
				else:
					break
			elif basicprompt == '800m-600m':
				try:
					eightToSix(input('Enter your 800m time: '))
				except:
					print("Sorry, that's not a valid time. Please try again.")
					continue
				else:
					break
			elif basicprompt == '300m-400m':
				try:
					threeToFour(input('Enter your 300m time: '))
				except:
					print("Sorry, that's not a valid time. Please try again.")
					continue
				else:
					break
			elif basicprompt == '400m-300m':
				try:
					fourToThree(input('Enter your 400m time: '))
				except:
					print("Sorry, that's not a valid time. Please try again.")
					continue
				else:
					break
			else:
				print("Sorry, that's not a valid group. Please try again.")
				basicprompt = input('What events do you want to convert? ')
				continue

		replay = input('Do you want to convert more times? Enter Yes or No:  ')
		if replay[0].lower() == 'y':
			continue
		else:
			break

#Advanced conversions

else:
	print('''

		Again, possible event groups are:
		800m/1500m
		800m/1500m* <-- this group is for 8/15 runners that are more on the 1500m side
		1500m
		1500m/5k 
		5k 
		5k/10k

		Possible conversions are:
		800m<->1500m
		1500m<->3000m
		1500m<->5000m
		3000m<->5000m
		1500m<->10000m
		5000m<->10000m

		Select your conversion by using the following format:
		ex) 800m-1500m
		    1500m-3000m
		    10000m-1500m

		Enter your time using the hh:mm:ss.ms format

		'''
		)
	user1 = input('What event do you specialize in? ')

	while True:

		if user1 == '800m/1500m':
			while True:
				user1 = eightFifteen
				prompt = input('What events do you want to convert? ')
				if prompt == '800m-1500m':
					try:
						user1.eightToFifteen(input('Enter your 800m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '1500m-800m':
					try:
						user1.fifteenToEight(input('Enter your 1500m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '1500m-3000m':
					try:
						user1.fifteenToThree(input('Enter your 1500m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '3000m-1500m':
					try:
						user1.threeToFifteen(input('Enter your 3000m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '1500m-5000m':
					try:
						user1.fifteenToFive(input('Enter your 1500m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '5000m-1500m':
					try:
						user1.fiveToFifteen(input('Enter your 5000m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '3000m-5000m':
					try:
						user1.threeToFive(input('Enter your 3000m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '5000m-3000m':
					try:
						user1.fiveToThree(input('Enter your 5000m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				else:
					print("Sorry, those events cannot be converted.")
					continue
		elif user1 == '800m/1500m*':
			while True:
				user1 = eightMoreFifteen
				prompt = input('What events do you want to convert? ')
				if prompt == '800m-1500m':
					try:
						user1.eightToFifteen(input('Enter your 800m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '1500m-800m':
					try:
						user1.fifteenToEight(input('Enter your 1500m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '1500m-3000m':
					try:
						user1.fifteenToThree(input('Enter your 1500m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '3000m-1500m':
					try:
						user1.threeToFifteen(input('Enter your 3000m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '1500m-5000m':
					try:
						user1.fifteenToFive(input('Enter your 1500m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '5000m-1500m':
					try:
						user1.fiveToFifteen(input('Enter your 5000m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '3000m-5000m':
					try:
						user1.threeToFive(input('Enter your 3000m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '5000m-3000m':
					try:
						user1.fiveToThree(input('Enter your 5000m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				else:
					print("Sorry, those events cannot be converted.")
					continue
		elif user1 == '1500m':
			while True:
				user1 = pureFifteen
				prompt = input('What events do you want to convert? ')
				if prompt == '800m-1500m':
					try:
						user1.eightToFifteen(input('Enter your 800m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '1500m-800m':
					try:
						user1.fifteenToEight(input('Enter your 1500m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '1500m-3000m':
					try:
						user1.fifteenToThree(input('Enter your 1500m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '3000m-1500m':
					try:
						user1.threeToFifteen(input('Enter your 3000m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '1500m-5000m':
					try:
						user1.fifteenToFive(input('Enter your 1500m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '5000m-1500m':
					try:
						user1.fiveToFifteen(input('Enter your 5000m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '3000m-5000m':
					try:
						user1.threeToFive(input('Enter your 3000m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '5000m-3000m':
					try:
						user1.fiveToThree(input('Enter your 5000m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '5000m-10000m':
					try:
						user1.fiveToTen(input('Enter your 5000m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '10000m-5000m':
					try:
						user.tenToFive(input('Enter your 10000m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '1500m-10000m':
					try:
						user1.fifteenToTen(input('Enter your 1500m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '10000m-1500m':
					try:
						user1.tenToFifteen(input('Enter your 10000m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				else:
					print("Sorry, those events cannot be converted.")
					continue
		elif user1 == '1500m/5000m':
			while True:
				user1 = fifteenFive
				prompt = input('What events do you want to convert? ')
				if prompt == '800m-1500m':
					try:
						user1.eightToFifteen(input('Enter your 800m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '1500m-800m':
					try:
						user1.fifteenToEight(input('Enter your 1500m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '1500m-3000m':
					try:
						user1.fifteenToThree(input('Enter your 1500m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '3000m-1500m':
					try:
						user1.threeToFifteen(input('Enter your 3000m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '1500m-5000m':
					try:
						user1.fifteenToFive(input('Enter your 1500m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '5000m-1500m':
					try:
						user1.fiveToFifteen(input('Enter your 5000m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '3000m-5000m':
					try:
						user1.threeToFive(input('Enter your 3000m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '5000m-3000m':
					try:
						user1.fiveToThree(input('Enter your 5000m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '5000m-10000m':
					try:
						user1.fiveToTen(input('Enter your 5000m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '10000m-5000m':
					try:
						user.tenToFive(input('Enter your 10000m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '1500-10000m':
					try:
						user1.fifteenToTen(input('Enter your 1500m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '10000m-1500m':
					try:
						user1.tenToFifteen(input('Enter your 10000m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				else:
					print("Sorry, those events cannot be converted.")
					continue
		elif user1 == '5000m':
			while True:
				user1 = pureFive
				prompt = input('What events do you want to convert? ')
				if prompt == '800m-1500m':
					try:
						user1.eightToFifteen(input('Enter your 800m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '1500m-800m':
					try:
						user1.fifteenToEight(input('Enter your 1500m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '1500m-3000m':
					try:
						user1.fifteenToThree(input('Enter your 1500m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '3000m-1500m':
					try:
						user1.threeToFifteen(input('Enter your 3000m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '1500m-5000m':
					try:
						user1.fifteenToFive(input('Enter your 1500m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '5000m-1500m':
					try:
						user1.fiveToFifteen(input('Enter your 5000m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '3000m-5000m':
					try:
						user1.threeToFive(input('Enter your 3000m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '5000m-3000m':
					try:
						user1.fiveToThree(input('Enter your 5000m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '5000m-10000m':
					try:
						user1.fiveToTen(input('Enter your 5000m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '10000m-5000m':
					try:
						user.tenToFive(input('Enter your 10000m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '1500m-10000m':
					try:
						user1.fifteenToTen(input('Enter your 1500m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '10000m-1500m':
					try:
						user1.tenToFifteen(input('Enter your 10000m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				else:
					print("Sorry, those events cannot be converted.")
					continue
		elif user1 == '5000m/10000m':
			while True:
				user1 = fiveTen
				prompt = input('What events do you want to convert? ')
				if prompt == '800m-1500m':
					try:
						user1.eightToFifteen(input('Enter your 800m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '1500m-800m':
					try:
						user1.fifteenToEight(input('Enter your 1500m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '1500m-3000m':
					try:
						user1.fifteenToThree(input('Enter your 1500m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '3000m-1500m':
					try:
						user1.threeToFifteen(input('Enter your 3000m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '1500m-5000m':
					try:
						user1.fifteenToFive(input('Enter your 1500m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '5000m-1500m':
					try:
						user1.fiveToFifteen(input('Enter your 5000m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '3000m-5000m':
					try:
						user1.threeToFive(input('Enter your 3000m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '5000m-3000m':
					try:
						user1.fiveToThree(input('Enter your 5000m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '5000m-10000m':
					try:
						user1.fiveToTen(input('Enter your 5000m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '10000m-5000m':
					try:
						user.tenToFive(input('Enter your 10000m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '1500m-10000m':
					try:
						user1.fifteenToTen(input('Enter your 1500m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '10000m-1500m':
					try:
						user1.tenToFifteen(input('Enter your 10000m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				else:
					print("Sorry, those events cannot be converted.")
					continue
		elif user1 == '10000m':
			while True:
				user1 = pureTen
				prompt = input('What events do you want to convert? ')
				if prompt == '800m-1500m':
					try:
						user1.eightToFifteen(input('Enter your 800m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '1500m-800m':
					try:
						user1.fifteenToEight(input('Enter your 1500m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '1500m-3000m':
					try:
						user1.fifteenToThree(input('Enter your 1500m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '3000m-1500m':
					try:
						user1.threeToFifteen(input('Enter your 3000m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '1500m-5000m':
					try:
						user1.fifteenToFive(input('Enter your 1500m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '5000m-1500m':
					try:
						user1.fiveToFifteen(input('Enter your 5000m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '3000m-5000m':
					try:
						user1.threeToFive(input('Enter your 3000m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '5000m-3000m':
					try:
						user1.fiveToThree(input('Enter your 5000m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '5000m-10000m':
					try:
						user1.fiveToTen(input('Enter your 5000m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '10000m-5000m':
					try:
						user.tenToFive(input('Enter your 10000m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '1500m-10000m':
					try:
						user1.fifteenToTen(input('Enter your 1500m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				elif prompt == '10000m-1500mb':
					try:
						user1.tenToFifteen(input('Enter your 10000m time: '))
					except:
						print("Sorry, that's not a valid time. Please try again.")
						continue
					else:
						break
				else:
					print("Sorry, those events cannot be converted.")
					continue
		else:
			print("Sorry, that's not a valid group. Please try again.")
			user1 = input('What event do you specialize in? ')
			continue

		replay = input('Do you want to convert more times? Enter Yes or No:  ')
		if replay[0].lower() == 'y':
			user1 = input('What event do you specialize in? ')
			continue
		else:
			break
"""
