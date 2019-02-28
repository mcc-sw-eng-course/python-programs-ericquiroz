import copy

class OrderTool:
    def __init__(self):
        self.list = []
        self.initial_list = []

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

    def execute_merge_sort(self):
        if len(self.initial_list) == 0 and len(self.list) > 0:
            self.initial_list = copy.deepcopy(self.list)
        elif len(self.initial_list) == 0 and len(self.list) == 0:
            raise EOFError("input data not set yet")

        self.merge_sort(self.list)

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
                else:
                    alist[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                alist[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                alist[k] = right_half[j]
                j += 1
                k += 1

        return alist


if __name__ == '__main__':
    o = OrderTool()

    o.set_input_data("test.txt")

    print(o.list)
    print(o.list_val())
