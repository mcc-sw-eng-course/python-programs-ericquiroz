import unittest
import os
import random
from OrderTool import OrderTool

class TestOrderTool(unittest.TestCase):
    def generate_random_number(self):
        if random.randint(1,3) == 2:
            return round(random.uniform(-999,999), random.randint(1,4))
        else:
            return random.randint(-9999,9999)

    def setUp(self):
        test_list = "45,43,23,7,83,11,0"
        filename = "correct.txt"

        f1 = open(filename, "w+")
        f1.write(test_list)
        f1.close()

        test_list = "45.4,43.1,23.43,7.23,83.43,11.432,0.1"
        filename = "correct_float.txt"

        f1 = open(filename, "w+")
        f1.write(test_list)
        f1.close()

        test_list = "-0.1,45,23.63,-43,-89.82,22,41.001,0"
        filename = "correct_negative.txt"

        f1 = open(filename, "w+")
        f1.write(test_list)
        f1.close()

        list = []
        for i in range(0, 10000):
            list.append(self.generate_random_number())

        test_list = ','.join(map(str, list))
        filename = "correct_10000.txt"

        f1 = open(filename, "w+")
        f1.write(test_list)
        f1.close()

        list = []
        for i in range(0, 100000):
            list.append(self.generate_random_number())

        test_list = ','.join(map(str, list))
        filename = "correct_100000.txt"

        f1 = open(filename, "w+")
        f1.write(test_list)
        f1.close()

        list = []
        for i in range(0, 1000000):
            list.append(self.generate_random_number())

        test_list = ','.join(map(str, list))
        filename = "correct_1M.txt"

        f1 = open(filename, "w+")
        f1.write(test_list)
        f1.close()

    def tearDown(self):
        os.remove("correct.txt")
        os.remove("correct_float.txt")
        os.remove("correct_negative.txt")
        os.remove("correct_10000.txt")
        os.remove("correct_100000.txt")
        os.remove("correct_1M.txt")

    def test_set_input_data(self):
        filename = "correct.txt"

        tool = OrderTool()
        tool.set_input_data(filename)

        self.assertEqual(tool.list_val(), "45,43,23,7,83,11,0")

    def test_set_input_data_float(self):
        filename = "correct_float.txt"

        tool = OrderTool()
        tool.set_input_data(filename)

        self.assertEqual(tool.list_val(), "45.4,43.1,23.43,7.23,83.43,11.432,0.1")

    def test_set_input_data_negative(self):
        filename = "correct_negative.txt"

        tool = OrderTool()
        tool.set_input_data(filename)

        self.assertEqual(tool.list_val(), "-0.1,45,23.63,-43,-89.82,22,41.001,0")

    def test_set_input_data_forbidden(self):
        tool = OrderTool()
        self.assertRaises(PermissionError, tool.set_input_data, "forbidden.txt")

    def test_set_input_data_file_not_found(self):
        tool = OrderTool()
        self.assertRaises(FileNotFoundError, tool.set_input_data, "notfound.txt")

    def test_set_input_data_incorrect_data_file(self):
        test_list = "45,43,23,7,83,11,0,hi"
        filename = "incorrect.txt"

        f1 = open(filename, "w+")
        f1.write(test_list)
        f1.close()

        tool = OrderTool()

        self.assertRaises(TypeError, tool.set_input_data, filename)

        os.remove(filename)

    def test_set_input_data_empty_data_file(self):
        test_list = ""
        filename = "empty.txt"

        f1 = open(filename, "w+")
        f1.write(test_list)
        f1.close()

        tool = OrderTool()

        self.assertRaises(EOFError, tool.set_input_data, filename)

        os.remove(filename)

    def test_set_output_data(self):
        filename = "correct.txt"

        tool = OrderTool()
        tool.set_input_data(filename)
        tool.set_output_data("correct2.txt")

        file = open("correct2.txt", "r")
        fileline = file.readline()
        file.close()

        os.remove("correct2.txt")

        self.assertEqual(fileline, "45,43,23,7,83,11,0")

    def test_set_output_data_forbidden(self):
        filename = "correct.txt"

        tool = OrderTool()
        tool.set_input_data(filename)

        self.assertRaises(PermissionError, tool.set_output_data, "forbidden/correct2.txt")

    def test_execute_merge_sort(self):
        filename = "correct.txt"

        tool = OrderTool()
        tool.set_input_data(filename)
        tool.execute_merge_sort()
        tool.set_output_data("correct2.txt")

        file = open("correct2.txt", "r")
        fileline = file.readline()
        file.close()

        os.remove("correct2.txt")

        self.assertEqual(fileline, "0,7,11,23,43,45,83")

    def test_execute_merge_sort_float(self):
        filename = "correct_float.txt"

        tool = OrderTool()
        tool.set_input_data(filename)
        tool.execute_merge_sort()
        tool.set_output_data("correct2.txt")

        file = open("correct2.txt", "r")
        fileline = file.readline()
        file.close()

        os.remove("correct2.txt")

        self.assertEqual(fileline, "0.1,7.23,11.432,23.43,43.1,45.4,83.43")

    def test_execute_merge_sort_negative(self):
        filename = "correct_negative.txt"

        tool = OrderTool()
        tool.set_input_data(filename)
        tool.execute_merge_sort()
        tool.set_output_data("correct2.txt")

        file = open("correct2.txt", "r")
        fileline = file.readline()
        file.close()

        os.remove("correct2.txt")

        self.assertEqual(fileline, "-89.82,-43,-0.1,0,22,23.63,41.001,45")

    def test_execute_merge_sort_10k(self):
        filename = "correct_10000.txt"

        tool = OrderTool()
        tool.set_input_data(filename)
        tool.execute_merge_sort()
        tool.set_output_data("correct2.txt")

        file = open("correct2.txt", "r")
        fileline = file.readline()
        file.close()

        os.remove("correct2.txt")

        list = fileline.split(',')
        prev = float("-inf")
        for item in list:
            if prev <= float(item):
                prev = float(item)
            else:
                self.assertTrue(False)

        self.assertTrue(True)

    def test_execute_merge_sort_100k(self):
        filename = "correct_100000.txt"

        tool = OrderTool()
        tool.set_input_data(filename)
        tool.execute_merge_sort()
        tool.set_output_data("correct2.txt")

        file = open("correct2.txt", "r")
        fileline = file.readline()
        file.close()

        os.remove("correct2.txt")

        list = fileline.split(',')
        prev = float("-inf")
        for item in list:
            if prev <= float(item):
                prev = float(item)
            else:
                self.assertTrue(False)

        self.assertTrue(True)

    def test_execute_merge_sort_1m(self):
        filename = "correct_1M.txt"

        tool = OrderTool()
        tool.set_input_data(filename)
        tool.execute_merge_sort()
        tool.set_output_data("correct2.txt")

        file = open("correct2.txt", "r")
        fileline = file.readline()
        file.close()

        os.remove("correct2.txt")

        list = fileline.split(',')
        prev = float("-inf")
        for item in list:
            if prev <= float(item):
                prev = float(item)
            else:
                self.assertTrue(False)

        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
