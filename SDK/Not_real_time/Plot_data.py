import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt
import numpy as np
import pywt

# Load Excel file
df = pd.read_excel('brainf.xlsx')  # Assumes first row is header

# Extract data from the second column (index 1)
data = df.iloc[:, 1].values

# Define bandpass filter parameters
fs = 500  # Sampling frequency in Hz
lowcut = 8
highcut = 12
order = 4

# Design Butterworth bandpass filter
nyq = 0.5 * fs
low = lowcut / nyq
high = highcut / nyq
b, a = butter(order, [low, high], btype='band')

# Apply filter
filtered_data = filtfilt(b, a, data)

# Plot original and filtered data
plt.figure(figsize=(12, 4))
plt.plot(data, label='Original Data', alpha=0.4)
plt.plot(filtered_data, label='Filtered (8–12 Hz)', linewidth=1.5)
plt.xlabel('Sample Index')
plt.ylabel('Amplitude')
plt.title('Bandpass Filtered Data (8–12 Hz)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Continuous Wavelet Transform (CWT)
scales = np.arange(1, 128)  # Adjust as needed
waveletname = 'morl'
coefficients, freqs = pywt.cwt(filtered_data, scales, waveletname, sampling_period=1/fs)
power = (abs(coefficients)) ** 2
time = np.arange(len(filtered_data)) / fs

# Plot time-frequency power
plt.figure(figsize=(12, 6))
plt.contourf(time, freqs, power, 100, cmap='inferno')
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')
plt.title('Wavelet Transform Power Spectrum')
plt.ylim(1, 60)  # Limit frequency range for clarity
plt.colorbar(label='Power')
plt.tight_layout()
plt.show()
