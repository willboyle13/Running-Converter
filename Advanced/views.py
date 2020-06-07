from django.shortcuts import render
from backendscript import cnvrsn as conv
import datetime
# Create your views here.

def advanced(request):
	return render(request, 'Advanced/advcalc.html')

def eightFift(request):
	if request.GET['events'] == "800m-1500m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t*2.048
			seconds_input = round(float(finalSecs), 2)
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "1500m-800m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t/2.048
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "1500m-3000m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t*2.183
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "3000m-1500m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t/2.183
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "1500m-5000m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t*3.849
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "5000m-1500m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t/3.849
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
	
	if request.GET['events'] == "3000m-5000m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t*1.763
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "5000m-3000m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t/1.763
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

def eightMoreFift(request):
	if request.GET['events'] == "800m-1500m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t*2.034
			seconds_input = round(float(finalSecs), 2)
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "1500m-800m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t/2.034
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "1500m-3000m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t*2.169
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "3000m-1500m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t/2.169
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "1500m-5000m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t*3.810
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "5000m-1500m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t/3.810
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
	
	if request.GET['events'] == "3000m-5000m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t*1.756
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "5000m-3000m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t/1.756
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

def fifteen(request):
	if request.GET['events'] == "800m-1500m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t*2.020
			seconds_input = round(float(finalSecs), 2)
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "1500m-800m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t/2.020
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "1500m-3000m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t*2.155
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "3000m-1500m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t/2.155
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "1500m-5000m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t*3.771
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "5000m-1500m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t/3.771
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
	
	if request.GET['events'] == "3000m-5000m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t*1.750
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "5000m-3000m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t/1.750
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "5000m-10000m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t*2.115
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "10000m-5000m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t/2.115
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "1500m-10000m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t*7.967
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "10000m-1500m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t/7.967
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

def fifteenFive(request):
	if request.GET['events'] == "800m-1500m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t*2.000
			seconds_input = round(float(finalSecs), 2)
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "1500m-800m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t/2.000
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "1500m-3000m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t*2.135
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "3000m-1500m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t/2.135
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "1500m-5000m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t*3.714
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "5000m-1500m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t/3.714
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
	
	if request.GET['events'] == "3000m-5000m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t*1.740
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "5000m-3000m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t/1.740
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "5000m-10000m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t*2.100
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "10000m-5000m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t/2.100
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "1500m-10000m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t*7.799
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "10000m-1500m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t/7.799
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

def five(request):
	if request.GET['events'] == "800m-1500m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t*1.989
			seconds_input = round(float(finalSecs), 2)
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "1500m-800m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t/1.989
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "1500m-3000m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t*2.124
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "3000m-1500m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t/2.124
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "1500m-5000m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t*3.683
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "5000m-1500m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t/3.683
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
	
	if request.GET['events'] == "3000m-5000m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t*1.734
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "5000m-3000m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t/1.734
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "5000m-10000m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t*2.092
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "10000m-5000m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t/2.092
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "1500m-10000m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t*7.707
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "10000m-1500m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t/7.707
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

def fiveTen(request):
	if request.GET['events'] == "800m-1500m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t*1.978
			seconds_input = round(float(finalSecs), 2)
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "1500m-800m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t/1.978
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "1500m-3000m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t*2.113
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "3000m-1500m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t/2.113
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "1500m-5000m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t*3.652
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "5000m-1500m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t/3.652
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
	
	if request.GET['events'] == "3000m-5000m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t*1.728
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "5000m-3000m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t/1.728
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "5000m-10000m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t*2.084
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "10000m-5000m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t/2.084
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "1500m-10000m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t*7.615
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "10000m-1500m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t/7.615
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

def ten(request):
	if request.GET['events'] == "800m-1500m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t*1.968
			seconds_input = round(float(finalSecs), 2)
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "1500m-800m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t/1.968
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "1500m-3000m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t*2.102
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "3000m-1500m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t/2.102
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "1500m-5000m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t*3.621
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "5000m-1500m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t/3.621
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
	
	if request.GET['events'] == "3000m-5000m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t*1.722
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "5000m-3000m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t/1.722
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "5000m-10000m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t*2.076
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "10000m-5000m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t/2.076
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "1500m-10000m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t*7.523
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})

	if request.GET['events'] == "10000m-1500m":
		try:
			m = request.GET['time']
			m2 = request.GET['time']
			t = conv.convertToSecs(m)
			finalSecs = t/7.523
			seconds_input = float(round(float(finalSecs), 2))
			t1 = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in t1:
				t1 = t1.rstrip('0')
			t1 = t1.lstrip('0:')
			return render(request, 'Advanced/advcalc.html', {'result':t1, 'original':m2})
		except ValueError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Advanced/advcalc.html', {'error':'Invalid time'})