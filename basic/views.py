from django.shortcuts import render
from backendscript import cnvrsn as conv  
import datetime
# Create your views here.

def basic(request):
	return render(request, 'basic/basiccalc.html')

def sprint(request):

	if request.GET['events'] == "55m":
		try:
			m = request.GET['time']
			n = request.GET['time']
			i = 0
			j = 0
			finalTimes = []
			newTimes = []
			ratios = [1.0736, 1.654]
			myNewTime = [n,n]
			for times in myNewTime:
				t = myNewTime[j]
				time = conv.convertToSecs(t)
				newTimes.append(time)
				j += 1
			for times in newTimes:
				finalSeconds = times*ratios[i]
				seconds_input = round(float(finalSeconds), 2)
				t1 = str(datetime.timedelta(seconds=seconds_input))
				if '0000' in t1:
					t1 = t1.rstrip('0')
					t1 = t1.lstrip('0:')
				if '0:' in t1:
					t1 = t1.lstrip('0:')
				finalTimes.append(t1)
				i += 1
			
			return render(request, 'basic/basiccalc.html', {'60m':finalTimes[0], '100m':finalTimes[1],
			 'original':m, 'fiftyfive':m})
		
		except ValueError:
			return render(request, 'basic/basiccalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'basic/basiccalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "100m":
		try:
			m = request.GET['time']
			n = request.GET['time']
			i = 0
			j = 0
			finalTimes = []
			newTimes = []
			ratios = [0.605, 0.649, 2.009]
			myNewTime = [n,n,n]
			for times in myNewTime:
				t = myNewTime[j]
				time = conv.convertToSecs(t)
				newTimes.append(time)
				j += 1
			for times in newTimes:
				finalSeconds = times*ratios[i]
				seconds_input = round(float(finalSeconds), 2)
				t1 = str(datetime.timedelta(seconds=seconds_input))
				if '0000' in t1:
					t1 = t1.rstrip('0')
					t1 = t1.lstrip('0:')
				if '0:' in t1:
					t1 = t1.lstrip('0:')
				finalTimes.append(t1)
				i += 1
			
			return render(request, 'basic/basiccalc.html', {'55m':finalTimes[0], '60m':finalTimes[1],
			 '200m':finalTimes[2], 'original':m, 'onehundred':m})
		
		except ValueError:
			return render(request, 'basic/basiccalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'basic/basiccalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "60m":
		try:
			m = request.GET['time']
			n = request.GET['time']
			i = 0
			j = 0
			finalTimes = []
			newTimes = []
			ratios = [0.9314, 1.541]
			myNewTime = [n,n]
			for times in myNewTime:
				t = myNewTime[j]
				time = conv.convertToSecs(t)
				newTimes.append(time)
				j += 1
			for times in newTimes:
				finalSeconds = times*ratios[i]
				seconds_input = round(float(finalSeconds), 2)
				t1 = str(datetime.timedelta(seconds=seconds_input))
				if '0000' in t1:
					t1 = t1.rstrip('0')
					t1 = t1.lstrip('0:')
				if '0:' in t1:
					t1 = t1.lstrip('0:')
				finalTimes.append(t1)
				i += 1
			
			return render(request, 'basic/basiccalc.html', {'55m':finalTimes[0], '100m':finalTimes[1],
			 'original':m, 'sixty':m})
		
		except ValueError:
			return render(request, 'basic/basiccalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'basic/basiccalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "200m":
		try:
			m = request.GET['time']
			n = request.GET['time']
			i = 0
			j = 0
			finalTimes = []
			newTimes = []
			ratios = [0.498, 1.6]
			myNewTime = [n,n]
			for times in myNewTime:
				t = myNewTime[j]
				time = conv.convertToSecs(t)
				newTimes.append(time)
				j += 1
			for times in newTimes:
				finalSeconds = times*ratios[i]
				seconds_input = round(float(finalSeconds), 2)
				t1 = str(datetime.timedelta(seconds=seconds_input))
				if '0000' in t1:
					t1 = t1.rstrip('0')
					t1 = t1.lstrip('0:')
				if '0:' in t1:
					t1 = t1.lstrip('0:')
				finalTimes.append(t1)
				i += 1
			
			return render(request, 'basic/basiccalc.html', {'100m':finalTimes[0], '300m':finalTimes[1],
			 'original':m, 'twohundred':m})
		
		except ValueError:
			return render(request, 'basic/basiccalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'basic/basiccalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "300m":
		try:
			m = request.GET['time']
			n = request.GET['time']
			i = 0
			j = 0
			finalTimes = []
			newTimes = []
			ratios = [0.625, 1.3964]
			myNewTime = [n,n]
			for times in myNewTime:
				t = myNewTime[j]
				time = conv.convertToSecs(t)
				newTimes.append(time)
				j += 1
			for times in newTimes:
				finalSeconds = times*ratios[i]
				seconds_input = round(float(finalSeconds), 2)
				t1 = str(datetime.timedelta(seconds=seconds_input))
				if '0000' in t1:
					t1 = t1.rstrip('0')
					t1 = t1.lstrip('0:')
				if '0:' in t1:
					t1 = t1.lstrip('0:')
				finalTimes.append(t1)
				i += 1
			
			return render(request, 'basic/basiccalc.html', {'200m':finalTimes[0], '400m':finalTimes[1],
			 'original':m, 'threehundred':m})
		
		except ValueError:
			return render(request, 'basic/basiccalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'basic/basiccalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "400m":
		try:
			m = request.GET['time']
			n = request.GET['time']
			i = 0
			j = 0
			finalTimes = []
			newTimes = []
			ratios = [0.7302, 1.32, 1.66, 2.34]
			myNewTime = [n,n,n,n]
			for times in myNewTime:
				t = myNewTime[j]
				time = conv.convertToSecs(t)
				newTimes.append(time)
				j += 1
			for times in newTimes:
				finalSeconds = times*ratios[i]
				seconds_input = round(float(finalSeconds), 2)
				t1 = str(datetime.timedelta(seconds=seconds_input))
				if '0000' in t1:
					t1 = t1.rstrip('0')
					t1 = t1.lstrip('0:')
				if '0:' in t1:
					t1 = t1.lstrip('0:')
				finalTimes.append(t1)
				i += 1
			
			return render(request, 'basic/basiccalc.html', {'300m':finalTimes[0], '500m':finalTimes[1],
			  '600m':finalTimes[2], '800m':finalTimes[3], 'original':m, 'fourhundred':m})
		
		except ValueError:
			return render(request, 'basic/basiccalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'basic/basiccalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "500m":
		try:
			m = request.GET['time']
			n = request.GET['time']
			i = 0
			j = 0
			finalTimes = []
			newTimes = []
			ratios = [0.758, 1.258, 1.774]
			myNewTime = [n,n,n]
			for times in myNewTime:
				t = myNewTime[j]
				time = conv.convertToSecs(t)
				newTimes.append(time)
				j += 1
			for times in newTimes:
				finalSeconds = times*ratios[i]
				seconds_input = round(float(finalSeconds), 2)
				t1 = str(datetime.timedelta(seconds=seconds_input))
				if '0000' in t1:
					t1 = t1.rstrip('0')
					t1 = t1.lstrip('0:')
				if '0:' in t1:
					t1 = t1.lstrip('0:')
				finalTimes.append(t1)
				i += 1
			
			return render(request, 'basic/basiccalc.html', {'400m':finalTimes[0], '600m':finalTimes[1],
			 '800m':finalTimes[2] ,'original':m, 'fivehundred':m})
		
		except ValueError:
			return render(request, 'basic/basiccalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'basic/basiccalc.html', {'error':'Invalid time'})

def distance(request):

	if request.GET['events'] == "600m":
		try:
			m = request.GET['time']
			n = request.GET['time']
			i = 0
			j = 0
			finalTimes = []
			newTimes = []
			ratios = [0.62, 0.812, 1.4, 1.8]
			myNewTime = [n,n,n,n]
			for times in myNewTime:
				t = myNewTime[j]
				time = conv.convertToSecs(t)
				newTimes.append(time)
				j += 1
			for times in newTimes:
				finalSeconds = times*ratios[i]
				seconds_input = round(float(finalSeconds), 2)
				t1 = str(datetime.timedelta(seconds=seconds_input))
				if '0000' in t1:
					t1 = t1.rstrip('0')
					t1 = t1.lstrip('0:')
				if '0:' in t1:
					t1 = t1.lstrip('0:')
				finalTimes.append(t1)
				i += 1
			
			return render(request, 'basic/basiccalc.html', {'400m':finalTimes[0], '500m':finalTimes[1],
			'800m':finalTimes[2], '1000m':finalTimes[3], 'original':m, 'sixhundred':m})
		
		except ValueError:
			return render(request, 'basic/basiccalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'basic/basiccalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "800m":
		try:
			m = request.GET['time']
			n = request.GET['time']
			i = 0
			j = 0
			finalTimes = []
			newTimes = []
			ratios = [0.443, 0.714, 1.286, 2.048, 2.191, 2.212]
			myNewTime = [n,n,n,n,n,n]
			for times in myNewTime:
				t = myNewTime[j]
				time = conv.convertToSecs(t)
				newTimes.append(time)
				j += 1
			for times in newTimes:
				finalSeconds = times*ratios[i]
				seconds_input = round(float(finalSeconds), 2)
				t1 = str(datetime.timedelta(seconds=seconds_input))
				if '0000' in t1:
					t1 = t1.rstrip('0')
					t1 = t1.lstrip('0:')
				if '0:' in t1:
					t1 = t1.lstrip('0:')
				finalTimes.append(t1)
				i += 1
			
			return render(request, 'basic/basiccalc.html', {'400m':finalTimes[0], '600m':finalTimes[1],
			'1000m':finalTimes[2], '1500m':finalTimes[3], '1600m':finalTimes[4], 'Mile':finalTimes[5], 'original':m, 'eighthundred':m})
		
		except ValueError:
			return render(request, 'basic/basiccalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'basic/basiccalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "1000m":
		try:
			m = request.GET['time']
			n = request.GET['time']
			i = 0
			j = 0
			finalTimes = []
			newTimes = []
			ratios = [0.555, 0.7776, 1.593, 1.7045, 1.7204]
			myNewTime = [n,n,n,n,n]
			for times in myNewTime:
				t = myNewTime[j]
				time = conv.convertToSecs(t)
				newTimes.append(time)
				j += 1
			for times in newTimes:
				finalSeconds = times*ratios[i]
				seconds_input = round(float(finalSeconds), 2)
				t1 = str(datetime.timedelta(seconds=seconds_input))
				if '0000' in t1:
					t1 = t1.rstrip('0')
					t1 = t1.lstrip('0:')
				if '0:' in t1:
					t1 = t1.lstrip('0:')
				finalTimes.append(t1)
				i += 1
			
			return render(request, 'basic/basiccalc.html', {'600m':finalTimes[0], '800m':finalTimes[1],
			'1500m':finalTimes[2], '1600m':finalTimes[3], 'Mile':finalTimes[4], 'original':m, 'onethousand':m})
		
		except ValueError:
			return render(request, 'basic/basiccalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'basic/basiccalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "1500m":
		try:
			m = request.GET['time']
			n = request.GET['time']
			i = 0
			j = 0
			finalTimes = []
			newTimes = []
			ratios = [0.488, 0.623, 1.07, 1.08, 1.36, 2.13, 2.287, 2.3, 3.59, 3.771]
			myNewTime = [n,n,n,n,n,n,n,n,n,n]
			for times in myNewTime:
				t = myNewTime[j]
				time = conv.convertToSecs(t)
				newTimes.append(time)
				j += 1
			for times in newTimes:
				finalSeconds = times*ratios[i]
				seconds_input = round(float(finalSeconds), 2)
				t1 = str(datetime.timedelta(seconds=seconds_input))
				if '0000' in t1:
					t1 = t1.rstrip('0')
					t1 = t1.lstrip('0:')
				if '0:' in t1:
					t1 = t1.lstrip('0:')
				finalTimes.append(t1)
				i += 1
			
			return render(request, 'basic/basiccalc.html', {'800m':finalTimes[0], '1000m':finalTimes[1],
			'1600m':finalTimes[2], 'Mile':finalTimes[3], '2000m':finalTimes[4], '3000m':finalTimes[5],
			'3200m':finalTimes[6], '2mile':finalTimes[7], '3mile':finalTimes[8],
			'5000m':finalTimes[9], 'original':m, 'fifteenhundred':m})
		
		except ValueError:
			return render(request, 'basic/basiccalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'basic/basiccalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "1600m":
		try:
			m = request.GET['time']
			n = request.GET['time']
			i = 0
			j = 0
			finalTimes = []
			newTimes = []
			ratios = [0.456, 0.587, 0.9346, 1.009, 1.271, 1.991, 2.137, 2.15, 3.355, 3.524]
			myNewTime = [n,n,n,n,n,n,n,n,n,n]
			for times in myNewTime:
				t = myNewTime[j]
				time = conv.convertToSecs(t)
				newTimes.append(time)
				j += 1
			for times in newTimes:
				finalSeconds = times*ratios[i]
				seconds_input = round(float(finalSeconds), 2)
				t1 = str(datetime.timedelta(seconds=seconds_input))
				if '0000' in t1:
					t1 = t1.rstrip('0')
					t1 = t1.lstrip('0:')
				if '0:' in t1:
					t1 = t1.lstrip('0:')
				finalTimes.append(t1)
				i += 1
			
			return render(request, 'basic/basiccalc.html', {'800m':finalTimes[0], '1000m':finalTimes[1],
			'1500m':finalTimes[2], 'Mile':finalTimes[3], '2000m':finalTimes[4], '3000m':finalTimes[5],
			'3200m':finalTimes[6], '2mile':finalTimes[7], '3mile':finalTimes[8],
			'5000m':finalTimes[9], 'original':m, 'sixteenhundred':m})
		
		except ValueError:
			return render(request, 'basic/basiccalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'basic/basiccalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "Mile":
		try:
			m = request.GET['time']
			n = request.GET['time']
			i = 0
			j = 0
			finalTimes = []
			newTimes = []
			ratios = [0.452, 0.581, 0.9259, 0.991, 1.259, 1.972, 2.118, 2.13, 3.324, 3.492]
			myNewTime = [n,n,n,n,n,n,n,n,n,n]
			for times in myNewTime:
				t = myNewTime[j]
				time = conv.convertToSecs(t)
				newTimes.append(time)
				j += 1
			for times in newTimes:
				finalSeconds = times*ratios[i]
				seconds_input = round(float(finalSeconds), 2)
				t1 = str(datetime.timedelta(seconds=seconds_input))
				if '0000' in t1:
					t1 = t1.rstrip('0')
					t1 = t1.lstrip('0:')
				if '0:' in t1:
					t1 = t1.lstrip('0:')
				finalTimes.append(t1)
				i += 1
			
			return render(request, 'basic/basiccalc.html', {'800m':finalTimes[0], '1000m':finalTimes[1],
			'1500m':finalTimes[2], '1600m':finalTimes[3], '2000m':finalTimes[4], '3000m':finalTimes[5],
			'3200m':finalTimes[6], '2mile':finalTimes[7], '3mile':finalTimes[8],
			'5000m':finalTimes[9], 'original':m, 'mileres':m})
		
		except ValueError:
			return render(request, 'basic/basiccalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'basic/basiccalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "2000m":
		try:
			m = request.GET['time']
			n = request.GET['time']
			i = 0
			j = 0
			finalTimes = []
			newTimes = []
			ratios = [0.735, 0.787, 0.794, 1.572, 1.681, 1.698, 2.639, 2.703]
			myNewTime = [n,n,n,n,n,n,n,n]
			for times in myNewTime:
				t = myNewTime[j]
				time = conv.convertToSecs(t)
				newTimes.append(time)
				j += 1
			for times in newTimes:
				finalSeconds = times*ratios[i]
				seconds_input = round(float(finalSeconds), 2)
				t1 = str(datetime.timedelta(seconds=seconds_input))
				if '0000' in t1:
					t1 = t1.rstrip('0')
					t1 = t1.lstrip('0:')
				if '0:' in t1:
					t1 = t1.lstrip('0:')
				finalTimes.append(t1)
				i += 1
			
			return render(request, 'basic/basiccalc.html', {'1500m':finalTimes[0], '1600m':finalTimes[1],
			'Mile':finalTimes[2], '3000m':finalTimes[3], '3200m':finalTimes[4], '2mile':finalTimes[5],
			'3mile':finalTimes[6], '5000m':finalTimes[7], 'original':m, 'twothousand':m})
		
		except ValueError:
			return render(request, 'basic/basiccalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'basic/basiccalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "3000m":
		try:
			m = request.GET['time']
			n = request.GET['time']
			i = 0
			j = 0
			finalTimes = []
			newTimes = []
			ratios = [0.468, 0.501, 0.505, 0.636, 1.07, 1.08, 1.681, 1.740, 3.654]
			myNewTime = [n,n,n,n,n,n,n,n,n]
			for times in myNewTime:
				t = myNewTime[j]
				time = conv.convertToSecs(t)
				newTimes.append(time)
				j += 1
			for times in newTimes:
				finalSeconds = times*ratios[i]
				seconds_input = round(float(finalSeconds), 2)
				t1 = str(datetime.timedelta(seconds=seconds_input))
				if '0000' in t1:
					t1 = t1.rstrip('0')
					t1 = t1.lstrip('0:')
				if '0:' in t1:
					t1 = t1.lstrip('0:')
				finalTimes.append(t1)
				i += 1
			
			return render(request, 'basic/basiccalc.html', {'1500m':finalTimes[0], '1600m':finalTimes[1],
			'Mile':finalTimes[2], '2000m':finalTimes[3], '3200m':finalTimes[4], '2mile':finalTimes[5],
			'3mile':finalTimes[6], '5000m':finalTimes[7], '10000m':finalTimes[8], 'original':m, 'threethousand':m})
		
		except ValueError:
			return render(request, 'basic/basiccalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'basic/basiccalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "3200m":
		try:
			m = request.GET['time']
			n = request.GET['time']
			i = 0
			j = 0
			finalTimes = []
			newTimes = []
			ratios = [0.437, 0.468, 0.472, 0.595, 0.935, 1.01, 1.572, 1.627, 3.416]
			myNewTime = [n,n,n,n,n,n,n,n,n]
			for times in myNewTime:
				t = myNewTime[j]
				time = conv.convertToSecs(t)
				newTimes.append(time)
				j += 1
			for times in newTimes:
				finalSeconds = times*ratios[i]
				seconds_input = round(float(finalSeconds), 2)
				t1 = str(datetime.timedelta(seconds=seconds_input))
				if '0000' in t1:
					t1 = t1.rstrip('0')
					t1 = t1.lstrip('0:')
				if '0:' in t1:
					t1 = t1.lstrip('0:')
				finalTimes.append(t1)
				i += 1
			
			return render(request, 'basic/basiccalc.html', {'1500m':finalTimes[0], '1600m':finalTimes[1],
			'Mile':finalTimes[2], '2000m':finalTimes[3], '3000m':finalTimes[4], '2mile':finalTimes[5],
			'3mile':finalTimes[6], '5000m':finalTimes[7], '10000m':finalTimes[8], 'original':m, 'thirtytwohundred':m})
		
		except ValueError:
			return render(request, 'basic/basiccalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'basic/basiccalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "2mile":
		try:
			m = request.GET['time']
			n = request.GET['time']
			i = 0
			j = 0
			finalTimes = []
			newTimes = []
			ratios = [0.435, 0.465, 0.470, 0.589, 0.926, 0.99, 1.562, 1.605, 3.382]
			myNewTime = [n,n,n,n,n,n,n,n,n]
			for times in myNewTime:
				t = myNewTime[j]
				time = conv.convertToSecs(t)
				newTimes.append(time)
				j += 1
			for times in newTimes:
				finalSeconds = times*ratios[i]
				seconds_input = round(float(finalSeconds), 2)
				t1 = str(datetime.timedelta(seconds=seconds_input))
				if '0000' in t1:
					t1 = t1.rstrip('0')
					t1 = t1.lstrip('0:')
				if '0:' in t1:
					t1 = t1.lstrip('0:')
				finalTimes.append(t1)
				i += 1
			
			return render(request, 'basic/basiccalc.html', {'1500m':finalTimes[0], '1600m':finalTimes[1],
			'Mile':finalTimes[2], '2000m':finalTimes[3], '3000m':finalTimes[4], '3200m':finalTimes[5],
			'3mile':finalTimes[6], '5000m':finalTimes[7], '10000m':finalTimes[8], 'original':m, 'twomile':m})
		
		except ValueError:
			return render(request, 'basic/basiccalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'basic/basiccalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "3mile":
		try:
			m = request.GET['time']
			n = request.GET['time']
			i = 0
			j = 0
			finalTimes = []
			newTimes = []
			ratios = [0.279, 0.298, 0.301, 0.379, 0.595, 0.636, 0.640, 1.028, 2.223]
			myNewTime = [n,n,n,n,n,n,n,n,n]
			for times in myNewTime:
				t = myNewTime[j]
				time = conv.convertToSecs(t)
				newTimes.append(time)
				j += 1
			for times in newTimes:
				finalSeconds = times*ratios[i]
				seconds_input = round(float(finalSeconds), 2)
				t1 = str(datetime.timedelta(seconds=seconds_input))
				if '0000' in t1:
					t1 = t1.rstrip('0')
					t1 = t1.lstrip('0:')
				if '0:' in t1:
					t1 = t1.lstrip('0:')
				finalTimes.append(t1)
				i += 1
			
			return render(request, 'basic/basiccalc.html', {'1500m':finalTimes[0], '1600m':finalTimes[1],
			'Mile':finalTimes[2], '2000m':finalTimes[3], '3000m':finalTimes[4], '3200m':finalTimes[5],
			'2mile':finalTimes[6], '5000m':finalTimes[7], '10000m':finalTimes[8], 'original':m, 'threemile':m})
		
		except ValueError:
			return render(request, 'basic/basiccalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'basic/basiccalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "5000m":
		try:
			m = request.GET['time']
			n = request.GET['time']
			i = 0
			j = 0
			finalTimes = []
			newTimes = []
			ratios = [0.272, 0.291, 0.294, 0.370, 0.577, 0.617, 0.623, 0.973, 2.159]
			myNewTime = [n,n,n,n,n,n,n,n,n]
			for times in myNewTime:
				t = myNewTime[j]
				time = conv.convertToSecs(t)
				newTimes.append(time)
				j += 1
			for times in newTimes:
				finalSeconds = times*ratios[i]
				seconds_input = round(float(finalSeconds), 2)
				t1 = str(datetime.timedelta(seconds=seconds_input))
				if '0000' in t1:
					t1 = t1.rstrip('0')
					t1 = t1.lstrip('0:')
				if '0:' in t1:
					t1 = t1.lstrip('0:')
				finalTimes.append(t1)
				i += 1
			
			return render(request, 'basic/basiccalc.html', {'1500m':finalTimes[0], '1600m':finalTimes[1],
			'Mile':finalTimes[2], '2000m':finalTimes[3], '3000m':finalTimes[4], '3200m':finalTimes[5],
			'2mile':finalTimes[6], '3mile':finalTimes[7], '10000m':finalTimes[8], 'original':m, 'fivethousand':m})
		
		except ValueError:
			return render(request, 'basic/basiccalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'basic/basiccalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "10000m":
		try:
			m = request.GET['time']
			n = request.GET['time']
			i = 0
			j = 0
			finalTimes = []
			newTimes = []
			ratios = [0.274, 0.293, 0.296, 0.450, 0.463]
			myNewTime = [n,n,n,n,n]
			for times in myNewTime:
				t = myNewTime[j]
				time = conv.convertToSecs(t)
				newTimes.append(time)
				j += 1
			for times in newTimes:
				finalSeconds = times*ratios[i]
				seconds_input = round(float(finalSeconds), 2)
				t1 = str(datetime.timedelta(seconds=seconds_input))
				if '0000' in t1:
					t1 = t1.rstrip('0')
					t1 = t1.lstrip('0:')
				if '0:' in t1:
					t1 = t1.lstrip('0:')
				finalTimes.append(t1)
				i += 1
			
			return render(request, 'basic/basiccalc.html', {'3000m':finalTimes[0], '3200m':finalTimes[1],
			'2mile':finalTimes[2], '3mile':finalTimes[3], '5000m':finalTimes[4], 'original':m, 'tenthousand':m})
		
		except ValueError:
			return render(request, 'basic/basiccalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'basic/basiccalc.html', {'error':'Invalid time'})