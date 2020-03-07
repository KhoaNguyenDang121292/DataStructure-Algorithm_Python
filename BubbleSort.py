class BasicSort(object):
    # global variables
    # Initialize
    def __init__(self, array):
        self.array = array

    def BubbleSort(self):
        for i in range(0, len(self.array) - 1):
            for j in range(i + 1, len(self.array)):
                if self.array[i] > self.array[j]:
                    self.array[i], self.array[j] = self.array[j], self.array[i]
        return self.array


if __name__ == "__main__":
    a = [3, 38, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
    basic = BasicSort(a)
    sorted_a = basic.BubbleSort()
    print(sorted_a)
