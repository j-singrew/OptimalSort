import os.path
import ctypes
import numpy as np
import copy 
import time


clibrary = None




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
