import numpy as np
from scipy.fft import fft
import matplotlib.pyplot as plt

# Sample EEG data (replace this with your actual data)
eeg_data = np.random.rand(1024)

# Function to calculate frequency bands
def calculate_frequency_bands(eeg_data, sampling_rate):
    n = len(eeg_data)
    frequencies = np.fft.fftfreq(n, d=1/sampling_rate)
    fft_values = fft(eeg_data)
    fft_values = np.abs(fft_values)

    # Define frequency bands (adjust these based on your specific needs)
    theta_band = (4, 8)  # Theta frequency band
    alpha_band = (8, 13)  # Alpha frequency band
    beta_band = (13, 30)  # Beta frequency band
    gamma_band = (30, 40)  # Gamma frequency band

    # Calculate the power in each frequency band
    theta_power = np.sum(fft_values[(frequencies >= theta_band[0]) & (frequencies <= theta_band[1])])
    alpha_power = np.sum(fft_values[(frequencies >= alpha_band[0]) & (frequencies <= alpha_band[1])])
    beta_power = np.sum(fft_values[(frequencies >= beta_band[0]) & (frequencies <= beta_band[1])])
    gamma_power = np.sum(fft_values[(frequencies >= gamma_band[0]) & (frequencies <= gamma_band[1])])

    return theta_power, alpha_power, beta_power, gamma_power

# Example usage
sampling_rate = 250  # Replace with your actual sampling rate
theta_power, alpha_power, beta_power, gamma_power = calculate_frequency_bands(eeg_data, sampling_rate)

print(f'Theta Power: {theta_power}')
print(f'Alpha Power: {alpha_power}')
print(f'Beta Power: {beta_power}')
print(f'Gamma Power: {gamma_power}')

# Plot EEG data and its FFT
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(eeg_data)
plt.title('EEG Data')

plt.subplot(2, 1, 2)
plt.plot(frequencies, fft_values)
plt.title('FFT of EEG Data')
plt.xlabel('Frequency (Hz)')
plt.show()
