############################################
### Copyright 2017 @ Kau Gon
############################################
## Test framework to test all algos
############################################
import random
import time
import logging
from texttable import Texttable

import custom_sort_lib as mysort
 
def generate_data():
    data_s = range(0, 30000)
    data_r = [i for i in data_s]
    random.shuffle(data_r)
    return data_s, data_s[::-1], data_r

if __name__ == '__main__':
    #logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)
    logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)

    data_sorted, data_sorted_reverse, data_random = generate_data()

    algos = (   sorted, 
                mysort.selection_sort,
                mysort.insertion_sort,
                mysort.shell_sort,
                mysort.merge_sort,
                mysort.merge_sort_nr,
            )

    data_set = {"data_random": data_random, 
                "data_sorted": data_sorted, 
                "data_sorted_reverse": data_sorted_reverse,
               } 

    results = {}
    for sortalgo in algos:
        results[sortalgo.__name__] = {}
            
    for data_type in data_set:
        #logging.info("")
        logging.info("="*25)
        logging.info("Testing data set: %s\n", data_type)
        data_test = data_set[data_type]

        for sortalgo in algos:
            logging.info("Fn: %s" % (sortalgo.__name__))

            # input data
            data_input = [i for i in data_test]
            logging.debug("Input: %s" % data_input)
            logging.debug("Expected: %s" % data_sorted)

            start = time.time()
            data_new = sortalgo(data_input)
            stop = time.time()

            logging.info("Execution time: %s\n" % (stop-start))
            logging.debug("Output: %s" % data_new)

            assert(data_new == data_sorted)

            results[sortalgo.__name__][data_type] = stop-start

    # Print result summary
    table = Texttable()
    len_d = len(data_set.keys())
    table.set_cols_dtype(['t'] + ['t']*len_d)

    header = ["Fn"] + data_set.keys()
    table.add_row(header)
    for sortalgo in algos:
        s_name = sortalgo.__name__ 
        row_s = [s_name]
        for data_type in data_set.keys():
            row_s += ["%s" % (results[s_name][data_type])]
        table.add_row(row_s)    
    print table.draw() + "\n"                
        
            
