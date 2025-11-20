"""
	• Implement the 7 Patterns: Write functions to generate arrays for each of the 7 dataset patterns (Random, Sorted, Reverse Sorted, High Duplicates, Near Sorted, etc.).
Vary the Size ($N$): Make the size ($N$) an input parameter for these functions, allowing you to generate small, medium, and large sub-types of each pattern (e.g., generate_random_array(N=1000000)).
"""
from numpy import random


def DataGeneration():
    #random-Array ,small,medium,large
    N_small = 20
    randomArrSmall =  random.randint(low=1,high=100,size=N_small)

    N_medium = 100_000
    randomArrMedium  = random.randint(low=1, high=1_000_000,size=N_medium)

    N_large  = 1_000_000
    randomArrLarge = random.randint(low=1,high=10_000_000,size=N_large)

    #sorted-Array
    #near sorted-Array
    #reverse sorted-Array 
    #no Duplicate-Array
    #high duplicate-Array

