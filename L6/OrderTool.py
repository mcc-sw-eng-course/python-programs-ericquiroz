import copy
import datetime


class OrderTool:
    def __init__(self):
        self.list = []
        self.initial_list = []

        self.heapList = [0]
        self.currentSize = 0

        self.number_of_records = 0
        self.time_consumed = 0
        self.start_time = 0
        self.end_time = 0

    @staticmethod
    def is_value_num(value):
        try:
            float(value)
        except ValueError:
            return False
        return True

    def list_val(self):
        string = ','.join(map(str, self.list))
        return string

    def set_input_data(self, path):
        file = open(path, 'r')
        try:
            text_list = file.readline()

            if len(text_list) == 0:
                raise EOFError("File is empty")

            tmp_list = text_list.split(',')
            for item in tmp_list:
                # check if item is a number
                if self.is_value_num(item):
                    if float(item) % 1 == 0:
                        try:
                            self.list.append(int(item))
                        except ValueError:
                            self.list.append(float(item))
                    else:
                        self.list.append(float(item))
                else:
                    raise TypeError("CSV is not well formatted or values are not numbers")

        finally:
            file.close()

    def set_output_data(self, path):
        file = open(path, 'w+')
        try:
            if len(self.list_val()) == 0:
                raise EOFError("List is empty")

            file.write(self.list_val())

        finally:
            file.close()

    def reset_statics(self):
        self.number_of_records = 0
        self.time_consumed = 0
        self.start_time = 0
        self.end_time = 0

    def execute_merge_sort(self):
        self.reset_statics()

        if len(self.initial_list) == 0 and len(self.list) > 0:
            self.initial_list = copy.deepcopy(self.list)
        elif len(self.initial_list) == 0 and len(self.list) == 0:
            raise EOFError("input data not set yet")

        self.start_time = datetime.datetime.now()
        self.merge_sort(self.list)
        self.end_time = datetime.datetime.now()
        self.time_consumed = (self.end_time - self.start_time).seconds

    def merge_sort(self, alist):
        if len(alist) > 1:
            mid = len(alist) // 2
            left_half = alist[:mid]
            right_half = alist[mid:]

            left_half = self.merge_sort(left_half)
            right_half = self.merge_sort(right_half)

            i = 0
            j = 0
            k = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    alist[k] = left_half[i]
                    i += 1
                    self.number_of_records += 1
                else:
                    alist[k] = right_half[j]
                    j += 1
                    self.number_of_records += 1
                k += 1

            while i < len(left_half):
                alist[k] = left_half[i]
                i += 1
                k += 1
                self.number_of_records += 1

            while j < len(right_half):
                alist[k] = right_half[j]
                j += 1
                k += 1
                self.number_of_records += 1

        return alist

    def execute_quick_sort(self):
        self.reset_statics()

        if len(self.initial_list) == 0 and len(self.list) > 0:
            self.initial_list = copy.deepcopy(self.list)
        elif len(self.initial_list) == 0 and len(self.list) == 0:
            raise EOFError("input data not set yet")

        self.start_time = datetime.datetime.now()
        self.quick_sort_helper(self.list, 0, len(self.list) - 1)
        self.end_time = datetime.datetime.now()
        self.time_consumed = (self.end_time - self.start_time).seconds

    def quick_sort_helper(self, alist, first, last):
        if first < last:
            splitpoint = self.partition(alist, first, last)

            self.quick_sort_helper(alist, first, splitpoint - 1)
            self.quick_sort_helper(alist, splitpoint + 1, last)

    def partition(self, alist, first, last):
        pivotvalue = alist[first]

        leftmark = first + 1
        rightmark = last

        done = False
        while not done:

            while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
                leftmark = leftmark + 1

            while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
                rightmark = rightmark - 1

            if rightmark < leftmark:
                done = True
            else:
                temp = alist[leftmark]
                alist[leftmark] = alist[rightmark]
                alist[rightmark] = temp
                self.number_of_records += 2

        temp = alist[first]
        alist[first] = alist[rightmark]
        alist[rightmark] = temp
        self.number_of_records += 2

        return rightmark

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
                self.number_of_records += 2
            i = mc

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def buildHeap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1

    def execute_heap_sort(self):
        self.reset_statics()

        if len(self.initial_list) == 0 and len(self.list) > 0:
            self.initial_list = copy.deepcopy(self.list)
        elif len(self.initial_list) == 0 and len(self.list) == 0:
            raise EOFError("input data not set yet")

        self.start_time = datetime.datetime.now()
        self.buildHeap(self.list)
        self.list = []
        while self.currentSize > 0:
            self.list.append(self.delMin())
        self.end_time = datetime.datetime.now()
        self.time_consumed = (self.end_time - self.start_time).seconds

    def get_performance_data(self):
        if self.start_time == 0:
            raise EOFError("sort has not been executed")

        statics_list = []
        statics_list.append(self.number_of_records)
        statics_list.append(self.time_consumed)
        statics_list.append(self.start_time)
        statics_list.append(self.end_time)

        return statics_list


if __name__ == '__main__':
    o = OrderTool()

    o.set_input_data("test.txt")

    print(o.list)
    print(o.list_val())

    o.execute_heap_sort()
    print(o.list_val())

    print(o.get_performance_data())
