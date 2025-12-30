#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    format = "%a %d %b %Y %H:%M:%S %z"
    
    dt1 = datetime.strptime(t1, format)
    dt2 = datetime.strptime(t2, format)
    
    diff = abs(int((dt1 - dt2).total_seconds()))
    return str(diff)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for _ in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        fptr.write(delta + '\n')

    fptr.close()
