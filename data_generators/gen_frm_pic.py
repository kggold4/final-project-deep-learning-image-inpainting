import numpy as np
from PIL import Image as mg
from matplotlib import pyplot as plt
IMAGE = 'yosemite.jpg'


class gen_frm_pic:
    def generate():

        img = plt.imread(IMAGE)

        # first and second dimension are the matrix, third dimension is the channel
        img = np.asarray(img)
        data = []
        for _y in range(1000, 1093, 3):

            for _x in range(400, 500, 3):

                mat = np.zeros((3, 3, 3), dtype=np.uint8)
                for i in range(3):
                    for j in range(3):
                        mat[i][j] = np.asarray(img[_y + i][_x + j])
                data.append(mat)
        print(data)
        return data
