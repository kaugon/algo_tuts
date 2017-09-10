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
    itr = 0
    n = len(data)
    for i in range(n):
        min_i = i
        for j in range(i, n):
            itr += 1
            if data[j] < data[min_i]:
                min_i = j
        if min_i != i:
            data[min_i], data[i] = data[i], data[min_i]
        #logging.debug("Iteration %s : %s" % (itr,data))
    return data

def insertion_sort(data):
    # sort data as it arrives
    # at ith iteration data on left of i is sorted
    # data on right of i is not yet processed
    itr = 0
    n = len(data)
    for i in range(n):
        for j in range(i, 0, -1):
            itr += 1
            if data[j] > data[j-1]:
                break
            data[j-1], data[j] = data[j], data[j-1]
            #logging.debug("Iteration %s : %s" % (itr,data))
    return data

def shell_sort(data):
    # base sort is still insertion sort
    # instead of comparing every next element, cmp only hth element 
    # i.e. h-sorting array
    # keep decrementing step value h as per knuth sequence
    itr = 0
    n = len(data)

    # kunth sequence # 1,4,9,13 
    h = 1;
    while h <= int(n/3):
        h = 3*h + 1
 
    # descending h-sorting
    while h >= 1:
        # insertion sort with step of h
        for i in range(h, n):
            for j in range(i, h-1, -1*h):
                itr += 1
                if data[j] < data[j-h]:
                    data[j-h], data[j] = data[j], data[j-h]
                    #logging.debug("Iteration %s h(%s) len(%s) xy(%s %s) : %s" % (
                    #    itr,h,i,j,j-h,data))
                else:
                    break;
        h = int(h/3)
    return data     
