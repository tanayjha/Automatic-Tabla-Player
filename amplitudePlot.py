# RUN CODE USING python3 amplitudePlot.py

# AMPLITUDE CALCULATION PART
# http://samcarcagno.altervista.org/blog/basic-sound-processing-python/

# TO CONVERT MP3 TO WAV FORMAT
# ffmpeg -i 111.mp3 -acodec pcm_s16le -ac 1 -ar 16000 out.wav

# METRONOME API TO PLAY THE BEATS PER MIN IN BACKGROUND 
# https://github.com/kiike/python-metronome
# USAGE ./metronome.py -b (beats/min) -n (4/8/16) -a(accent)


# ANDROID APP TO PLAY THE TABLA TAALS (yet to figure out a way to integrate it)
# https://play.google.com/store/apps/details?id=in.spyders.android.tabla&hl=en
# UPDATE - Use http://vishwamohini.com/music/demo-tabla.php for online tabla player

import matplotlib.pyplot as plt
from pylab import *
from scipy.io import wavfile
import operator, wave, wavio
import numpy as np

w = wave.open('Babaji Sharnam.wav')
print (w.getsampwidth())
sampFreq, snd = wavio.read('Babaji Sharnam.wav')

snd = snd/2**15

snd = np.atleast_2d(snd)
samplingPoints, channels = snd.shape

if (channels > 2):
	samplingPoints, channels = channels, samplingPoints
samplingRate = samplingPoints / sampFreq

if (channels == 2):
	s1 = snd[:, 0]  # These contain two-dimensional data - one track for the left and one track for the right speaker. Select one
else:
	s1 = snd[0]

timearray = arange(0, samplingPoints, 1)
timearray = timearray/sampFreq
timearray = timearray*1000

# plt.plot(timearray, s1, color = 'k')
ylabel('Amplitude')
xlabel('Time (ms)')
# plt.show()

# PRINT TO CHECK BASIC VALUES
# print (channels)
# print (samplingRate)
# print (samplingPoints)
# print (sampFreq)
# print (s1)


allDiff = {}

# CALCULATE DIFFERENCE OF AMPLITUDE BETWEEN EVERY SAMPLE POINT
for i in range (2, samplingPoints):
	allDiff[i] = s1[i] - s1[i-1]

# Find biggest amplitude difference
sorted_allDiff = sorted(allDiff.items(), key=operator.itemgetter(1), reverse = True) 

count = 0
for x in sorted_allDiff:
	print (x[0]/sampFreq)	# Print the time at which amplitude difference is maximum
	count = count + 1
	if(count == 10):	# Print the first 10 values
		break


