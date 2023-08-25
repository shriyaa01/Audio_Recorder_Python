# Importing required libraries
import sounddevice
from scipy.io.wavfile import write

# Setting the sample rate for the audio
fs = 44100  # Sample rate (samples per second)

# Getting user input for recording duration
second = int(input("Enter the time duration in seconds: "))

# user to enter the desired recording duration
print("Recording....\n")

# Recording audio using sounddevice library
record_voice = sounddevice.rec(int(second * fs), samplerate=fs, channels=2)  # Recording stereo audio
sounddevice.wait()  # Wait for recording to complete

# Saving the recorded audio to a WAV file
write("out.wav", fs, record_voice)

# Indicating that the recording process is finished
print("Finished...\nPlease Check it...")
