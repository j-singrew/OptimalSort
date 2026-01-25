import numpy as np
#target['N'],
#normalised_runs,
#duplicate_ratio

def vectur_analytics(feature_vecter:list):
    array_algorithm_map = {
    "small_array": ["InsertionSort", "Timsort"],
    "medium_array": ["Timsort", "QuickSort", "HeapSort"],
    "large_array": ["QuickSort", "NumPy Sort", "Timsort"],
    "high_duplicate": ["CountingSort", "Timsort"],
    "low_duplicate": ["QuickSort", "HeapSort", "Timsort"],
    "sorted": ["InsertionSort", "Timsort"],
    "reverse_sorted": ["Timsort"],
    "nearly_sorted": ["Timsort"],
    "random": ["QuickSort", "HeapSort", "Timsort"],
    "zigzag": ["QuickSort", "HeapSort"]
}

    for vector in feature_vecter:
        N = vector[0]
        N_runs = vector[1]
        D_ratio = vector[2]





