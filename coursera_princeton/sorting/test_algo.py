############################################
### Copyright 2017 @ Kau Gon
############################################
import random
import time

def generate_data():
    data_s = range(0, 10000)
    data_r = [i for i in data_s]
    random.shuffle(data_r)
    return data_s, data_r

if __name__ == '__main__':
    data_sorted, data_random = generate_data()
    #print "Input: %s" % data_random
    #print "Expected: %s" % data_sorted

    algos = (sorted, sorted)
    for sortalgo in algos:
        print "\nSorting using: %s" % (sortalgo.__name__)
        start = time.time()
        data_new = sortalgo(data_random)
        stop = time.time()
        print "Execution time: %s" % (stop-start)
        #print "Output: %s" % data_new
        assert(data_new == data_sorted)
        
