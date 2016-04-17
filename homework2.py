import sys
import numpy


def find_biggest_number(mylist):
    max = sys.maxint * -1
    for item in mylist:
        if max < item:
            max = item
    return max

def find_smallest_number(mylist):
    min = sys.maxint
    for item in mylist:
        if min > item:
            min = item
    return min

grades = {
    "Ben": [80, 90, 100],
    "Zach": [70, 85, 50],
    "Meghan": [100, 90, 15, 90]
}

for item, values in grades.iteritems():
    print item,":"
    print "Biggest: ", find_biggest_number(values)
    print "Smallest: ", find_smallest_number(values)
    print "Mean: ", numpy.mean(values)
    print "Sorted: ", sorted(values)