class BasicSort(object):
    # global variables
    # Initialize
    def __init__(self, array):
        self.array = array

    def InsertionSort(self):
        for i in range(1, len(self.array)):
            min = self.array[i]
            j = i - 1
            while j >= 0 and min < self.array[j]:
                self.array[j + 1] = self.array[j]
                j -= 1
            self.array[j + 1] = min
        return self.array


if __name__ == "__main__":
    a = [3, 38, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
    basic = BasicSort(a)
    sorted_a = basic.InsertionSort()
    print(sorted_a)
