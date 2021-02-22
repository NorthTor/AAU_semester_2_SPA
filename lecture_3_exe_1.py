#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 13:10:00 2021

@author: torkaufmanngjerde
"""
import multiprocessing
import numpy as np
import time


def icircle(L):
    # L = number of pairs(x,y)
    x = np.random.rand(1,L) #generate x, y arrays
    y = np.random.rand(1,L)
    x = np.power(x,2) # Raise to the power of 2
    y = np.power(y,2)
    z = np.add(x,y) # Add the pairs 
    z = np.sqrt(z)  # Take square root of each entry in z vector
    nbr  = np.count_nonzero(z < 1) # count how many entries satisfy > 1 
    return nbr # Done, return the number of elements in L that was < 1       

def parpi(M, L, N):
    # M = number of workers
    # L = number of pairs (x,y)
    # N = number of realizations
    start = time.time()
    
    pool = multiprocessing.Pool(processes=(M))
    results = [pool.apply_async(icircle, args=(L,)) for x in range(0,N)]
    Z_array  = [p.get() for p in results]
    end = time.time()
    
    sum_M = np.sum(Z_array)
    
    pi_estimate = (4*sum_M)/(L*N)
    
    print('     Real Pi:', 3.14159265359)
    print('Estimated Pi:',pi_estimate)
    print('  Time taken:', end-start, 'second(s)')
    
    

if __name__ == '__main__':
   parpi(4, 1*10**8, 1)

 