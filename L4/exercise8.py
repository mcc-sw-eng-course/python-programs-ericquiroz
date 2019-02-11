import math
from decimal import *


def mean(dataset):
    if type(dataset) == list:
        for i in dataset:
            if not (type(i) == int or type(i) == float):
                raise TypeError

        size = len(dataset)

        total = sum(dataset)

        mean = total / size

        return mean
    else:
        raise TypeError

def stddev(dataset):
    if type(dataset) == list:
        for i in dataset:
            if not (type(i) == int or type(i) == float):
                raise TypeError

        meanVal = mean(dataset)
        #print meanVal

        size = len(dataset)
        #print size

        acum = 0

        #Dif with mean
        for data in dataset:
            dif = data - meanVal
            #print dif
            acum = acum + (dif ** 2)

        #print acum

        res = math.sqrt(acum / (size - 1))

        return res;
    else:
        raise TypeError
    
def median(dataset):
    if type(dataset) == list:
        for i in dataset:
            if not (type(i) == int or type(i) == float):
                raise TypeError

        dataset.sort()

        size = len(dataset)

        if size == 0:
            raise ValueError

        if size % 2 == 1:
            val = dataset[int(math.floor(size / 2))]
        else:
            val = (dataset[int(math.floor(size / 2))] + dataset [int(math.floor(size / 2)) - 1]) / 2

        return val;

    else:
        raise TypeError
    
def nquartil(dataset, quartil):
    if type(dataset) == list:
        for i in dataset:
            if not (type(i) == int or type(i) == float):
                raise TypeError

        if type(quartil) == int:
            if 0 < quartil <= 3:

                size = len(dataset)

                if size == 0:
                    raise ValueError

                if quartil == 1:
                    q = (size + 1) / 4
                    #print q

                    if q % 1 == 0:
                        res = dataset[int(q) - 1]
                    else:
                        frac, whole = math.modf(q)
                        whole = int(whole)

                        #print whole, frac

                        res = dataset[whole - 1] + (frac * (dataset[whole] - dataset[whole - 1]))

                elif quartil == 2:
                    res = median(dataset)
                elif quartil == 3:
                    q = 3 * (size + 1) / 4
                    #print q

                    if q % 1 == 0:
                        res = dataset[int(q) - 1]
                    else:
                        frac, whole = math.modf(q)
                        whole = int(whole)

                        #print whole, frac

                        res = dataset[whole - 1] + (frac * (dataset[whole] - dataset[whole - 1]))

                return res;
            else:
                raise ValueError
        else:
            raise TypeError
    else:
        raise TypeError
    
def npercentil(dataset, percentil):
    if type(dataset) == list:
        for i in dataset:
            if not (type(i) == int or type(i) == float):
                raise TypeError

        if type(percentil) == int:

            if 0 < percentil <= 100:
                dataset.sort()

                size = len(dataset)

                if size == 0:
                    raise ValueError

                p = (percentil / 100) * size

                if p % 1 == 0:
                    res = (dataset[int(p) - 1] + dataset[int(p)]) / 2
                else:
                    res = dataset[int(round(p)) - 1]

                return res;
            else:
                raise ValueError
        else:
            raise TypeError

    else:
        raise TypeError

