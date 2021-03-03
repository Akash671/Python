""" author akash kumar """

import itertools
import os

numbers = '0123456789'
y = ''
for c in itertools.product(numbers, repeat=4):
    pin = y+''.join(c)
    print pin
    os.system("./xyz "+pin)
