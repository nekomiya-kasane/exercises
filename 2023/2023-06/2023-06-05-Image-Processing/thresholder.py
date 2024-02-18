import numpy as np

def find_peaks(arr):
    peaks = []
    valleys = []
    prev_slope = np.sign(arr[1] - arr[0])

    for i in range(1, len(arr) - 1):
        slope = np.sign(arr[i + 1] - arr[i])

        if prev_slope > 0 and slope < 0:
            peaks.append(i)
        elif prev_slope < 0 and slope > 0:
            valleys.append(i)

        prev_slope = slope

    return peaks, valleys

def eval_otsu_threshold(arr):
    total = np.sum(arr)

    best_threshold = 0
    max_var = 0

    for t in range(len(arr)):
        back_pixels = np.sum(arr[:t])
        fore_pixels = np.sum(arr[t:])

        back_weight = back_pixels / total
        fore_weight = fore_pixels / total

        if back_pixels == 0 or fore_pixels == 0:
            continue

        back_mean = np.sum(np.arange(t) * arr[:t]) / back_pixels
        fore_mean = np.sum(np.arange(t, 256) * arr[t:]) / fore_pixels

        var = back_weight * fore_weight * (back_mean - fore_mean)**2

        if var > max_var:
            best_threshold = t
            max_var = var

    return best_threshold

def eval_hist_threshold(arr, method: str = 'mean'):
    if type(arr) == type([]):
        arr = np.array(arr)

    if method == 'mean':
        total = np.sum(arr)
        return np.dot(np.array([i for i in range(len(arr))]), arr) / total

    if method == 'double_peaks_max':
        _, valleys = find_peaks(arr)
        threshold = np.max(valleys)
        return threshold

    if method == 'double_peaks_min':
        _, valleys = find_peaks(arr)
        threshold = np.min(valleys)
        return threshold
    
    if method == 'otsu':
        return eval_otsu_threshold(arr)
