import numpy as np
import matplotlib.pyplot as plt

# Define the signal
t = np.arange(256)  # Time vector
f = np.sin(t)  # Signal: sine wave

# Compute the FFT
fft_result = np.fft.fft(f)
frequencies = np.fft.fftfreq(t.shape[-1])  # Frequency axis

# Compute the amplitude spectrum
amplitude = np.abs(fft_result) / len(f)  # Normalize to preserve units
print(f'{np.max(amplitude):.3f}')


amplitude[1:len(f)//2] *= 2  # Double the amplitudes for the single-sided spectrum

# Plot the amplitude spectrum
plt.figure(figsize=(8, 4))
plt.plot(frequencies[:len(f)//2], amplitude[:len(f)//2])  # Single-sided
plt.title("Amplitude Spectrum of f(t) = sin(t)")
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
plt.grid()
plt.show()
