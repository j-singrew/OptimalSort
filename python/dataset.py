"""
	• Implement the 7 Patterns: Write functions to generate arrays for each of the 7 dataset patterns (Random, Sorted, Reverse Sorted, High Duplicates, Near Sorted, etc.).
Vary the Size ($N$): Make the size ($N$) an input parameter for these functions, allowing you to generate small, medium, and large sub-types of each pattern (e.g., generate_random_array(N=1000000)).
"""
import numpy as np
from numpy import random

def generateNearSortedArray(sorted_Array ,swap_percentage):
    near_sorted = sorted_Array.copy
    N =len(near_sorted)

    num_swaps = int(N * swap_percentage)


    for i in range(num_swaps):

        ida ,idb = np.random.randint(0,N-1),np.random.randint(0,N-1)
        near_sorted[ida],near_sorted[idb] = near_sorted[idb], near_sorted[ida]

    return near_sorted

def DataGeneration():
    N_small = 20
    N_medium = 100_000
    N_large  = 1_000_000
    N_UNIQUE = 1000

    #random-Array ,small,medium,large
    randomArrSmall =  random.randint(low=1,high=100,size=N_small)

    randomArrMedium  = random.randint(low=1, high=1_000_000,size=N_medium)

    randomArrLarge = random.randint(low=1,high=10_000_000,size=N_large)

    #sorted-Array
    Master_Array = np.random.randint(low=1, high=10000000, size=1_000_000)
    sorted_Array = np.sort(Master_Array)

    randomArrSmall = sorted_Array[:N_small].copy()


    randomArrMedium  = sorted_Array[:N_medium].copy()


    randomArrLarge =  sorted_Array[:N_large].copy()

    #near sorted-Array
    swap_percentage = 0.5

    near_sorted_array = generateNearSortedArray(sorted_Array,swap_percentage)

    randomArrSmall = near_sorted_array[:N_small].copy()

    randomArrMedium  = near_sorted_array[:N_medium].copy()

    randomArrLarge = near_sorted_array[:N_large].copy()

    #reverse sorted-Array 

    reversed_Array = sorted_Array[::-1].copy()

    randomArrSmall = reversed_Array[:N_small].copy()


    randomArrMedium  = reversed_Array[:N_medium].copy()


    randomArrLarge = reversed_Array[:N_large].copy()

    #no Duplicate-Array

    unique_Master_Array = np.arange(N_large)
    np.random.shuffle(unique_Master_Array)

    randomArrSmall = unique_Master_Array[:N_small].copy()

    randomArrMedium  =  unique_Master_Array[:N_medium].copy()

    randomArrLarge =  unique_Master_Array[:N_large].copy()

    #high duplicate-Array

    MASTER_DUPLICATE_ARRAY = np.random.randint(low=0, high=N_UNIQUE, size=N_large)  

    duplicateArrSmall = MASTER_DUPLICATE_ARRAY[:N_small].copy()


    duplicateArrMedium = MASTER_DUPLICATE_ARRAY[:N_medium].copy()


    duplicateArrLarge = MASTER_DUPLICATE_ARRAY[:N_large].copy()
