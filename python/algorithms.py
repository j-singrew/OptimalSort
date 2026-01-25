import numpy as np
import csv

#target['N'],
#normalised_runs,
#duplicate_ratio
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


def numb_run(normalised_run:float):

    #sortedness
    if normalised_run <= 0.05:
        return "sorted"
    elif normalised_run <= 0.1:
        return "nearly_sorted"
    elif normalised_run <= 0.6:
        return "random"
    else:
        return "zigzag"

def D_ratio(duplicate_ratio:float):
    if duplicate_ratio  <= 4.0:
        return "low_duplicate"
    if duplicate_ratio  >= 5.0:      
        return "high_duplicate"
    
def  Get_best_alg(A_arr,run_rate,duplicate_ratio):

    size_algos = array_algorithm_map[A_arr]
    run_algos = array_algorithm_map[run_rate]
    dup_algos = array_algorithm_map[duplicate_ratio]


    return list(set(size_algos) & set(run_algos) & set(dup_algos))


def vectur_analytics(feature_vecter:list):
    results = []

    for vector in feature_vecter:
        N, normalised_runs, duplicate_ratio = vector

        if N  < 100_000:
            A_arr = "small_array"


        elif 100_000 >= N < 1_000_000:
            A_arr = "medium_array"


        elif  N >= 1_000_000:
            A_arr = "large_array"

      


        run_rate =  vectur_analytics(normalised_runs)
        duplicate_ratio = D_ratio(duplicate_ratio)

        candidates = Get_best_alg(A_arr,run_rate,duplicate_ratio)

        best_fit = candidates[0] if candidates else None

        results.append({
            "N": N,
            "normalised_run": normalised_runs,
            "duplicate_ratio": duplicate_ratio,
            "candidates": candidates,
            "selected_algorithm": best_fit
        })
    
    return results


