import numpy as np

import pywt

def wavelet_denoise_1d(signal, wavelet: str='db4', level: int=1, threshold_type: str='soft'):
    coeffs = pywt.wavedec(signal, wavelet, level=level)

    for i in range(1, len(coeffs)):
        threshold = np.std(coeffs[i]) * np.sqrt(2 * np.log2(signal.size))

        if threshold_type == 'soft':
            coeffs[i] = pywt.threshold(coeffs[i], threshold, mode='soft')
        elif threshold_type == 'hard':
            coeffs[i] = pywt.threshold(coeffs[i], threshold, mode='hard')

    denoised = pywt.waverec(coeffs, wavelet)

    return denoised

def kernal_denoise_1d(signal, kernel: str | list | np.ndarray = 'gauss', size = 11, sigma = 10):
    if type(signal) == type([]): # list
        signal = np.array(signal)

    data = signal.copy()
    if type(kernel) == type(''): # string
        kernel = kernel.lower()
        pad_width = size // 2
        data = np.pad(data, pad_width, mode='edge')
        if kernel == 'gauss':
            kernel = np.fromfunction(lambda x: (1 / np.sqrt(2 * np.pi * sigma)) * np.exp(-((x - size // 2)**2) / (sigma**2)), (size,))
        elif kernel == 'mean':
            kernel = np.ones((size, ))
        else:
            print("Unimplemented kernel.")
            return np.array([])
    print(kernel)

    denoised = np.array([np.sum(kernel * data[i: i + size]) for i in range(len(signal))])
    return denoised