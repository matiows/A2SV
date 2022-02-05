#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    if len(str(n)) == 1:
        return n
    
    sum = 0
    for val in str(n):
        sum += int(val)
    sum*=k
    
    return superDigit(sum, 1)