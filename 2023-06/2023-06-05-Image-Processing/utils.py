import numpy as np
from matplotlib import pyplot as plt
import decomposer

def show_all_pipes(imgs, titles=[], real_scale=False):
    n = len(imgs)
    plt.figure(figsize=(5 * n, 5))

    if not len(titles):
        titles = [f'Image {i + 1}' for i in range(n)]

    for i, img in enumerate(imgs):
        plt.subplot(1, n, i + 1)
        if real_scale:
            plt.imshow(img, cmap='gray', vmin=0, vmax=255)
        else:
            plt.imshow(img, cmap='gray')
        plt.title(titles[i])

    plt.tight_layout()
    plt.show()

def grayout(r, g, b):
    return (r + g + b) / 3

def normalize(arr):
    mi, mx = np.min(arr), np.max(arr)
    normalizer = lambda x: round((x - mi) / (mx - mi) * 255) if mi != mx else 128
    return np.vectorize(normalizer)(arr)

def apply_standard_deviation_filter(arr, size: int = 5):
    filtered_image = np.zeros_like(arr, dtype=np.float64)
    padded_image = np.pad(arr, ((size // 2, size // 2), (2, 2)), mode='edge')

    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            region = padded_image[i:i + size, j:j + size]
            filtered_image[i, j] = np.std(region)

    return filtered_image

def apply_gaussian_filter(image, size: int = 3, sigma: float = 1.5, print_kernel: bool = False):
    kernel = np.fromfunction(lambda x, y: (1 / (2 * np.pi * sigma**2)) * np.exp(-((x - size // 2)**2 + (y - size // 2)**2) / (2 * sigma**2)), (size, size))
    kernel = kernel / np.sum(kernel)

    if print_kernel:
        print("Kernel:\n", kernel)

    pad_width = size // 2
    padded_image = np.pad(image, pad_width, mode='edge')

    filtered_image = np.zeros_like(image, dtype=np.float64)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            region = padded_image[i:i+size, j:j+size]
            filtered_image[i, j] = np.sum(region * kernel)

    return filtered_image

def binarize(img, threahold: int = 25):
    thresholded = np.where(img < threahold, 0, img)
    thresholded = np.where(img >= threahold, 1, thresholded)
    return thresholded

def erosion_or_dilation(image, size, erosion=True):
    height, width = image.shape

    result = np.zeros_like(image)

    for y in range(size, height - size):
        for x in range(size, width - size):
            region = image[y - size:y + size + 1, x - size: x + size + 1]
            new_value = np.min(region) if erosion else np.max(region)
            result[y, x] = new_value

    return result

def is_barcode(labels, label, original):
    info = decomposer.get_components_info(labels, label, original)
    if abs(info.cover - 1) > 0.3 or info.size < 400 or info.minor_radius < 30 or info.major_radius < 30:
        return False, info
    return True, info