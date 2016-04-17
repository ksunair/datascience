import sys
import numpy

def get_numbers():
    usr_input = raw_input("Enter numbers seperated by a comma: ")
    inputValues = usr_input.split(',')
    intValues = []
    for value in inputValues:
        intValues.append(int(value))
    return intValues

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

input_list = get_numbers()
print "Biggest: ", find_biggest_number(input_list)
print "Smallest: ", find_smallest_number(input_list)
print "Mean: ", numpy.mean(input_list)
sorted_list = sorted(input_list)
print sorted_list