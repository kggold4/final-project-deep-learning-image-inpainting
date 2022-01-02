import os
import numpy as np
from PIL import Image as mg
import matplotlib.pyplot as plt

IMAGE = 'images/yosemite.jpg'
IMAGE_2 = 'images/GrandCanyon.jpg'
WILD_IMAGES_DIR = 'images/auto_coder_data/train/wild'

EXAMPLE_WILD_IMAGE_1 = "../images/auto_coder_data/train/wild/flickr_wild_001930.jpg"
EXAMPLE_WILD_IMAGE_2 = "../images/auto_coder_data/train/wild/flickr_wild_002930.jpg"

def get_random_image(path=WILD_IMAGES_DIR):
    files_list = os.listdir(path)
    images_list = []
    for file_name in files_list:
        if '.jpg' in file_name or '.png' in file_name:
            images_list.append(file_name)
            
    return images_list[np.random.randint(0, len(images_list))]
    

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
    for _y in range(100, 500, 3):
        for _x in range(100, 500, 3):
            mat = np.zeros((3, 3, 3), dtype=np.uint8)
            for i in range(3):
                for j in range(3):
                    mat[i][j] = np.asarray(img[_y + i][_x + j])
            data_2.append(mat)

    return data, data_2


def generate_5():
    img = plt.imread(IMAGE)

    # first and second dimension are the matrix, third dimension is the channel
    img = np.asarray(img)

    data = []
    for _y in range(800, 1000, 5):

        for _x in range(1800, 2000, 5):

            mat = np.zeros((5, 5, 3), dtype=np.uint8)
            for i in range(5):
                for j in range(5):
                    mat[i][j] = np.asarray(img[_y + i][_x + j])
            data.append(mat)
    img = plt.imread(IMAGE_2)

    img = np.asarray(img)
    data_2 = []
    for _y in range(100, 500, 5):
        for _x in range(100, 500, 5):
            mat = np.zeros((5, 5, 3), dtype=np.uint8)
            for i in range(5):
                for j in range(5):
                    mat[i][j] = np.asarray(img[_y + i][_x + j])
            data_2.append(mat)

    return data, data_2


def generate_wild_image(path1=EXAMPLE_WILD_IMAGE_1, path2=EXAMPLE_WILD_IMAGE_2):
    
    img = plt.imread(path1)
    img = np.asarray(img)

    data = []
    for _y in range(0, 100, 5):
        for _x in range(0, 100, 5):
            mat = np.zeros((5, 5, 3), dtype=np.uint8)
            for i in range(5):
                for j in range(5):
                    mat[i][j] = np.asarray(img[_y + i][_x + j])
            data.append(mat)
            
    img = plt.imread(path2)
    img = np.asarray(img)
    data_2 = []
    for _y in range(0, 100, 5):
        for _x in range(0, 100, 5):
            mat = np.zeros((5, 5, 3), dtype=np.uint8)
            for i in range(5):
                for j in range(5):
                    mat[i][j] = np.asarray(img[_y + i][_x + j])
            data_2.append(mat)

    return data, data_2


if __name__ == "__main__":
    data, data_2 = generate_wild_image()
    print(data)
    print('********************************************')
    print(data_2)

