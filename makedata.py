#!/usr/bin/env python
"""
python makedata.py > kalman1d.data.R
"""

import numpy as np

# Simple kalman filter example - gaussian updates and observations

f_off = 0.1
f_mul = -1.01
f_std = 0.3

h_off = 1.2
h_mul = 0.4
h_std = 0.7

n = 100 # num obs

x = [1.23] # states, with initial value

# generate states, markov style
for i in range(1,n):
	x.append(f_off + np.random.normal(f_mul * x[-1], f_std))

# generate observations
y = [h_off + np.random.normal(h_mul * datum, h_std) for datum in x]

# write R data
print "N <- %i" % n
print "y <- structure(c(" +  ", ".join(map(str, y)) + "), .Dim=c(%i))" % len(y)
print "# x <- structure(c(" +  ", ".join(map(str, x)) + "), .Dim=c(%i))" % len(x)

