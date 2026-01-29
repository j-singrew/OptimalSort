import pandas as pd
from cpp import run_c_insertion_sort,run_c_heap_sort,run_c_three_way_quick_sort,run_c_shell_sort,run_c_merge_sort,run_iteration_metrics

strategy_map = {
    "small_array": ["InsertionCore"],
    "medium_array": ["PartitionCore", "HeapFallback"],
    "high_duplicate": ["CountPath"],
    "reverse_sorted": ["ReverseAware"]
}

strategy_to_algorithm = {
    "InsertionCore": ["InsertionSort"],
    "PartitionCore": ["QuickSort"],
    "HeapFallback": ["HeapSort"],
    "CountPath": ["CountingSort"],
    "ReverseAware": ["HeapSort"] 
}
Algorithm_map = {
     "InsertionSort": run_c_insertion_sort,
    "QuickSort": run_c_three_way_quick_sort,
    "HeapSort": run_c_heap_sort,
    "MergeSort":run_c_merge_sort,
    "ShellSort":run_c_shell_sort,
}

duplicate_map = {
    "low_duplicate": ["PartitionCore", "HeapFallback"],  
    "high_duplicate": ["CountPath"]                      
}


run_map = {
    "sorted": ["InsertionCore"],
    "nearly_sorted": ["InsertionCore"],
    "random": ["PartitionCore", "HeapFallback"],
    "zigzag": ["PartitionCore", "HeapFallback"],
    "reverse_sorted": ["ReverseAware"]
}


def numb_run(normalised_run: float):
    if normalised_run <= 0.05:
        return run_map["sorted"]
    elif normalised_run <= 0.1:
        return run_map["nearly_sorted"]
    elif normalised_run <= 0.6:
        return run_map["random"]
    else:
        return run_map["zigzag"]

def D_ratio(dup_ratio: float):
    if dup_ratio <= 0.4:
        return duplicate_map["low_duplicate"]
    else:
        return duplicate_map["high_duplicate"]
    
def Get_best_alg(size_key, run_key, dup_key):

    list(set(size_key) & set(run_key) & set(dup_key))
    return



def vector_analytics(arr:list,feature_vectors: list, benchmark_csv: str,num_runs: int):
    results = []
    benchmark_df = pd.read_csv(benchmark_csv)

    for vector in feature_vectors:
        N, normalised_runs, duplicate_ratio = vector


        if N < 100_000:
            size_key = "small_array"
        elif N < 1_000_000:
            size_key = "medium_array"
        else:
            size_key = "large_array"


        run_key = numb_run(normalised_runs)
        dup_key = D_ratio(duplicate_ratio)


        candidates = Get_best_alg(size_key, run_key, dup_key)


        subset = benchmark_df[
            (benchmark_df['algorithm_name'].isin(candidates)) &
            (benchmark_df['N'] == N)
        ]

        if not subset.empty:
            best_alg = subset.loc[subset['avg_time_ms'].idxmin(), 'algorithm_name']
        else:
            best_alg = candidates[0] if candidates else None



        run_iteration_metrics(arr,strategy_to_algorithm[best_alg],num_runs)
        results.append({
            "N": N,
            "normalised_run": normalised_runs,
            "duplicate_ratio": duplicate_ratio,
            "candidates": candidates,
            "selected_algorithm": best_alg
        })

    return results
