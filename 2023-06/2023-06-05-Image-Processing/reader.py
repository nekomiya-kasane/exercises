# import our basic, light-weight png reader library
import imageIO.png
import numpy as np

# this function reads an RGB color png file and returns width, height, as well as pixel arrays for r,g,b


class ImageReader:
    file_path: str = ""
    width: int = -1
    height: int = -1
    r = np.array([[]])
    g = np.array([[]])
    b = np.array([[]])

    def __init__(self, path: str):
        try:
            self.file_path = path
            image_reader = imageIO.png.Reader(filename=path)
            # png reader gives us width and height, as well as RGB data in image_rows (a list of rows of RGB triplets)
            (self.width, self.height, rgb_image_rows,
             rgb_image_info) = image_reader.read()

            print("read image width={}, height={}".format(
                self.width, self.height))

            self.r = np.zeros((self.height, self.width))
            self.g = np.zeros((self.height, self.width))
            self.b = np.zeros((self.height, self.width))

            for i, row in enumerate(rgb_image_rows):
                r, g, b = 0, 0, 0
                j = 0
                for elem in range(len(row)):
                    # RGB triplets are stored consecutively in image_rows
                    if elem % 3 == 0:
                        r = row[elem]
                    elif elem % 3 == 1:
                        g = row[elem]
                    else:
                        b = row[elem]
                        self.r[i, j] = r
                        self.g[i, j] = g
                        self.b[i, j] = b
                        j += 1

            self.ready = True
        except Exception as e:
            print("Error! " + str(e))
            self.ready = False

    def is_ready(self):
        return self.ready
