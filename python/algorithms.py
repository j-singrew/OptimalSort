import pandas as pd

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
     "InsertionSort": c_insertion_sort,
    "QuickSort": custom_sort.c_three_way_quicksort,
    "HeapSort": custom_sort.c_heapsort,
    "MergeSort":custom_sort.c_merge_sort,
    "ShellSort":custom_sort.c_shell_sort,
}

def numb_run(normalised_run: float):
    if normalised_run <= 0.05:
        return "sorted"
    elif normalised_run <= 0.1:
        return "nearly_sorted"
    elif normalised_run <= 0.6:
        return "random"
    else:
        return "zigzag"

def D_ratio(dup_ratio: float):
    if dup_ratio <= 0.4:
        return "low_duplicate"
    else:
        return "high_duplicate"

def Get_best_alg(size_key, run_key, dup_key):
    size_algos = strategy_map[size_key]
    run_algos = strategy_map[run_key]
    dup_algos = strategy_map[dup_key]
    return list(set(size_algos) & set(run_algos) & set(dup_algos))

def execute_algorithm(name, arr):
    return strategy_to_algorithm[name](arr)

def vector_analytics(arr:list,feature_vectors: list, benchmark_csv: str):
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


        execute_algorithm(best_alg,arr)
        results.append({
            "N": N,
            "normalised_run": normalised_runs,
            "duplicate_ratio": duplicate_ratio,
            "candidates": candidates,
            "selected_algorithm": best_alg
        })

    return results
