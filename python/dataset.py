"""
	• Implement the 7 Patterns: Write functions to generate arrays for each of the 7 dataset patterns (Random, Sorted, Reverse Sorted, High Duplicates, Near Sorted, etc.).
Vary the Size ($N$): Make the size ($N$) an input parameter for these functions, allowing you to generate small, medium, and large sub-types of each pattern (e.g., generate_random_array(N=1000000)).
"""
import numpy as np
from numpy import random


def DataGeneration():
    N_small = 20
    N_medium = 100_000
    N_large  = 1_000_000


    #random-Array ,small,medium,large
    randomArrSmall =  random.randint(low=1,high=100,size=N_small)

    randomArrMedium  = random.randint(low=1, high=1_000_000,size=N_medium)

    randomArrLarge = random.randint(low=1,high=10_000_000,size=N_large)

    #sorted-Array
    u_Array = np.random.randint(low=1, high=10000000, size=1_000_000)
    sorted_Array = np.sort(u_Array)

    randomArrSmall = sorted_Array[:N_small].copy()


    randomArrMedium  = sorted_Array[:N_medium].copy()


    randomArrLarge =  sorted_Array[:N_large].copy()


    #near sorted-Array





    #reverse sorted-Array 
    #no Duplicate-Array
    #high duplicate-Array

