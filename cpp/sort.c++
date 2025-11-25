#include <cstdio>


extern "C" {
void swap(int* arr,int i,int j){
    int holder_variable = arr[i];

    arr[i] = arr[j];
    arr[j] = holder_variable;
}
int custom_quicksort_partition( int* arr, int low ,int high){


    int arr_low= low - 1;
    int arr_high = high +1;
    int pivot = arr[arr_low];

    while(true){

        do {
            arr_low++;
        }while(arr[arr_low] < pivot);
    }

    do {
        arr_high--;
    }while(arr[arr_high] > pivot);

    if (arr_low >=arr_high){
        return arr_high;
    };

    swap(arr,arr_low,arr_high);



}
void  custom_quicksort( int* arr, int size){

    custom_quicksort_partition(arr,size);
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


