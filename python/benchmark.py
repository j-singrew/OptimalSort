from dataset import DataGeneration
from analytics.run_metric import run_variation_counter
import numpy  as np

import os.path
import ctypes
import copy
import time
import csv
from typing import List, Dict, Any

dataset = DataGeneration()
run_metrics = run_variation_counter(dataset)
clibrary = None
final_results = []
Time_Threshold = 1000
NUM_RUNS = 5


try:
 
        clibrary = ctypes.CDLL('custom_sort.so')

except OSError:

        try:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            library_path = os.path.join(current_dir, 'custom_sort.so')
            
       
            clibrary = ctypes.CDLL(library_path)
            
        except Exception as inner_e:
         
            clibrary = None
            print(f"[WARNING] Secondary load attempt failed: {type(inner_e).__name__}.")
        if clibrary is not None:
            
            try:
                print("Sucess conecting c++")
    


                clibrary.custom_quicksort_c.argtypes = [
                    ctypes.POINTER(ctypes.c_int), 
                    ctypes.c_int,
                ]
                clibrary.custom_quicksort_c.restype = None  

                clibrary.c_insertion_sort.argtypes = [
                    ctypes.POINTER(ctypes.c_int), 
                    ctypes.c_int,
                ]
                clibrary.c_insertion_sort.restype = None  

                clibrary.c_heapsort.argtypes = [
                    ctypes.POINTER(ctypes.c_int), 
                    ctypes.c_int,
                ]
                clibrary.c_heapsort.restype = None  

                clibrary.c_three_way_quicksort.argtypes = [
                    ctypes.POINTER(ctypes.c_int), 
                    ctypes.c_int,
                ]
                clibrary.c_three_way_quicksort.restype = None  

                clibrary.c_shell_sort.argtypes = [
                    ctypes.POINTER(ctypes.c_int), 
                    ctypes.c_int,
                ]
                clibrary.c_shell_sort.restype = None  

                clibrary.c_merge_sort.argtypes = [
                    ctypes.POINTER(ctypes.c_int), 
                    ctypes.c_int,
                ]
                clibrary.c_merge_sort.restype = None  

                SWAP = ctypes.c_longlong.in_dll(clibrary ,"SWAP").value
                COMPARASON = ctypes.c_longlong.in_dll(clibrary ,"COMPARASON").value






            except Exception as e:
                print(f"\n[WARNING] C++ Library FFI failed to establish connection.")
                clibrary = None


