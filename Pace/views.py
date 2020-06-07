from django.shortcuts import render
from backendscript import cnvrsn as conv
import datetime
# Create your views here.

def pace(request):
	return render(request, 'Pace/pacecalc.html')

def calculatepace(request):
	
	if request.GET['type'] == 'Miles':
		try:
			t =  request.GET['time']
			t1 =  request.GET['time']
			t2 =  request.GET['time']
			dm = float(request.GET['distance'])
			dk = float(request.GET['distance'])*1.609
			newTime1 = conv.convertToSecs(t1)
			newTime2 = conv.convertToSecs(t2)
			km = newTime1/dk
			mi = newTime2/dm
			seconds_input = round(float(km), 2)
			perkm = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in perkm:
				perkm = perkm.rstrip('0')
				perkm = perkm.lstrip('0:')
			if '0:' in perkm:
				perkm = perkm.lstrip('0:')

			seconds_input = round(float(mi), 2)
			permile = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in permile:
				permile = permile.rstrip('0')
				permile = permile.lstrip('0:')
			if '0:' in permile:
				permile = permile.lstrip('0:')

			return render(request, 'Pace/pacecalc.html', {'permile':permile, 'perkm':perkm, 'goaltimemiles':t, 'distance':dm})

		except ValueError:
			return render(request, 'Pace/pacecalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Pace/pacecalc.html', {'error':'Invalid time'})

	if request.GET['type'] == 'Km':
		try:
			t =  request.GET['time']
			t1 =  request.GET['time']
			t2 =  request.GET['time']
			dk = float(request.GET['distance'])
			dm = float(request.GET['distance'])/1.609
			newTime1 = conv.convertToSecs(t1)
			newTime2 = conv.convertToSecs(t2)
			km = newTime1/dk
			mi = newTime2/dm
			seconds_input = round(float(km), 2)
			perkm = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in perkm:
				perkm = perkm.rstrip('0')
				perkm = perkm.lstrip('0:')
			if '0:' in perkm:
				perkm = perkm.lstrip('0:')

			seconds_input = round(float(mi), 2)
			permile = str(datetime.timedelta(seconds=seconds_input))
			if '0000' in permile:
				permile = permile.rstrip('0')
				permile = permile.lstrip('0:')
			if '0:' in permile:
				permile = permile.lstrip('0:')

			return render(request, 'Pace/pacecalc.html', {'permile':permile, 'perkm':perkm, 'goaltimekm':t, 'distance':dk})

		except ValueError:
			return render(request, 'Pace/pacecalc.html', {'error':'Invalid time'})
		except IndexError:
			return render(request, 'Pace/pacecalc.html', {'error':'Invalid time'})

def calculatesplits(request):
	if request.GET['type'] == 'M':
		if request.GET['splittype'] == 'M':
			try:
				split_mm = request.GET['splittype']
				t =  request.GET['time']
				t1 =  request.GET['time']
				splitd = request.GET['splitdistance']
				fulld = request.GET['distance']
				rd = float(request.GET['distance'])
				sd =  float(request.GET['splitdistance'])
				nos = rd/sd
				newTime1 = conv.convertToSecs(t1)
				st = newTime1/nos
				seconds_input = round(float(st), 2)
				split_t = str(datetime.timedelta(seconds=seconds_input))
				if '0000' in split_t:
					split_t = split_t.rstrip('0')
					split_t = split_t.lstrip('0:')
				if '0:' in split_t:
					split_t = split_t.lstrip('0:')


				return render(request, 'Pace/pacecalc.html', {'original':t, 'originald':fulld, 'split_t':split_t, 'splitd':splitd, 'split_mm':split_mm})

			except ValueError:
				return render(request, 'Pace/pacecalc.html', {'error':'Invalid time'})
			except IndexError:
				return render(request, 'Pace/pacecalc.html', {'error':'Invalid time'})

	if request.GET['type'] == 'Km':
		if request.GET['splittype'] == 'M':
			try:
				split_kmm = request.GET['splittype']
				t =  request.GET['time']
				t1 =  request.GET['time']
				splitd = request.GET['splitdistance']
				fulld = request.GET['distance']
				rd = float(request.GET['distance'])*1000
				sd =  float(request.GET['splitdistance'])
				nos = rd/sd
				newTime1 = conv.convertToSecs(t1)
				st = newTime1/nos
				seconds_input = round(float(st), 2)
				split_t = str(datetime.timedelta(seconds=seconds_input))
				if '0000' in split_t:
					split_t = split_t.rstrip('0')
					split_t = split_t.lstrip('0:')
				if '0:' in split_t:
					split_t = split_t.lstrip('0:')


				return render(request, 'Pace/pacecalc.html', {'original':t, 'originald':fulld, 'split_t':split_t, 'splitd':splitd, 'split_kmm':split_kmm})

			except ValueError:
				return render(request, 'Pace/pacecalc.html', {'error':'Invalid time'})
			except IndexError:
				return render(request, 'Pace/pacecalc.html', {'error':'Invalid time'})

	if request.GET['type'] == 'Miles':
		if request.GET['splittype'] == 'M':
			try:
				split_mim = request.GET['splittype']
				t =  request.GET['time']
				t1 =  request.GET['time']
				splitd = request.GET['splitdistance']
				fulld = request.GET['distance']
				rd = float(request.GET['distance'])*1609
				sd =  float(request.GET['splitdistance'])
				nos = rd/sd
				newTime1 = conv.convertToSecs(t1)
				st = newTime1/nos
				seconds_input = round(float(st), 2)
				split_t = str(datetime.timedelta(seconds=seconds_input))
				if '0000' in split_t:
					split_t = split_t.rstrip('0')
					split_t = split_t.lstrip('0:')
				if '0:' in split_t:
					split_t = split_t.lstrip('0:')


				return render(request, 'Pace/pacecalc.html', {'original':t, 'originald':fulld, 'split_t':split_t, 'splitd':splitd, 'split_mim':split_mim})

			except ValueError:
				return render(request, 'Pace/pacecalc.html', {'error':'Invalid time'})
			except IndexError:
				return render(request, 'Pace/pacecalc.html', {'error':'Invalid time'})