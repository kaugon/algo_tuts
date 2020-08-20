############################################
### Copyright 2017-2020 @ Kau Gon
############################################
## All elementery sort algos
############################################
import logging
import random

#########################

def selection_sort(data):
    ## - At ith iteration, find the min element in the remaining array
    ## - Exchange it with element at ith position 
    ## - So at the end of ith iteration, element at ith position is 
    ##   at its right place
    
    ## - elements left of i, is sorted and smaller than a[i]
    ## - anything right of i, is larger than a[i]
    
    ## In best case scenario, if array is already sorted, its still going 
    ## to go thru all O(N^2) compares. This sort is independent of input order
    
    itr = 0
    n = len(data)
    for i in range(n):
        min_index = i
        for j in range(i, n):
            itr += 1
            if data[j] < data[min_index]:
                min_index = j
        if min_index != i:
            data[min_index], data[i] = data[i], data[min_index]
        #logging.debug("Iteration %s : %s" % (itr,data))
    return data

#########################

def insertion_sort(data):
    # sort data as it arrives
    # i.e. element at ith position is always moved to right place
    # at ith iteration data on left of i is sorted
    
    # data on right of i is not yet processed
    # i.e. it doesnt access whole array during ith iteration, 
    # bit opposite way to selection
    # so by the end of the array for ith position, array is sorted on left so less compares are required.
    
    # note that in selection sort for an iteration we had O(N) compares, but only 1 exchange.
    # in insertion sort we can have O(N) compares, but we need to do O(N) exhanges
    # so it may seem to be slower... but.. 
    # but in avg case total comparisons and exchanges are 1/4*O(N^2) i.e. less than selection sort.
    
    # with already sorted array, O(N) happens to be best case.
    
    # with reverse sorted array, it does all O(N^2) compares and exchanges and performs worst than 
    # selection sort wrt exhanges.
    
    # For partially sorted i.e. avg case, with smaller N, insertion sort is still right one to use 
    # (over merge/quick sort) for all practical purposes.
    
    
    itr = 0
    n = len(data)
    for i in range(n):
        for j in range(i, 0, -1): # reverse loop: left side only loop
            itr += 1
            if data[j] > data[j-1]: # found the right place
                break
            data[j-1], data[j] = data[j], data[j-1] # exchange at every step in inner loop
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
    # both low and hi are indices included
    # mid is index to last element of first array
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

###############################
## Quick Sort
###############################
__qs_itr = 0
def __qs_partition(data, low, hi):
    global __qs_itr
    pivot, i, j = low, low+1, hi
    #logging.debug("Iteration %s : lh(%s %s) %s" % (__qs_itr, low, hi, data[low:hi+1]))

    while True:
        # Left: first largest element than pivot
        # dont cross the boundry
        while i<= hi and data[i] <= data[pivot]:
            i += 1 

        # Right: first smallest element than pivot
        # dont cross i
        while j >= i and data[j] > data[pivot]: 
            j -= 1

        #logging.debug("Iteration %s : ij(%s %s)" % (__qs_itr,i,j))

        # this assert would never happen becasue above while condition is j>=i
        # just adding this as sanity for unintended code modification
        assert( j != i)

        # exit condition
        if j < i: break
 
        # put them in correct partitions
        data[i], data[j] = data[j], data[i]
        i += 1
        j -= 1
        #logging.debug("Iteration %s : %s" % (__qs_itr,data))

    # put pivoted element at right jth place
    if pivot != j:
        data[j], data[pivot] = data[pivot], data[j]

    #logging.debug("Iteration %s : p(%s) : %s" % (__qs_itr, j, data))
    __qs_itr += 1

    # pivot elemnt is at j
    return j 

def __qs_sort(data, low, hi):
    # both low and hi are indices included
    # pivot is index to last element of first array

    if low < hi:
        pivot = __qs_partition(data, low, hi)
        # FIXME: boundtry condition checks here ??
        if pivot > low:
            __qs_sort(data, low, pivot-1)   
        if pivot < hi:
            __qs_sort(data, pivot+1, hi)    

def quick_sort(data, shuffle=False):
    global __qs_itr
    __qs_itr = 0
    if shuffle:
        random.shuffle(data)
    __qs_sort(data, 0, len(data)-1)
    return data

def quick_sort_shuffle(data):
    return quick_sort(data, shuffle=True)

###############################
## Heap Sort (Binary)
###############################
__hs_itr = 0
def __hs_sink(data, k, n):
    global __hs_itr
    # parent node of k that should be sinked
    # its children are at 2k+1, 2k+2
    while True:
        __hs_itr += 1
        j = 2*k+1
        # finished thru all child nodes
        if j >= n:
            break
        # pick up bigger child
        v1 = j
        #logging.debug("Iteration %s : n(%s) rcc(%s %s %s)" % (__hs_itr, n, k, j, j+1))
        if j+1 < n and data[v1] < data[j+1]:
            v1 = j+1
        # is child bigger than parent, swap
        if data[k] < data[v1]:
            data[k], data[v1] = data[v1], data[k]
            #logging.debug("Iteration %s : pc(%s %s) : %s" % (__hs_itr, k, v1, data))
            k = v1
        else:
            # parent is at right location
            break

def __hs_construct_heap(data):
    n = len(data)
    # Start with last parent node
    # in tree of n nodes, parent node will always be at n/2
    for k in range(int(n/2)-1, -1, -1):
        __hs_sink(data, k, n) 

def __hs_sort_heap(data):
    global __hs_itr
    n = len(data)
    hi = n-1
    # Root node is always the max
    while True:
        # take root, exchange with last element. Root is t proper place in array
        data[hi], data[0] = data[0], data[hi]
        #logging.debug("Iteration %s : sort(%s) : %s" % (__hs_itr, hi, data))
        # root is at its sorted place
        if hi <= 1:
            break;
        __hs_sink(data, 0, hi)
        hi -= 1 
     
def heap_sort(data):
    global __hs_itr
    __hs_itr = 0
    n = len(data)
    # construct max heap
    __hs_construct_heap(data)
    #logging.debug("Iteration %s : Heap : %s" % (__hs_itr, data))
    # sort heap
    __hs_sort_heap(data)
    return data

