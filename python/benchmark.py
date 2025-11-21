from dataset import DataGeneration
import numpy  as np
import timeit

dataset = DataGeneration()

def benchmark_dataset_generation():
    size_name = ["small","medium","large"]

    benchmarks_to_run = []

    for pattern_name ,arr_size in dataset.items():

        for i ,arr in enumerate(arr_size):
            current_size_name = size_name[i]

            arr_benchmark = {
                "name": f"{pattern_name}_{current_size_name}",
                "N": len(arr),
                "data": arr    
            }
            benchmarks_to_run .append(arr_benchmark)

    print("--- 18 Test Targets Prepared ---")

    for target in benchmarks_to_run:

        print(f"Target: {target['name']:<25} (N={target['N']:,})")

    return benchmarks_to_run

def  run_iteration_metrics(data_arr,sort_func):
    # 1. Initialize times list
    timeit_setup_code = "import copy; data_copy = copy.deepcopy(data)"
    run_times = []

    d_array = data_arr.copy

    run_bechmark = "sort_function(d_array)"
    times = timeit.repeat(
        run_bechmark , 
        setup=timeit_setup_code,
        globals={'sort_func': sort_func, 'data': data_arr}, 
        repeat=5,  
        number=1   
    )
    run_times.append(min(times))
    return min(times)

def Benchmarking_Orchestration():

    all_data_s = benchmark_dataset_generation()
    test_targets = run_iteration_metrics(all_data_s)

    algorithms_to_run = [
        ("Python Timsort", lambda arr: arr.tolist().sort()),
        ("NumPy Sort", lambda arr: np.sort(arr))
    ]

    final_results = []
    for algo_name ,algo_typ in  algorithms_to_run:

        for targets in test_targets:




