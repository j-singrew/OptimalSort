#include <cstdio>


extern "C" {
void swap(int* arr,int i,int j){
    int holder_variable = arr[i];

    arr[i] = arr[j];
    arr[j] = holder_variable;
}
void  custom_quicksort_partition( int* arr, int size){

    if (size <=1 ){
        printf("Sorted")
    }
    int arr_middle = arr[size/2];
    int arr_low= arr[0];
    int arr_high = arr[size-1];
    int pivot = (arr_middle + arr_high  + arr_low)/3;

    while(true){

        do {
            arr_low++;
        }while(arr[arr_low] < pivot);
    }

    do {
        arr_high++;
    }while(arr[arr_high] > pivot);

    if (arr_low > arr_high){
        break;
    };

    swap(arr,arr_low,arr_high);



}
void  custom_quicksort( int* arr, int size){
    custom_quicksort_partition(arr,size);

    for (int i = 0;i < arr[size]; i ++){
        printf(arr[i]);
    }
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


