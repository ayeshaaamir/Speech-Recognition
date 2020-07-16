frequency_samples,audio_signal=wavfile.read("C:/Users/Kiet k Maree/Desktop/audio/seriously.wav")
audio_signal=audio_signal[0:int(3.5*frequency_samples)]
#keep the first 3.5 seconds
audio_signal
