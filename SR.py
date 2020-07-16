import numpy as np #for array computation
from scipy.io import wavfile #to access .wav files
import matplotlib.pyplot as plt

frequency_samples,audio_signal=wavfile.read("C:/Users/Kiet k Maree/Downloads/audio/seriously.wav")

print("signal types",audio_signal.dtype)
print("frequencies",frequency_samples)
print("frequencies",frequency_samples)
print("signal duration",round(audio_signal.shape[0]/(frequency_samples),2),'seconds')

audio_signal=audio_signal/np.power(2,2)
audio_signal=audio_signal[:100]  #0-100
time_axis=1000*np.arange(0,len(audio_signal),1)/float(frequency_samples)
plt.plot(time_axis,audio_signal,color='blue')
plt.xlabel('time-millisec')
plt.ylabel('frequencies')
plt.title('audio file frequencies')
plt.show()
