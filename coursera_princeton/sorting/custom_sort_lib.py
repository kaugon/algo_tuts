############################################
### Copyright 2017 @ Kau Gon
############################################
## All elementery sort algos
############################################
import logging

def selection_sort(data):
    ## - At ith iteration, element at ith position is at its right place
    ## - elements left of i, is sorted and smaller than a[i]
    ## - anything right of i, is larger than a[i]
    n = len(data)
    itr = 0
    for i in range(n):
        #logging.debug("Iteration %s : %s" % (itr,data))
        min_i = i
        for j in range(i, n):
            itr += 1
            if data[j] < data[min_i]:
                min_i = j
        if min_i != i:
            data[min_i], data[i] = data[i], data[min_i]
    return data

def insertion_sort(data):
    # sort data as it arrives
    # at ith iteration data on left of i is sorted
    # data on right of i is not yet processed
    n = len(data)
    itr = 0
    for i in range(n):
        for j in range(i, 0, -1):
            #logging.debug("Iteration %s : %s" % (itr,data))
            itr += 1
            if data[j] > data[j-1]:
                break
            data[j-1], data[j] = data[j], data[j-1]
    return data
