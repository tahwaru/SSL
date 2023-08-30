#import os

#file = "vlc_record1.wav"
#os.system("mpg123 " + file)
import wave
import matplotlib.pyplot as plt
import numpy as np
from NoizGen import NoiseGen

obj = wave.open('vlc_record2.wav')

print('audio Parameters: ', obj.getparams())

sample_freq = obj.getframerate() # number of samples per second
n_samples = obj.getnframes() # number of samples or frames
signal_wave = obj.readframes(-1) # wave amplitude, i.e. sound intensity
duration = n_samples/sample_freq # audio length

print ("sample freq :\n ", sample_freq)
print ("n_samples :\n ", n_samples)
print ("signal wave length:\n ",len(signal_wave))
print ("duration :\n ", duration)

signal_array = np.frombuffer(signal_wave, dtype=np.int16)
print("signal array shape \n", signal_array.shape) # n_samples * n_channels
l_channel = signal_array[0::2] # every other samples starting from 0
r_channel = signal_array[1::2]# every other samples starting from 1
time = np.linspace(0, duration, num=n_samples)
print("type of the signal_wave variable \n", type(signal_wave))
print("time \n", time.shape)

n_channels = 2 # if the audio is recorded in stereo, there are 2 independent audio channels
# Making the signal noisy
signal_array_noisy = np.frombuffer(signal_wave, dtype=np.int16)
print("\n shape signal \n", signal_array_noisy.shape)
mean = 1000
variance = 1
noiz = NoiseGen(len(signal_array_noisy), mean, variance)[0]
print("\n shape signal \n", noiz.shape)

signal_array_noisy =  signal_array_noisy + 0.01*np.multiply(noiz,signal_array_noisy) # 0 mean and unit variance 
#print("signal array shape \n", signal_array.shape) # n_samples * n_channels
l_channel_noisy = signal_array_noisy[0::2] # every other samples starting from value at  index 0
r_channel_noisy = signal_array_noisy[1::2]# every other samples starting from value at index 1


plt.figure(1,figsize=(15,5))
#plt.plot(time, signal_array[:time.shape[0]])
plt.plot(time, l_channel)
plt.title("Audio Plot - left channel")
plt.ylabel("signal wave")
plt.xlabel("time(s)")
plt.xlim(0, duration) # limiting the x axis to the audio time
plt.figure(2,figsize=(15,5))
#plt.plot(time, signal_array[:time.shape[0]])
plt.plot(time, r_channel)
plt.title("Audio Plot - right channel")
plt.ylabel("signal wave")
plt.xlabel("time(s)")
plt.xlim(0, duration) # limiting the x axis to the audio time

#spectrogram
plt.figure(3, figsize=(15, 5))
plt.specgram(l_channel, Fs=sample_freq, vmin=-20, vmax=50)
plt.title('left - channel')
plt.ylabel('frequency (Hz)')
plt.xlabel('Time (s)')
plt.xlim(0, duration)
plt.colorbar()

plt.figure(4, figsize=(15, 5))
plt.specgram(r_channel, Fs=sample_freq, vmin=-20, vmax=50)
plt.title('right - channel')
plt.ylabel('frequency (Hz)')
plt.xlabel('Time (s)')
plt.xlim(0, duration)
plt.colorbar()

# after adding noise to the received signals
plt.figure(5,figsize=(15,5))
#plt.plot(time, signal_array[:time.shape[0]])
plt.plot(time, l_channel_noisy)
plt.title("Audio Plot - left channel noisy")
plt.ylabel("signal wave")
plt.xlabel("time(s)")
plt.xlim(0, duration) # limiting the x axis to the audio time
plt.figure(6,figsize=(15,5))
#plt.plot(time, signal_array[:time.shape[0]])
plt.plot(time, r_channel_noisy)
plt.title("Audio Plot - right channel noisy")
plt.ylabel("signal wave")
plt.xlabel("time(s)")
plt.xlim(0, duration) # limiting the x axis to the audio time

#spectrogram
plt.figure(7, figsize=(15, 5))
plt.specgram(l_channel_noisy, Fs=sample_freq, vmin=-20, vmax=50)
plt.title('left - channel noisy')
plt.ylabel('frequency (Hz)')
plt.xlabel('Time (s)')
plt.xlim(0, duration)
plt.colorbar()

plt.figure(8, figsize=(15, 5))
plt.specgram(r_channel_noisy, Fs=sample_freq, vmin=-20, vmax=50)
plt.title('right - channel noisy')
plt.ylabel('frequency (Hz)')
plt.xlabel('Time (s)')
plt.xlim(0, duration)
plt.colorbar()


plt.show()
