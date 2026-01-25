import numpy as np
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
        return array_algorithm_map["sorted"]["reverse_sorted"]
    elif normalised_run <= 0.1:
        return array_algorithm_map["nearly_sorted"]
    elif normalised_run <= 0.6:
        return array_algorithm_map["random"]
    else:
        return array_algorithm_map["zigzag"]

def D_ratio(run_ratio:float):
    if D_ratio  <= 4.0:
        return array_algorithm_map["low_duplicate"]
    if D_ratio  >= 5.0:      
        return array_algorithm_map["high_duplicate"]  


def vectur_analytics(feature_vecter:list):
    for vector in feature_vecter:
        N = vector[0]
        N_runs = vector[1]
        D_ratio_ = vector[2]
        if N  < 100_000:
            A_arr = array_algorithm_map["small_array"]
            run_rate =  vectur_analytics(N_runs)
            duplicate_ratio = D_ratio(D_ratio_)

        elif 100_000 >= N < 1_000_000:
            A_arr = array_algorithm_map["medium_array"]
            run_rate =  vectur_analytics(N_runs)
            duplicate_ratio = D_ratio(D_ratio_)


        elif  N >= 1_000_000:
            A_arr = array_algorithm_map["large_array"]
            run_rate =  vectur_analytics(N_runs)
            duplicate_ratio = D_ratio(D_ratio_)
      





