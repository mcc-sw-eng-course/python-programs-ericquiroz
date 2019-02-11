from copy import deepcopy


class myPowerList:
    def __init__(self):
        self.list = []

    def isValueNum(self, value):
        try:
            val = float(value)
        except ValueError:
            return False;

        return True;
    
    def __str__(self):
        return ','.join(map(str, self.list))

    def addItem(self, item):
        if self.isValueNum(item):
            # print(f'Adding {item} to list')
            self.list.append(item)
        else:
            # print(f'Invalid number: {item}')
            raise TypeError

    def readFromTextFile(self, fileName):
        if type(fileName) == str:
            file = open(fileName, 'r')
            try:
                # print(f'Exporting list to file {fileName}')
                textList = file.readline()
                tmpList = textList.split(',')
                for item in tmpList:
                    self.addItem(item)
            finally:
                file.close()
        else:
            raise TypeError
