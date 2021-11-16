# util helping functions


class util_functions:

    @staticmethod
    def swap(arr, i , j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
