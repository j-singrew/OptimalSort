from dataset import DataGeneration
import numpy  as np
import timeit

dataset = DataGeneration()

def prepare_benchmark_targets():
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
            benchmarks_to_run.append(arr_benchmark)

    print("--- 18 Test Targets Prepared ---")

    for target in benchmarks_to_run:

        print(f"Target: {target['name']:<25} (N={target['N']:,})")

    return benchmarks_to_run

def  run_iteration_metrics(data_arr,sort_func,num_runs):
    # 1. Initialize times list
    timeit_setup_code = "import copy; data_copy = copy.deepcopy(data)"
    run_times = []



    run_bechmark = "sort_function(data_copy)"
    times = timeit.repeat(
        run_bechmark , 
        setup=timeit_setup_code,
        globals={'sort_func': sort_func, 'data': data_arr}, 
        repeat=num_runs,  
        number=1   
    )
    run_times.append(min(times))
    return min(times)

def Benchmarking_Orchestration():
    NUM_RUNS = 5
    all_data_s = prepare_benchmark_targets()
    test_targets = run_iteration_metrics(all_data_s)

    algorithms_to_run = [

        ("Python Timsort", lambda arr: arr.tolist().sort()),
        ("NumPy Sort", lambda arr: np.sort(arr))
    ]

    final_results = []
    for algo_name ,algo_typ in  algorithms_to_run:

        for target in test_targets:

            data_to_pass = target['data']

            alg_time = run_iteration_metrics(data=data_to_pass,data_name=target['name'],N= NUM_RUNS )

            final_record = {
                "algorithm_name": algo_name,
                "data_pattern": target['name'].split('_')[0],
                "size_category": target['name'].split('_')[-1],
                "N": target['N'],
                "avg_time_ms":  alg_time['avg_time_ms'],
                "num_runs": NUM_RUNS,
                "comparisons": 0, 
                "swaps": 0      
            }
            final_results.append(final_record)
            
            print(f"  {target['name']:<30} | Time: {final_results['avg_time_ms']:.4f} ms")




if __name__ == "__main__":
    Benchmarking_Orchestration()





