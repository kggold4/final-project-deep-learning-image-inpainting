import numpy as np
from PIL import Image as mg
from matplotlib import pyplot as plt
IMAGE = 'yosemite.jpg'
IMAGE_2 = 'GrandCanyon.jpg'


def generate():

    img = plt.imread(IMAGE)

    # first and second dimension are the matrix, third dimension is the channel
    img = np.asarray(img)
    data = []
    for _y in range(1000, 1400, 3):

        for _x in range(2100, 2400, 3):

            mat = np.zeros((3, 3, 3), dtype=np.uint8)
            for i in range(3):
                for j in range(3):
                    mat[i][j] = np.asarray(img[_y + i][_x + j])
            data.append(mat)
    img = plt.imread(IMAGE_2)

    img = np.asarray(img)
    data_2 = []
    for _y in range(100 ,500, 3):
        for _x in range(100, 500, 3):
            mat = np.zeros((3, 3, 3), dtype=np.uint8)
            for i in range(3):
                for j in range(3):
                    mat[i][j] = np.asarray(img[_y + i][_x + j])
            data_2.append(mat)

    return data,data_2
def generate_5():
    img = plt.imread(IMAGE)

    # first and second dimension are the matrix, third dimension is the channel
    img = np.asarray(img)

    data = []
    for _y in range(1000, 1200, 5):

        for _x in range(2100, 2300, 5):

            mat = np.zeros((5,5,3), dtype=np.uint8)
            for i in range(5):
                for j in range(5):
                    mat[i][j] = np.asarray(img[_y + i][_x + j])
            data.append(mat)
    img = plt.imread(IMAGE_2)

    img = np.asarray(img)
    data_2 = []
    for _y in range(100 ,330, 5):
        for _x in range(100, 330, 5):
            mat = np.zeros((5, 5, 3), dtype=np.uint8)
            for i in range(5):
                for j in range(5):
                    mat[i][j] = np.asarray(img[_y + i][_x + j])
            data_2.append(mat)

    return data,data_2
        
if __name__ == "__main__":

    generate_5()