#include <cstdio>

extern "C" {
void  custom_quicksort( int* arr, int size){
    printf("Quicksort connection established\n");
    printf("Got array with size%d\n",size);
}
}

extern "C"{
    void insertion_sort(int* arr,int size){
            printf("Insertion Sort is active\n");
    }
}

extern "C"{
    void heap_sort(int* arr,int size){
            printf("Heap Sort is active\n");
    }
}
extern "C"{
    void three_way_quick_sort(int* arr,int size){
            printf("3-WAY Quick sort is active\n");
    }
}

extern "C"{
    void shell_sort(int* arr,int size){
            printf("shell sort is active\n");
    }
}

extern "C"{
    void merge_sort(int* arr,int size){
            printf("merge sort is active\n");
    }
}


