# Built in packages
import math
import sys
from pathlib import Path

# Matplotlib will need to be installed if it isn't already. This is the only package allowed for this base part of the 
# assignment.
from matplotlib import pyplot as plt
from matplotlib import pyplot 
from matplotlib.patches import Rectangle, Polygon

import numpy as np

from reader import ImageReader 
import denoise
import thresholder
import decomposer
from utils import *
# a useful shortcut method to create a list of lists based array representation for an image, initialized with a value
def createInitializedGreyscalePixelArray(image_width, image_height, initValue = 0):

    new_array = [[initValue for x in range(image_width)] for y in range(image_height)]
    return new_array


# You can add your own functions here:

# This is our code skeleton that performs the barcode detection.
# Feel free to try it on your own images of barcodes, but keep in mind that with our algorithm developed in this assignment,
# we won't detect arbitrary or difficult to detect barcodes!
def main():

    command_line_arguments = sys.argv[1:]

    SHOW_DEBUG_FIGURES = True

    # this is the default input image filename
    filename = "Barcode6"
    input_filename = "images/"+filename+".png"

    if command_line_arguments != []:
        input_filename = command_line_arguments[0]
        SHOW_DEBUG_FIGURES = False

    output_path = Path("output_images")
    if not output_path.exists():
        # create output directory
        output_path.mkdir(parents=True, exist_ok=True)

    output_filename = output_path / Path(filename+"_output.png")
    if len(command_line_arguments) == 2:
        output_filename = Path(command_line_arguments[1])

    # we read in the png file, and receive three pixel arrays for red, green and blue components, respectively
    # each pixel array contains 8 bit integer values between 0 and 255 encoding the color values
    # STUDENT IMPLEMENTATION here


    img = ImageReader(input_filename)

    img_rgb = np.dstack((img.r, img.g, img.b))

    im = grayout(img.r, img.g, img.b)
    im_norm = normalize(im)
    sd = apply_standard_deviation_filter(im_norm)

    n = 4
    sigma = 15
    size = 9

    gausses = [sd.copy()] + [None] * n
    titles = ["Input"] + [f"After applying {i + 1} time{'s' if i else ''}" for i in range(n)]
    for i in range(n):
        gausses[i+1] = apply_gaussian_filter(gausses[i], sigma=sigma, size=size)

    if SHOW_DEBUG_FIGURES:
        show_all_pipes(gausses, titles)

    gauss: np.ndarray = gausses[-1] # type: ignore
    hist = np.log(np.histogram(gauss, bins=256, range=(0, 256))[0])
    hist[np.isinf(hist)] = 0
    hist_smoothed_gauss = denoise.kernal_denoise_1d(hist, 'gauss', size=11, sigma=15)
    hist_smoothed_wavelet = denoise.wavelet_denoise_1d(hist, level=3)

    threshold = thresholder.eval_hist_threshold(hist_smoothed_gauss, 'otsu') - 2
    thresholded = binarize(gauss, threshold) * 255

    n = 4
    eroses = [thresholded.copy()] + [None] * n
    titles = ["Input"] + [f"After erosing {i + 1} time{'s' if i else ''}" for i in range(n)]
    for i in range(n):
        eroses[i+1] = erosion_or_dilation(eroses[i], 2)
    if SHOW_DEBUG_FIGURES:
        show_all_pipes(eroses, titles)
    eros: np.ndarray = eroses[-1] # type: ignore

    dilateds = [eros.copy()] + [None] * n
    titles = ["Input"] + [f"After dilating {i + 1} time{'s' if i else ''}" for i in range(n)]
    for i in range(n):
        dilateds[i+1] = erosion_or_dilation(dilateds[i], 2, False)
    if SHOW_DEBUG_FIGURES:
        show_all_pipes(dilateds, titles)
    dilated: np.ndarray = dilateds[-1] # type: ignore

    labels, label_num = decomposer.get_connected_components(dilated)

    if SHOW_DEBUG_FIGURES:
        decomposer.plot_components(labels)

    fig, ax = plt.subplots()

    mx_size = 0
    mx_rect = decomposer.Rect(0, 0, 0, 0)
    for i in range(1, label_num + 1):
        rect = decomposer.get_outer_box(labels, i)

        isbarcode, info = is_barcode(labels, i, None)
        if info.size > mx_size and isbarcode:
            mx_size = info.size
            mx_rect = rect
            #print(i, info)

    rectangle = Rectangle((mx_rect.top, mx_rect.left),
                            mx_rect.height, mx_rect.width, edgecolor='g', facecolor='none')

    ax.add_patch(rectangle)

    ax.set_xlim(0, img.width)
    ax.set_ylim(img.height, 0)
    #decomposer.plot_components(labels)
    plt.imshow(img_rgb.astype(np.uint8))
    plt.savefig("asdf")

    pyplot.savefig(output_filename, dpi=600)

    if SHOW_DEBUG_FIGURES:
        # plot the current figure
        pyplot.show()


if __name__ == "__main__":
    main()