def permanente_storage(run_data: List[Dict[str, Any]]):

    if not run_data:
        print("Error: No data records found to save.")
        return
    file_name = 'ds.csv'
    fieldnames = list(run_data[0].keys())




    file_exists = os.path.isfile(file_name)
   

    try:

        with open(file_name,'a',newline='',encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            writer.writerows(run_data)

    except Exception as e:
        print(f"\n[ERROR] Failed to save benchmark data to CSV: {e}")

def run_c_quicksort_wrapper(arr:np.ndarray):

    if clibrary  is None:
        raise RuntimeError("C++ library not loaded. Cannot run C++ quicksort.")     
    arr_c_compatible = np.ascontiguousarray(arr, dtype=np.intc)
    c_arr_pointer = arr_c_compatible.ctypes.data_as(ctypes.POINTER(ctypes.c_int))
    clibrary.custom_quicksort_c(c_arr_pointer, arr_c_compatible.size)

    
def run_c_insertion_sort(arr:np.ndarray):

    if clibrary is None:
        raise RuntimeError("C++ library not loaded. Cannot run C++ insertion sort.")   
    
    arr_c_compatible = np.ascontiguousarray(arr, dtype=np.intc)
    c_arr_pointer = arr_c_compatible.ctypes.data_as(ctypes.POINTER(ctypes.c_int))
    clibrary.c_insertion_sort(c_arr_pointer, arr_c_compatible.size)

def run_c_heap_sort(arr:np.ndarray):

    if clibrary is None:
        raise RuntimeError("C++ library not loaded. Cannot run C++ heap sort.")   
    arr_c_compatible = np.ascontiguousarray(arr, dtype=np.intc)
    c_arr_pointer = arr_c_compatible.ctypes.data_as(ctypes.POINTER(ctypes.c_int))
    clibrary.c_heapsort(c_arr_pointer, arr_c_compatible.size)

def run_c_three_way_quick_sort(arr:np.ndarray):

    if clibrary is None:
        raise RuntimeError("C++ library not loaded. Cannot run C++ 3 way quicksort.")   

    arr_c_compatible = np.ascontiguousarray(arr, dtype=np.intc)
    c_arr_pointer = arr_c_compatible.ctypes.data_as(ctypes.POINTER(ctypes.c_int))
    clibrary.c_three_way_quicksort(c_arr_pointer, arr_c_compatible.size)

def run_c_shell_sort(arr:np.ndarray):
    if clibrary is None:
        raise RuntimeError("C++ library not loaded. Cannot run C++ 3 shell sort.")   

    arr_c_compatible = np.ascontiguousarray(arr, dtype=np.intc)
    c_arr_pointer = arr_c_compatible.ctypes.data_as(ctypes.POINTER(ctypes.c_int))
    clibrary.c_shell_sort(c_arr_pointer, arr_c_compatible.size)

def run_c_merge_sort(arr:np.ndarray):
    if clibrary is None:
        raise RuntimeError("C++ library not loaded. Cannot run C++ merge sort.")   
        
    arr_c_compatible = np.ascontiguousarray(arr, dtype=np.intc)
    c_arr_pointer = arr_c_compatible.ctypes.data_as(ctypes.POINTER(ctypes.c_int))
    clibrary.c_merge_sort(c_arr_pointer, arr_c_compatible.size)

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

    times_list = []
    swaps_list = []
    comparisons_list = []

    for _ in range(num_runs):

        data_copy = copy.deepcopy(data_arr)
        start_time = time.perf_counter()

        sort_func(data_copy)

        end_time = time.perf_counter()

        SWAP = ctypes.c_longlong.in_dll(clibrary ,"SWAP").value
        COMPARASON = ctypes.c_longlong.in_dll(clibrary ,"COMPARASON").value

        times_list.append(end_time - start_time)
        swaps_list.append(SWAP)
        comparisons_list.append(COMPARASON)  

    avg_time = min(times_list)
    avg_swaps = sum(swaps_list) / num_runs
    avg_comparisons = sum(comparisons_list) / num_runs

    return { 'time': avg_time, 'swaps': avg_swaps, 'comps': avg_comparisons }




def Benchmarking_Orchestration():

    test_targets = prepare_benchmark_targets()

    algorithms_to_run = [

        ("Python Timsort", lambda arr: arr.tolist().sort()),
        ("NumPy Sort", lambda arr: np.sort(arr))
    ]



    for algo_name ,algo_typ in  algorithms_to_run:

        for target in test_targets:

            data_to_pass = target['data']

            alg_time = run_iteration_metrics(data_arr=data_to_pass,sort_func=algo_typ,num_runs= NUM_RUNS )

            final_record = {
                "algorithm_name": algo_name,
                "data_pattern": target['name'].split('_')[0],
                "size_category": target['name'].split('_')[-1],
                "N": target['N'],
                "avg_time_ms":  alg_time['time'],
                "num_runs": NUM_RUNS,
                "comparisons": 0, 
                "swaps": 0      
            }
            final_results.append(final_record)
            permanente_storage(final_results)
            print(f"  {target['name']:<30} | Time: {alg_time['time']:.4f} ms")

    return final_results

def Benchmark_Cpp_Sort():
    print("This is run metrics ",run_metrics)
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

    test_targets = prepare_benchmark_targets()

    for target in test_targets:
        for algs,algo_typ in cpp_algorithms_to_run:
            if (algs =="C++ Insertion Sort" or algs =="C++ three way shell Sort")   and target['N'] > 100000:
                alg_time = 99999.0 
            else:          
    
                alg_metrics = run_iteration_metrics(
                data_arr=target["data"],
                sort_func=algo_typ,
                num_runs=NUM_RUNS,          
                )

            #if alg_metrics['alg_time'] >= Time_Threshold:
                #final_time = 99999.0
            #else:
                #final_time = alg_metrics['alg_time']


            #runs_per_size.append((runs,normalised_run_metric,duplicate_ratio ))
            #run_data[key] = (runs_per_size,data_length)
            #run_metrics
            #'random_order': ([(15, 0.75, 0.0), (66550, 0.6655, 0.00482), (666318, 0.666318, 0.048225)], 1000000)
            key = (target['name'].split('r_')[0])+"r"
            print("ok this is other key",key)

            final_record = {
                "algorithm_name":  algs,
                "data_pattern": target['name'].split('_')[0],
                "size_category": target['name'].split('_')[-1],
                "N": target['N'],
                "avg_time_ms":  alg_metrics['time'],
                "num_runs": NUM_RUNS,
                "comparisons":  alg_metrics['comps'], 
                "swaps":  alg_metrics['swaps'],
                "normalised_run":run_metrics[key][1],
                "duplite_ratio":run_metrics[key][-1]                
            }
            final_results.append(final_record)
            permanente_storage(final_results)
            print(f"  {target['name']:<30} | C++ Time: {alg_metrics['time']:.4f} ms")

if __name__ == "__main__":
    Benchmarking_Orchestration()
    Benchmark_Cpp_Sort()
