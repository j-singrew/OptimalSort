#include <iostream>
using namespace std;
#include <cstdio>
/*
Insertion Sort

Heapsort

Quick Sort (Standard 2-Way)

3-Way Quick Sort

Shell Sort

Merge Sort
*/


extern "C" {

void  custom_quicksort_c( int* arr, int size){
    printf("Quicksort connection established\n");
    printf("Got array with size%d\n",size);

}
}

extern "C"{
    void Insertion_Sort(int* arr,int size){
            printf("Insertion Sort is active\n");
    }
}

extern "C"{
    void HeapSort(int* arr,int size){
            printf("Heap Sort is active\n");
    }
}

extern "C"{
    void three_way_Quick_Sort(int* arr,int size){
            printf("3-WAY Quick sort is active\n");
    }
}

extern "C"{
    void Shell_Sort(int* arr,int size){
            printf("shell sort is active\n");
    }
}

extern "C"{
    void Merge_Sort(int* arr,int size){
            printf("merge sort is active\n");
    }
}


