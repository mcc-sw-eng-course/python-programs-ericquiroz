# Exercise 9


def convert_to_roman(number):
    if type(number) == int:
        if 0 < number <= 3999:
            aux = number
            count = 0
            res = ''

            # 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1
            rom = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
            num = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

            while aux > 0:
                while aux >= num[count]:
                    aux -= num[count]
                    res += rom[count]
                if count < 13:
                    count += 1

            return res

        else:
            raise ValueError("Use only numbers between 1 and 3999")
    else:
        raise TypeError("Use only whole numbers")
