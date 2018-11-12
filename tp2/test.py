# -*- coding: utf-8 -*-
"""
Author: Balamurali M
Markov Chain Example2
"""

import numpy as np
# Current state
I = np.matrix([[0.5, 0.5]])
# Transition Matrix
T = np.matrix([[.7, 0.3],
               [.6, 0.4]])

T1 = I * T
print ("# After 1 hours")
print (T1)

T2 = T1 * T
print ("# After 2 hours")
print (T2)

T3 = T2 * T
print ("# After 3 hours")
print (T3)
