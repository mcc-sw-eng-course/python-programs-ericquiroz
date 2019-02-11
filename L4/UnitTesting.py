from exercise8 import mean
from exercise8 import stddev
from exercise8 import median
from exercise8 import nquartil
from exercise8 import npercentil
from exercise9 import convert_to_roman
from myPowerList import myPowerList
from UserList import UserList
from UserList import User
import unittest


class TestUM(unittest.TestCase):
    def test_convert_to_roman(self):
        self.assertEqual(convert_to_roman(2548), "MMDXLVIII")

    def test_convert_to_roman_negative_number(self):
        self.assertRaises(ValueError, convert_to_roman, -1)

    def test_convert_to_roman_greater_than_3999(self):
        self.assertRaises(ValueError, convert_to_roman, 5000)

    def test_convert_to_roman_float_number(self):
        self.assertRaises(TypeError, convert_to_roman, 4.5)

    def test_convert_to_roman_float_string(self):
        self.assertRaises(TypeError, convert_to_roman, "Five Hundred")

    def test_convert_to_roman_float_array(self):
        self.assertRaises(TypeError, convert_to_roman, [456])

    def test_convert_to_roman_float_none(self):
        self.assertRaises(TypeError, convert_to_roman, None)

    def test_mean_number_list(self):
        self.assertEqual(mean([1, 2, 3]), 2)

    def test_mean_float_list(self):
        self.assertAlmostEqual(mean([1.1, 2.2, 3.3]), 2.2)

    def test_mean_empty_list(self):
        self.assertRaises(ZeroDivisionError, mean, [])

    def test_mean_string(self):
        self.assertRaises(TypeError, mean, "a")

    def test_mean_string_list(self):
        self.assertRaises(TypeError, mean, ["a", "b"])

    def test_mean_list_with_numbers_and_strings(self):
        self.assertRaises(TypeError, mean, [1, "b"])

    def test_mean_boolean(self):
        self.assertRaises(TypeError, mean, True)

    def test_stddev_number_list(self):
        self.assertEqual(stddev([1, 2, 3]), 1)

    def test_stddev_float_list(self):
        self.assertAlmostEqual(stddev([1.1, 2.2, 3.3]), 1.1)

    def test_stddev_empty_list(self):
        self.assertRaises(ZeroDivisionError, stddev, [])

    def test_stddev_string(self):
        self.assertRaises(TypeError, stddev, "a")

    def test_stddev_string_list(self):
        self.assertRaises(TypeError, stddev, ["a", "b"])

    def test_stddev_list_with_numbers_and_strings(self):
        self.assertRaises(TypeError, stddev, [1, "b"])

    def test_stddev_boolean(self):
        self.assertRaises(TypeError, stddev, True)

    def test_median_number_list(self):
        self.assertEqual(median([1, 2, 3]), 2)

    def test_median_number_even_list(self):
        self.assertAlmostEqual(median([1, 2, 3, 4]), 2.5)

    def test_median_float_list(self):
        self.assertAlmostEqual(median([1.1, 2.2, 3.3]), 2.2)

    def test_median_float_even_list(self):
        self.assertAlmostEqual(median([1.1, 2.2, 3.3, 4.4]), 2.75)

    def test_median_empty_list(self):
        self.assertRaises(ValueError, median, [])

    def test_median_string(self):
        self.assertRaises(TypeError, median, "a")

    def test_median_string_list(self):
        self.assertRaises(TypeError, median, ["a", "b"])

    def test_median_list_with_numbers_and_strings(self):
        self.assertRaises(TypeError, median, [1, "b"])

    def test_median_boolean(self):
        self.assertRaises(TypeError, median, True)

    def test_1quartil_number_list(self):
        self.assertEqual(nquartil([1, 2, 3], 1), 1)

    def test_1quartil_number_even_list(self):
        self.assertAlmostEqual(nquartil([1, 2, 3, 4], 1), 1.25)

    def test_1quartil_float_list(self):
        self.assertAlmostEqual(nquartil([1.1, 2.2, 3.3], 1), 1.1)

    def test_1quartil_float_even_list(self):
        self.assertAlmostEqual(nquartil([1.1, 2.2, 3.3, 4.4], 1), 1.375)

    def test_1quartil_empty_list(self):
        self.assertRaises(ValueError, nquartil, [], 1)

    def test_1quartil_string(self):
        self.assertRaises(TypeError, nquartil, "a", 1)

    def test_1quartil_string_list(self):
        self.assertRaises(TypeError, nquartil, ["a", "b"], 1)

    def test_1quartil_list_with_numbers_and_strings(self):
        self.assertRaises(TypeError, nquartil, [1, "b"], 1)

    def test_1quartil_boolean(self):
        self.assertRaises(TypeError, nquartil, True, 1)

    def test_2quartil_number_list(self):
        self.assertEqual(nquartil([1, 2, 3], 2), 2)

    def test_2quartil_number_even_list(self):
        self.assertAlmostEqual(nquartil([1, 2, 3, 4], 2), 2.5)

    def test_2quartil_float_list(self):
        self.assertAlmostEqual(nquartil([1.1, 2.2, 3.3], 2), 2.2)

    def test_2quartil_float_even_list(self):
        self.assertAlmostEqual(nquartil([1.1, 2.2, 3.3, 4.4], 2), 2.75)

    def test_2quartil_empty_list(self):
        self.assertRaises(ValueError, nquartil, [], 2)

    def test_2quartil_string(self):
        self.assertRaises(TypeError, nquartil, "a", 2)

    def test_2quartil_string_list(self):
        self.assertRaises(TypeError, nquartil, ["a", "b"], 2)

    def test_2quartil_list_with_numbers_and_strings(self):
        self.assertRaises(TypeError, nquartil, [1, "b"], 2)

    def test_2quartil_boolean(self):
        self.assertRaises(TypeError, nquartil, True, 2)

    def test_2quartil_median(self):
        self.assertAlmostEqual(nquartil([1.1, 2.2, 3.3, 4.4], 2), median([1.1, 2.2, 3.3, 4.4]))

    def test_3quartil_number_list(self):
        self.assertEqual(nquartil([1, 2, 3], 3), 3)

    def test_3quartil_number_even_list(self):
        self.assertAlmostEqual(nquartil([1, 2, 3, 4], 3), 3.75)

    def test_3quartil_float_list(self):
        self.assertAlmostEqual(nquartil([1.1, 2.2, 3.3], 3), 3.3)

    def test_3quartil_float_even_list(self):
        self.assertAlmostEqual(nquartil([1.1, 2.2, 3.3, 4.4], 3), 4.125)

    def test_3quartil_empty_list(self):
        self.assertRaises(ValueError, nquartil, [], 3)

    def test_3quartil_string(self):
        self.assertRaises(TypeError, nquartil, "a", 3)

    def test_3quartil_string_list(self):
        self.assertRaises(TypeError, nquartil, ["a", "b"], 3)

    def test_3quartil_list_with_numbers_and_strings(self):
        self.assertRaises(TypeError, nquartil, [1, "b"], 3)

    def test_3quartil_boolean(self):
        self.assertRaises(TypeError, nquartil, True, 3)

    def test_5quartil(self):
        self.assertRaises(ValueError, nquartil, [1, 2, 3], 5)

    def test_none_quartil(self):
        self.assertRaises(TypeError, nquartil, [1, 2, 3], None)

    def test_string_quartil(self):
        self.assertRaises(TypeError, nquartil, [1, 2, 3], "one")

    def test_20percentil_number_list(self):
        self.assertEqual(npercentil([1, 2, 3], 20), 1)

    def test_20percentil_number_even_list(self):
        self.assertAlmostEqual(npercentil([1, 2, 3, 4], 20), 1)

    def test_50percentil_number_even_list(self):
        self.assertAlmostEqual(npercentil([1, 2, 3, 4], 50), 2.5)

    def test_20percentil_float_list(self):
        self.assertAlmostEqual(npercentil([1.1, 2.2, 3.3], 1), 3.3)

    def test_20percentil_float_even_list(self):
        self.assertAlmostEqual(npercentil([1.1, 2.2, 3.3, 4.4], 1), 4.4)

    def test_20percentil_empty_list(self):
        self.assertRaises(ValueError, npercentil, [], 1)

    def test_20percentil_string(self):
        self.assertRaises(TypeError, npercentil, "a", 1)

    def test_20percentil_string_list(self):
        self.assertRaises(TypeError, npercentil, ["a", "b"], 1)

    def test_20percentil_list_with_numbers_and_strings(self):
        self.assertRaises(TypeError, npercentil, [1, "b"], 1)

    def test_20percentil_boolean(self):
        self.assertRaises(TypeError, npercentil, True, 1)

    def test_string_percentil(self):
        self.assertRaises(TypeError, npercentil, [1, 2, 3, 4], "string")

    def test_200_percentil(self):
        self.assertRaises(ValueError, npercentil, [1, 2, 3, 4], 200)

    def test_read_from_text_file(self):
        list = "45,43,23,7,83,11,0"

        f1 = open("correct.txt", "w+")
        f1.write(list)
        f1.close()

        power_list = myPowerList()
        power_list.readFromTextFile("correct.txt")

        self.assertEqual(str(power_list), list)

    def test_read_from_invalid_text_file(self):
        list = "f,43,23,7,83,11,HELLO WORLD"

        f1 = open("incorrect.txt", "w+")
        f1.write(list)
        f1.close()

        power_list = myPowerList()
        self.assertRaises(TypeError, power_list.readFromTextFile, "incorrect.txt")

    def test_read_file_not_exists(self):
        power_list = myPowerList()

        self.assertRaises(FileNotFoundError, power_list.readFromTextFile, "404.txt")

    def test_read_invalid_file(self):
        power_list = myPowerList()
        self.assertRaises(TypeError, power_list.readFromTextFile, 55)

    def test_create_user_list(self):
        userlist = UserList()

        user1 = User('user1', 'address1', '1234567890', 'user@user.com')
        user2 = User('user2', 'address2', '9876543210', 'user2@user2.com')

        userlist.addItem(user1)
        userlist.addItem(user2)

        self.assertEqual(str(userlist), repr(user1) + "," + str(user2))

    def test_create_userlist_non_user_datatype(self):
        userlist = UserList()

        self.assertRaises(TypeError, userlist.addItem, "User")

    def test_save_load_user_records(self):
        filename = 'test.out'

        userlist = UserList()

        user1 = User('user3', 'address3', '1234567890', 'user3@user3.com')
        user2 = User('user4', 'address4', '9876543210', 'user4@user4.com')

        userlist.addItem(user1)
        userlist.addItem(user2)

        userlist.exportList(filename)

        exportedUserList = UserList()
        exportedUserList.importList(filename)

        self.assertEqual(str(userlist), str(exportedUserList))

    def test_search_user_in_list(self):
        userlist = UserList()

        user1 = User('user1', 'address1', '1234567890', 'user@user.com')
        user2 = User('user2', 'address2', '9876543210', 'user2@user2.com')
        user3 = User('user3', 'address3', '1234567890', 'user3@user3.com')
        user4 = User('user4', 'address4', '9876543210', 'user4@user4.com')

        userlist.addItem(user1)
        userlist.addItem(user2)
        userlist.addItem(user3)
        userlist.addItem(user4)

        userfound = userlist.searchByUserName("user3")

        self.assertEqual(user3, userfound)

    def test_search_user_not_in_list(self):
        userlist = UserList()

        user1 = User('user1', 'address1', '1234567890', 'user@user.com')
        user2 = User('user2', 'address2', '9876543210', 'user2@user2.com')
        user3 = User('user3', 'address3', '1234567890', 'user3@user3.com')
        user4 = User('user4', 'address4', '9876543210', 'user4@user4.com')

        userlist.addItem(user1)
        userlist.addItem(user2)
        userlist.addItem(user3)
        userlist.addItem(user4)

        self.assertRaises(KeyError, userlist.searchByUserName, "user5")

    def test_search_none(self):
        userlist = UserList()

        user1 = User('user1', 'address1', '1234567890', 'user@user.com')
        user2 = User('user2', 'address2', '9876543210', 'user2@user2.com')
        user3 = User('user3', 'address3', '1234567890', 'user3@user3.com')
        user4 = User('user4', 'address4', '9876543210', 'user4@user4.com')

        userlist.addItem(user1)
        userlist.addItem(user2)
        userlist.addItem(user3)
        userlist.addItem(user4)

        self.assertRaises(KeyError, userlist.searchByUserName, None)


if __name__ == '__main__':
    unittest.main()
