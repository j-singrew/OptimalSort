"""
	• Implement the 7 Patterns: Write functions to generate arrays for each of the 7 dataset patterns (Random, Sorted, Reverse Sorted, High Duplicates, Near Sorted, etc.).
Vary the Size ($N$): Make the size ($N$) an input parameter for these functions, allowing you to generate small, medium, and large sub-types of each pattern (e.g., generate_random_array(N=1000000)).
"""
import numpy as np
from numpy import random

def generateNearSortedArray(sorted_Array ,swap_percentage):

    near_sorted = sorted_Array.copy()
    N =len(near_sorted)
    num_swaps = int(N * swap_percentage)


    for i in range(num_swaps):

        ida ,idb = np.random.randint(0,N-1),np.random.randint(0,N-1)

        if ida != idb:
            near_sorted[ida],near_sorted[idb] = near_sorted[idb], near_sorted[ida]

    return near_sorted

def DataGeneration():
    N_small = 20
    N_medium = 100_000
    N_large  = 1_000_000
    N_UNIQUE = 1000
    swap_percentage = 0.01
    
    MASTER_UNSORTED = np.random.randint(low=1, high=10_000_000, size=N_large)
    MASTER_SORTED = np.sort(MASTER_UNSORTED)
    MASTER_REVERSED = MASTER_SORTED[::-1].copy()
    MASTER_UNIQUE = np.arange(N_large)
    np.random.shuffle(MASTER_UNIQUE)
    MASTER_DUPLICATE = np.random.randint(low=0, high=N_UNIQUE, size=N_large)


    #random-Array ,small,medium,large
    randomArrSmall =  random.randint(low=1,high=100,size=N_small)

    randomArrMedium  = random.randint(low=1, high=1_000_000,size=N_medium)

    randomArrLarge = random.randint(low=1,high=10_000_000,size=N_large)

    #sorted-Array


    sortedArrSmall =  MASTER_SORTED [:N_small].copy()


    sortedArrMedium  =  MASTER_SORTED [:N_medium].copy()


    sortedArrLarge =   MASTER_SORTED [:N_large].copy()

    #near sorted-Array


    near_sorted_array = generateNearSortedArray( MASTER_SORTED ,swap_percentage)

    nSortedArrSmall = near_sorted_array[:N_small].copy()

    nSortedArrMedium  = near_sorted_array[:N_medium].copy()

    nSortedArrLarge = near_sorted_array[:N_large].copy()

    #reverse sorted-Array 


    reverseArrSmall = MASTER_REVERSED[:N_small].copy()


    reverseArrMedium  = MASTER_REVERSED[:N_medium].copy()


    reverseArrLarge = MASTER_REVERSED[:N_large].copy()

    #no Duplicate-Array


    noDuplicateArrSmall = MASTER_UNIQUE [:N_small].copy()

    noDuplicateArrMedium  =  MASTER_UNIQUE [:N_medium].copy()

    noDuplicateArrLarge =  MASTER_UNIQUE[:N_large].copy()

    #high duplicate-Array

    MASTER_DUPLICATE_ARRAY = np.random.randint(low=0, high=N_UNIQUE, size=N_large)  

    duplicateArrSmall = MASTER_DUPLICATE_ARRAY[:N_small].copy()


    duplicateArrMedium = MASTER_DUPLICATE_ARRAY[:N_medium].copy()


    duplicateArrLarge = MASTER_DUPLICATE_ARRAY[:N_large].copy()
