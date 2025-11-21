"""
	• Implement the 7 Patterns: Write functions to generate arrays for each of the 7 dataset patterns (Random, Sorted, Reverse Sorted, High Duplicates, Near Sorted, etc.).
Vary the Size ($N$): Make the size ($N$) an input parameter for these functions, allowing you to generate small, medium, and large sub-types of each pattern (e.g., generate_random_array(N=1000000)).
"""
import numpy as np
from numpy import random

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

def generate_Near_Sorted_Array(N:int,swap_percentage: float = SWAP_PERCENTAGE) -> np.ndarray:

    near_sorted = MASTER_SORTED[:N].copy()
    num_swaps = int(N * swap_percentage)


    for i in range(num_swaps):

        ida ,idb = np.random.randint(0,N),np.random.randint(0,N)

        if ida != idb:
            near_sorted[ida],near_sorted[idb] = near_sorted[idb], near_sorted[ida]

    return near_sorted

def generate_random_order(N:int) -> np.array:

    return MASTER_UNSORTED[:N].copy()

def generate_already_sorted(N:int) -> np.array:

    return MASTER_SORTED[:N].copy

def generate_reverse_sorted(N:int) ->np.array:

    return MASTER_SORTED[:N][::-1].copy()

def generate_no_duplicate(N:int)->np.array:

    return MASTER_UNIQUE[:N].copy()


def generate_high_duplicate(N:int) ->np.asarray:

    return MASTER_DUPLICATE[:N].copy()






def DataGeneration():

    datasets = {}

    mob_spawner = [
        ("random_order", generate_random_order),
        ("sorted_order", generate_already_sorted),
        ("reverse_sorted", generate_reverse_sorted),
        ("near_sorted", generate_Near_Sorted_Array),
        ("no_duplicates", generate_no_duplicate),
        ("high_duplicates", generate_high_duplicate),
    ]

    for key, value in mob_spawner:


        arr_small = value(N_SMALL)
        arr_medium = value(N_MEDIUM)
        arr_large = value(N_LARGE)


        datasets[key] = (arr_small, arr_medium, arr_large)


    print("All data generated")
    return datasets