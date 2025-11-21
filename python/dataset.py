"""
	• Implement the 7 Patterns: Write functions to generate arrays for each of the 7 dataset patterns (Random, Sorted, Reverse Sorted, High Duplicates, Near Sorted, etc.).
Vary the Size ($N$): Make the size ($N$) an input parameter for these functions, allowing you to generate small, medium, and large sub-types of each pattern (e.g., generate_random_array(N=1000000)).
"""
import numpy as np
from numpy import random

def generateNearSortedArray(N:int,swap_percentage: float = SWAP_PERCENTAGE) -> np.ndarray:

    near_sorted = MASTER_SORTED[:N].copy()
    num_swaps = int(N * swap_percentage)


    for i in range(num_swaps):

        ida ,idb = np.random.randint(0,N),np.random.randint(0,N)

        if ida != idb:
            near_sorted[ida],near_sorted[idb] = near_sorted[idb], near_sorted[ida]

    return near_sorted

def DataGeneration():
    N_SMALL = 20
    N_MEDIUM = 100_000
    N_LARGE  = 1_000_000
    N_UNIQUE = 1000
    SWAP_PERCENTAGE = 0.01
    
    MASTER_UNSORTED = np.random.randint(low=1, high=10_000_000, size=N_LARGE)
    MASTER_SORTED = np.sort(MASTER_UNSORTED)
    MASTER_REVERSED = MASTER_SORTED[::-1].copy()
    MASTER_UNIQUE = np.arange(N_LARGE)
    np.random.shuffle(MASTER_UNIQUE)
    MASTER_DUPLICATE = np.random.randint(low=0, high=N_UNIQUE, size=N_LARGE)


    #random-Array ,small,medium,large
    randomArrSmall =  random.randint(low=1,high=100,size=N_SMALL)

    randomArrMedium  = random.randint(low=1, high=1_000_000,size=    N_MEDIUM)

    randomArrLarge = random.randint(low=1,high=10_000_000,size=N_LARGE)

    #sorted-Array


    sortedArrSmall =  MASTER_SORTED [:N_SMALL].copy()


    sortedArrMedium  =  MASTER_SORTED [:N_MEDIUM].copy()


    sortedArrLarge =   MASTER_SORTED [:N_LARGE].copy()

    #near sorted-Array


    near_sorted_array = generateNearSortedArray( MASTER_SORTED ,SWAP_PERCENTAGE)

    nSortedArrSmall = near_sorted_array[:N_SMALL].copy()

    nSortedArrMedium  = near_sorted_array[:N_MEDIUM].copy()

    nSortedArrLarge = near_sorted_array[:N_LARGE].copy()

    #reverse sorted-Array 


    reverseArrSmall = MASTER_REVERSED[:N_SMALL].copy()


    reverseArrMedium  = MASTER_REVERSED[:N_MEDIUM].copy()


    reverseArrLarge = MASTER_REVERSED[:N_LARGE].copy()

    #no Duplicate-Array


    noDuplicateArrSmall = MASTER_UNIQUE [:N_SMALL].copy()

    noDuplicateArrMedium  =  MASTER_UNIQUE [:N_MEDIUM].copy()

    noDuplicateArrLarge =  MASTER_UNIQUE[:N_LARGE].copy()

    #high duplicate-Array

    MASTER_DUPLICATE_ARRAY = np.random.randint(low=0, high=N_UNIQUE, size=N_LARGE)  

    duplicateArrSmall = MASTER_DUPLICATE_ARRAY[:N_SMALL].copy()


    duplicateArrMedium = MASTER_DUPLICATE_ARRAY[:N_MEDIUM].copy()


    duplicateArrLarge = MASTER_DUPLICATE_ARRAY[:N_LARGE].copy()
