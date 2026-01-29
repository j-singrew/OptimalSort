import pandas as pd

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
    size_algos = array_algorithm_map[size_key]
    run_algos = array_algorithm_map[run_key]
    dup_algos = array_algorithm_map[dup_key]
    return list(set(size_algos) & set(run_algos) & set(dup_algos))

def vector_analytics(feature_vectors: list, benchmark_csv: str):
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

        results.append({
            "N": N,
            "normalised_run": normalised_runs,
            "duplicate_ratio": duplicate_ratio,
            "candidates": candidates,
            "selected_algorithm": best_alg
        })

    return results
