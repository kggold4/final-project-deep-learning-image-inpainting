import os, cv2

# util helping functions
IMAGES_PATH = 'c:/compress'
COMPRESSED_IMAGES_PATH = 'c:/compress/compressed'
DEFAULT_HEIGHT = 200
DEFAULT_WIDTH = 200


class util_functions:

    @staticmethod
    def swap(arr, i , j) -> None:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    @staticmethod
    def compress_images(from_path=IMAGES_PATH, to_path=COMPRESSED_IMAGES_PATH, height=DEFAULT_HEIGHT, width=DEFAULT_WIDTH) -> None:
        files_list = os.listdir(from_path)
        images_list = []
        for file_name in files_list:
            if '.jpg' in file_name or '.png' in file_name:
                images_list.append(file_name)

        data = []
        for i in range(len(images_list)):
            image_path = from_path + '/' + images_list[i]
            image = cv2.imread(image_path) # cv2.IMREAD_GRAYSCALE
            image = cv2.resize(image, (height, width))
            data.append(image)

        for i in range(len(data)):
            image = data[i]
            cv2.imwrite(to_path + '/' + images_list[i], image)
