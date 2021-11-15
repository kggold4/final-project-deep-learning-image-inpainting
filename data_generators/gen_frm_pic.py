import numpy as np
from PIL import Image as mg
from matplotlib import pyplot as plt
if __name__ == '__main__':

    img = plt.imread('elon.jpg')
    img = np.asarray(img)  # first and second dimension are the matrix, third dimension is the channel
    data = []
    for _y in range(0, len(img) - 3, 3):
        for _x in range(0, len(img[_y]) - 3, 3):

            mat = np.zeros((3, 3, 3), dtype=np.uint8)
            for i in range(3):
                for j in range(3):
                    mat[i][j] = np.asarray(img[_y + i][_x + j])
            data.append(mat)

    print(len(data))