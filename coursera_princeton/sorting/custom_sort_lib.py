############################################
### Copyright 2017 @ Kau Gon
############################################
## All elementery sort algos
############################################
import logging

#########################

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

#########################

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

#########################

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

#########################
## Merge Sort - Recursive
#########################
__ms_itr = 0
def __ms_merge(data, aux, low, mid, hi):
    global __ms_itr
    #logging.debug("Iteration %s : lmh (%s %s %s)" % (__ms_itr, low, mid, hi))
    ###logging.debug("Iteration %s : aux: %s" % (__ms_itr,aux))
    k = low
    while k <= hi:
        aux[k] = data[k]
        k += 1
    ###logging.debug("Iteration %s : aux: %s" % (__ms_itr,aux))

    i, j, k = low, mid+1, low
    while k <= hi:
        if i > mid: 
            data[k] = aux[j]
            j += 1
        elif j > hi: 
            data[k] = aux[i]
            i += 1
        elif aux[i] <= aux[j]: 
            data[k] = aux[i]
            i += 1
        else:
            data[k] = aux[j]
            j += 1
        k += 1
    #logging.debug("Iteration %s : %s" % (__ms_itr,data))
    __ms_itr += 1

def __ms_sort(data, aux, low, hi):
    if hi <= low: return
    mid = low + int((hi-low)/2)
    __ms_sort(data, aux, low, mid)
    __ms_sort(data, aux, mid+1, hi)
    # if both halfs already in sorted merge, we dont need to do anything. 
    if data[mid] <= data[mid+1]: return
    __ms_merge(data, aux, low, mid, hi)

def merge_sort(data):
    global __ms_itr
    __ms_itr=0
    n = len(data)
    aux = [int(-1)]*n
    __ms_sort(data, aux, 0, n-1)
    return data

###############################
## Merge Sort non-recursive
###############################
def __ms_sort_nr(data, aux, low, hi):
    global __ms_itr
    ws = 1
    while ws <= hi+1:
        #logging.debug("Iteration %s : ws(%s)" % (__ms_itr,ws))
        for i in range(low+ws, hi+1, 2*ws):
            # optimize here if its already sorted
            if data[i-1] > data[i]:
                h = min(i+ws-1, hi)
                __ms_merge(data, aux, i-ws, i-1, h)
        ws = ws+ws

def merge_sort_nr(data):
    global __ms_itr
    __ms_itr=0
    n = len(data)
    aux = [int(-1)]*n
    __ms_sort_nr(data, aux, 0, n-1)
    return data


