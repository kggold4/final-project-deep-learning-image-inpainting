import numpy as np
from PIL import Image
if __name__ == '__main__':
    upper_bound = 40
    lower_bound = 20
    data =[]
    w, h = 3, 3
    for l in range (333):#vibrate the coloer in the first channel
        mat = np.zeros((h,w,3),dtype=np.uint8)
        d = np.random.randint(lower_bound,upper_bound)
        k, m, n = np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255-d)
        for i in range(h):
            for j in range(w):
                mat[i][j][0] = np.random.randint(n, n + d)
                mat[i][j][1] = m
                mat[i][j][2] = k
        data.append(mat)
    for l in range (333): #vibrate the color in the second channel
        mat = np.zeros((h,w,3),dtype=np.uint8)
        d = np.random.randint(lower_bound, upper_bound)
        k, m, n = np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255-d)
        for i in range(h):
            for j in range(w):
                mat[i][j][0] = k
                mat[i][j][1] = np.random.randint(n, n + d)
                mat[i][j][2] = m
        data.append(mat)
    for l in range (334): #vibrate the color in the third channel
        mat = np.zeros((h,w,3),dtype=np.uint8)
        d = np.random.randint(lower_bound, upper_bound)
        k, m, n = np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255-d)
        for i in range(h):
            for j in range(w):
                mat[i][j][0] = k
                mat[i][j][1] = m
                mat[i][j][2] = np.random.randint(n, n + d)
        data.append(mat)
    img = Image.fromarray(data[100], 'RGB')
    img.save('my1.png')
    img = Image.fromarray(data[500], 'RGB')
    img.save('my2.png')
    img = Image.fromarray(data[900], 'RGB')
    img.save('my3.png')
