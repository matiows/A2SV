#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumToys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY prices
#  2. INTEGER k
#

def maximumToys(prices, k):
    prices.sort()
    run_sum = 0
    
    for i in range(len(prices)):
        if (run_sum + prices[i]) <= k:
            run_sum += prices[i]
        
        else:
            return i
