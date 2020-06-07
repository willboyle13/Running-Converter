from django.shortcuts import render
from backendscript import cnvrsn as conv  
import datetime
# Create your views here.

def track(request):
    return render(request, 'track/trackcalc.html')

def mens(request):
    if request.GET['tracktype'] == "Undersized":
        if request.GET['events'] == "200m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [0.9872, 0.9698]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'undertwohundred':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "300m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [0.9890, 0.9727]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'underthreehundred':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "400m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [0.9901, 0.9746]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'underfourhundred':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "500m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [0.9909, 0.9758]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'underfivehundred':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "600y":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [0.9912, 0.9763]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'undersixhundredy':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "600m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [0.9915, 0.9768]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'undersixhundred':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "800m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [0.9923, 0.9783]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'undereighthundred':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})  

        if request.GET['events'] == "1000m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [0.9929, 0.9794]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'underonethousand':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "1500m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [0.9939, 0.9812]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'underfifteenhundred':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "Mile":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [0.9941, 0.9816]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'undermile':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "3000m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [0.9953, 0.9839]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'underthreethousand':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "5000m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [0.9961, 0.9855]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'underfivethousand':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "4x200m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [0.9872, 0.9698]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'underfourbytwo':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "4x400m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [0.9901, 0.9746]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'underfourbyfour':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "4x800m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [0.9923, 0.9783]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'underfourbyeight':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "DMR":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [0.9931, 0.9798]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'underDMR':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

    if request.GET['tracktype'] == "Flat":
        if request.GET['events'] == "200m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.013, 0.9824]
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
                
                return render(request, 'track/trackcalc.html', {'Undersized':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'flattwohundred':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "300m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.0111, 0.9835]
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
                
                return render(request, 'track/trackcalc.html', {'Undersized':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'flatthreehundred':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "400m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.01, 0.9843]
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
                
                return render(request, 'track/trackcalc.html', {'Undersized':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'flatfourhundred':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "500m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.009, 0.9848]
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
                
                return render(request, 'track/trackcalc.html', {'Undersized':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'flatfivehundred':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "600y":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.009, 0.9850]
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
                
                return render(request, 'track/trackcalc.html', {'Undersized':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'flatsixhundredy':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "600m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.0086, 0.9852]
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
                
                return render(request, 'track/trackcalc.html', {'Undersized':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'flatsixhundred':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "800m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.0078, 0.9859]
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
                
                return render(request, 'track/trackcalc.html', {'Undersized':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'flateighthundred':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})  

        if request.GET['events'] == "1000m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.007, 0.9864]
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
                
                return render(request, 'track/trackcalc.html', {'Undersized':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'flatonethousand':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "1500m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.0061, 0.9872]
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
                
                return render(request, 'track/trackcalc.html', {'Undersized':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'flatfifteenhundred':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "Mile":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.006, 0.9874]
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
                
                return render(request, 'track/trackcalc.html', {'Undersized':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'flatmile':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "3000m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.0047, 0.9885]
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
                
                return render(request, 'track/trackcalc.html', {'Undersized':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'flatthreethousand':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "5000m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.004, 0.9894]
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
                
                return render(request, 'track/trackcalc.html', {'Undersized':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'flatfivethousand':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "4x200m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.013, 0.9824]
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
                
                return render(request, 'track/trackcalc.html', {'Undersized':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'flatfourbytwo':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "4x400m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.01, 0.9843]
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
                
                return render(request, 'track/trackcalc.html', {'Undersized':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'flatfourbyfour':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "4x800m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.008, 0.9859]
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
                
                return render(request, 'track/trackcalc.html', {'Undersized':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'flatfourbyeight':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "DMR":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.007, 0.9866]
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
                
                return render(request, 'track/trackcalc.html', {'Undersized':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'FlatDMR':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

    if request.GET['tracktype'] == "BOS":
        if request.GET['events'] == "200m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.0179, 1.0311]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'Undersized':finalTimes[1],
                 'original':m, 'bostwohundred':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "300m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.0168, 1.0281]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'Undersized':finalTimes[1],
                 'original':m, 'bosthreehundred':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "400m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.0160, 1.0261]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'Undersized':finalTimes[1],
                 'original':m, 'bosfourhundred':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "500m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.0154, 1.0248]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'Undersized':finalTimes[1],
                 'original':m, 'bosfivehundred':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "600y":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.0152, 1.0243]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'Undersized':finalTimes[1],
                 'original':m, 'bossixhundredy':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "600m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.0150, 1.0238]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'Undersized':finalTimes[1],
                 'original':m, 'bossixhundred':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "800m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.0143, 1.0222]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'Undersized':finalTimes[1],
                 'original':m, 'boseighthundred':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})  

        if request.GET['events'] == "1000m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.0138, 1.021]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'Undersized':finalTimes[1],
                 'original':m, 'bosonethousand':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "1500m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.013, 1.0191]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'Undersized':finalTimes[1],
                 'original':m, 'bosfifteenhundred':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "Mile":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.0128, 1.0187]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'Undersized':finalTimes[1],
                 'original':m, 'bosmile':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "3000m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.0116, 1.0164]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'Undersized':finalTimes[1],
                 'original':m, 'bosthreethousand':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "5000m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.0107, 1.0147]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'Undersized':finalTimes[1],
                 'original':m, 'bosfivethousand':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "4x200m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.0179, 1.0311]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'Undersized':finalTimes[1],
                 'original':m, 'bosfourbytwo':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "4x400m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.0160, 1.0261]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'Undersized':finalTimes[1],
                 'original':m, 'bosfourbyfour':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "4x800m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.0143, 1.0222]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'Undersized':finalTimes[1],
                 'original':m, 'bosfourbyeight':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "DMR":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.0136, 1.0206]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'Undersized':finalTimes[1],
                 'original':m, 'bosDMR':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

def womens(request):
    if request.GET['tracktype'] == "Undersized":
        if request.GET['events'] == "200m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [0.9900, 0.9749]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'undertwohundred':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "300m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [0.9918, 0.9779]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'underthreehundred':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "400m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [0.9929, 0.9799]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'underfourhundred':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "500m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [0.9937, 0.9812]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'underfivehundred':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "600y":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [0.9940, 0.9818]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'undersixhundredy':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "600m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [0.9943, 0.9823]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'undersixhundred':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "800m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [0.9951, 0.9838]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'undereighthundred':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})  

        if request.GET['events'] == "1000m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [0.9958, 0.9850]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'underonethousand':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "1500m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [0.9967, 0.9868]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'underfifteenhundred':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "Mile":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [0.9969, 0.9871]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'undermile':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "3000m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [0.9981, 0.9896]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'underthreethousand':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "5000m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [0.9989, 0.9913]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'underfivethousand':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "4x200m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [0.9900, 0.9749]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'underfourbytwo':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "4x400m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [0.9929, 0.9799]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'underfourbyfour':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "4x800m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [0.9951, 0.9838]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'underfourbyeight':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "DMR":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [0.9959, 0.9853]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'underDMR':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

    if request.GET['tracktype'] == "Flat":
        if request.GET['events'] == "200m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.0111, 0.9847]
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
                
                return render(request, 'track/trackcalc.html', {'Undersized':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'flattwohundred':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "300m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.0083, 0.9860]
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
                
                return render(request, 'track/trackcalc.html', {'Undersized':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'flatthreehundred':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "400m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.0072, 0.9869]
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
                
                return render(request, 'track/trackcalc.html', {'Undersized':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'flatfourhundred':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "500m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.0063, 0.9874]
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
                
                return render(request, 'track/trackcalc.html', {'Undersized':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'flatfivehundred':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "600y":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.006, 0.9877]
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
                
                return render(request, 'track/trackcalc.html', {'Undersized':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'flatsixhundredy':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "600m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.0057, 0.9879]
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
                
                return render(request, 'track/trackcalc.html', {'Undersized':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'flatsixhundred':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "800m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.0049, 0.9886]
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
                
                return render(request, 'track/trackcalc.html', {'Undersized':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'flateighthundred':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})  

        if request.GET['events'] == "1000m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.0042, 0.9892]
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
                
                return render(request, 'track/trackcalc.html', {'Undersized':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'flatonethousand':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "1500m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.0033, 0.9901]
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
                
                return render(request, 'track/trackcalc.html', {'Undersized':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'flatfifteenhundred':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "Mile":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.0031, 0.9902]
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
                
                return render(request, 'track/trackcalc.html', {'Undersized':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'flatmile':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "3000m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.0019, 0.9915]
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
                
                return render(request, 'track/trackcalc.html', {'Undersized':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'flatthreethousand':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "5000m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.0011, 0.9924]
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
                
                return render(request, 'track/trackcalc.html', {'Undersized':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'flatfivethousand':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "4x200m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.0111, 0.9847]
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
                
                return render(request, 'track/trackcalc.html', {'Undersized':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'flatfourbytwo':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "4x400m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.0072, 0.9869]
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
                
                return render(request, 'track/trackcalc.html', {'Undersized':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'flatfourbyfour':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "4x800m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.0049, 0.9886]
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
                
                return render(request, 'track/trackcalc.html', {'Undersized':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'flatfourbyeight':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "DMR":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.0041, 0.9894]
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
                
                return render(request, 'track/trackcalc.html', {'Undersized':finalTimes[0], 'BOS':finalTimes[1],
                 'original':m, 'FlatDMR':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

    if request.GET['tracktype'] == "BOS":
        if request.GET['events'] == "200m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.0155, 1.0257]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'Undersized':finalTimes[1],
                 'original':m, 'bostwohundred':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "300m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.0142, 1.0226]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'Undersized':finalTimes[1],
                 'original':m, 'bosthreehundred':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "400m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.0133, 1.0205]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'Undersized':finalTimes[1],
                 'original':m, 'bosfourhundred':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "500m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.0127, 1.0192]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'Undersized':finalTimes[1],
                 'original':m, 'bosfivehundred':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "600y":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.0125, 1.0185]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'Undersized':finalTimes[1],
                 'original':m, 'bossixhundredy':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "600m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.0122, 1.0180]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'Undersized':finalTimes[1],
                 'original':m, 'bossixhundred':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "800m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.0115, 1.0165]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'Undersized':finalTimes[1],
                 'original':m, 'boseighthundred':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})  

        if request.GET['events'] == "1000m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.0109, 1.0152]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'Undersized':finalTimes[1],
                 'original':m, 'bosonethousand':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "1500m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.01, 1.0133]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'Undersized':finalTimes[1],
                 'original':m, 'bosfifteenhundred':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "Mile":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.0099, 1.0131]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'Undersized':finalTimes[1],
                 'original':m, 'bosmile':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "3000m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.0086, 1.0105]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'Undersized':finalTimes[1],
                 'original':m, 'bosthreethousand':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "5000m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.0077, 1.0088]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'Undersized':finalTimes[1],
                 'original':m, 'bosfivethousand':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "4x200m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.0155, 1.0257]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'Undersized':finalTimes[1],
                 'original':m, 'bosfourbytwo':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "4x400m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.0133, 1.0205]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'Undersized':finalTimes[1],
                 'original':m, 'bosfourbyfour':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "4x800m":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.0115, 1.0165]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'Undersized':finalTimes[1],
                 'original':m, 'bosfourbyeight':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})

        if request.GET['events'] == "DMR":
            try:
                m = request.GET['time']
                n = request.GET['time']
                i = 0
                j = 0
                finalTimes = []
                newTimes = []
                ratios = [1.0107, 1.0149]
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
                
                return render(request, 'track/trackcalc.html', {'Flat':finalTimes[0], 'Undersized':finalTimes[1],
                 'original':m, 'bosDMR':m})
            
            except ValueError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
            except IndexError:
                return render(request, 'track/trackcalc.html', {'error':'Invalid time'})
