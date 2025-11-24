from dataset import DataGeneration
import numpy  as np
import timeit
import ctypes

dataset = DataGeneration()
clibrary = None

def setup_ctype_quicksort():
    global clibrary
    try:
        clibrary = ctypes.CDLL("/Users/joshuasingrew/Desktop/GitHub/New Folder With Items/my_new_africon_app/OptimalSort/cpp/custom_sort.so")
        print("Sucess conecting c++")


        clibrary.custom_quicksort.argtypes = [
        np.ctypeslib.ndpointer(
            dtype=np.intc,
            flags='WRITEABLE',
            
        ),
        ctypes.c_int,
        ]
        clibrary.custom_quicksort.restype = None  

        clibrary.insertion_sort.argtypes = [
        np.ctypeslib.ndpointer(
            dtype=np.intc,
            flags='WRITEABLE',
            
        ),
        ctypes.c_int,
        ]
        clibrary.insertion_sort.restype = None  

        clibrary.heap_sort.argtypes = [
        np.ctypeslib.ndpointer(
            dtype=np.intc,
            flags='WRITEABLE',
            
        ),
        ctypes.c_int,
        ]
        clibrary.heap_sort.restype = None  

        clibrary.three_way_quick_sort.argtypes = [
        np.ctypeslib.ndpointer(
            dtype=np.intc,
            flags='WRITEABLE',
            
        ),
        ctypes.c_int,
        ]
        clibrary.three_way_quick_sort.restype = None  

        clibrary.shell_sort.argtypes = [
        np.ctypeslib.ndpointer(
            dtype=np.intc,
            flags='WRITEABLE',
            
        ),
        ctypes.c_int,
        ]
        clibrary.shell_sort.restype = None  

        clibrary.merge_sort.argtypes = [
        np.ctypeslib.ndpointer(
            dtype=np.intc,
            flags='WRITEABLE',
            
        ),
        ctypes.c_int,
        ]
        clibrary.merge_sort.restype = None  

    except Exception as e:
        print(f"\n[WARNING] C++ Library FFI failed to establish connection.")
        clibrary = None

def run_c_quicksort_wrapper(arr:np.ndarray):

    if clibrary  is None:
        raise RuntimeError("C++ library not loaded. Cannot run C++ quicksort.")   

    clibrary.custom_quicksort(arr)

def run_c_insertion_sort(arr:np.ndarray):

    if clibrary is None:
        raise RuntimeError("C++ library not loaded. Cannot run C++ insertion sort.")   

    clibrary.insertion_sort(arr)

def run_c_heap_sort(arr:np.ndarray):

    if clibrary is None:
        raise RuntimeError("C++ library not loaded. Cannot run C++ heap sort.")   

    clibrary.heap_sort(arr)

def run_c_three_way_quick_sort(arr:np.ndarray):

    if clibrary is None:
        raise RuntimeError("C++ library not loaded. Cannot run C++ 3 way quicksort.")   

    clibrary.three_way_quick_sort(arr)

def run_c_shell_sort(arr:np.ndarray):
    if clibrary is None:
        raise RuntimeError("C++ library not loaded. Cannot run C++ 3 shell sort.")   

    clibrary.shell_sort(arr)

def run_c_merge_sort(arr:np.ndarray):
    if clibrary is None:
        raise RuntimeError("C++ library not loaded. Cannot run C++ merge sort.")   
        
    clibrary.merge_sort(arr)

def prepare_benchmark_targets():
    size_name = ["small","medium","large"]

    benchmarks_to_run = []

    for pattern_name ,arr_size in dataset.items():

        for i ,arr in enumerate(arr_size):
            current_size_name = size_name[i]
            arr_benchmark = {
                "name": f"{pattern_name}_{current_size_name}",
                "N": len(arr),
                "data": arr.copy()
            }

            benchmarks_to_run.append(arr_benchmark)
      

    print("--- 18 Test Targets Prepared ---")

    for target in benchmarks_to_run:

        print(f"Target: {target['name']:<25} (N={target['N']:,})")

    return benchmarks_to_run

def  run_iteration_metrics(data_arr,sort_func,num_runs):

    timeit_setup_code = "import numpy as np; data = base_data.copy()" 
    stmt = "sort_func(data)"

    times =timeit.repeat(
        stmt,
        setup=timeit_setup_code,
        globals={"sort_func": sort_func, "base_data": data_arr},
        repeat=num_runs,
        number=1,
    )
    return min(times) * 1000






def Benchmarking_Orchestration():
    NUM_RUNS = 5

    test_targets = prepare_benchmark_targets()

    algorithms_to_run = [

        ("Python Timsort", lambda arr: arr.tolist().sort()),
        ("NumPy Sort", lambda arr: np.sort(arr))
    ]

    final_results = []

    for algo_name ,algo_typ in  algorithms_to_run:

        for target in test_targets:

            data_to_pass = target['data']

            alg_time = run_iteration_metrics(data_arr=data_to_pass,sort_func=algo_typ,num_runs= NUM_RUNS )

            final_record = {
                "algorithm_name": algo_name,
                "data_pattern": target['name'].split('_')[0],
                "size_category": target['name'].split('_')[-1],
                "N": target['N'],
                "avg_time_ms":  alg_time,
                "num_runs": NUM_RUNS,
                "comparisons": 0, 
                "swaps": 0      
            }
            final_results.append(final_record)
            
            print(f"  {target['name']:<30} | Time: {alg_time:.4f} ms")

            final_record["avg_time_ms"] = alg_time
    return final_results

def Benchmark_Cpp_Sort():
    cpp_algorithms_to_run = [
    ("C++ Quick Sort", run_c_quicksort_wrapper),
    ("C++ Insertion Sort", run_c_insertion_sort),
    ("C++ heap Sort", run_c_heap_sort),
    ("C++ three way quicksort Sort",run_c_three_way_quick_sort),
    ("C++ three way shell Sort",run_c_shell_sort),
    ("C++ three way merge Sort",run_c_merge_sort),
]
    if clibrary is None:
        print("C++ library not loaded. Skipping C++ benchmarks.")
        return
    Num_RUNS = 5
    test_targets = prepare_benchmark_targets()

    print("\n--- Running C++ Quicksort ---")
    for target in test_targets:
        for algs,algo_typ in cpp_algorithms_to_run:
            base_data = target["data"]
            alg_time = run_iteration_metrics(
                data_arr=base_data,
                sort_func=algo_typ,
                num_runs=Num_RUNS,          
            )
        print(f"  {target['name']:<30} | C++ Time: {alg_time:.4f} ms")


if __name__ == "__main__":
    setup_ctype_quicksort()
    Benchmarking_Orchestration()
    Benchmark_Cpp_Sort()
