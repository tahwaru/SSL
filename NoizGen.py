import numpy as np
import matplotlib.pyplot as plt



def Signal_plus_noizen(n_samples, mean):
        P_n = 1;   # target noise power
        SNR = 15;  # target SNR in dB
        P_s = P_n / 10^(-SNR/10); # calculated signal power
        a = 0.6
        s = randn(1,n_samples)*sqrt(P_s) + mean; # normal distribution with standard deviation = sqrt(P_s) and mean=mean
        v = randn(1,n_samples)*sqrt(P_n) + mean;
        y = a*s + v;


def NoiseGen(n_samples, mean, variance):
    return (np.sqrt(variance)*np.random.randn(1,n_samples) + mean)

#def NoiseGen(n_samples, mean, variance):
    return (np.sqrt(variance)*np.random.random(n_samples) + mean)

#noise = NoiseGen(100, 0, 5)
#print("\n noise values \n", noise[:4])
#plt.figure(1)
#t = np.arange(noise.shape[0])
#plt.plot(t, np.fft.fft(noise))

#noise2 = NoiseGen(100, 1, 5)
#print("\n noise values \n", noise2[:4])

#plt.figure(2)
#plt.plot(t, np.fft.fft(noise2))


#plt.show()
