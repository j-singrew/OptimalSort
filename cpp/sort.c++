#include <cstdio>
#include <utility>
#include<vector>

void custom_quicksort_recursive(int* arr, int low, int high);
int hoare_partition(int* arr, int low, int high);
void three_way_partition(int* arr, int low, int high, int& i, int& j);

void three_way_quicksort_recursive(int* arr, int low, int high){
    if(low > high){
        return;
    }

    int i,j;

    three_way_partition(arr, low, high, i, j);
    three_way_quicksort_recursive(arr, low, i);  
    three_way_quicksort_recursive(arr, j, high);


}



int hoare_partition(int* arr, int low, int high) {

    int pivot = arr[low + (high - low) / 2]; 

    int i = low - 1; 
    int j = high + 1; 

    while (true) {

        do { i++; } while (arr[i] < pivot);


        do { j--; } while (arr[j] > pivot);


        if (i >= j) {

            return j; 
        }


        std::swap(arr[i], arr[j]); 
    }
}

void  three_way_partition(int* arr,int low,int high ,int& i,int& j){
    
    if(high - low <= 1){
        if (arr[high] < arr[low])
            std::swap(arr[high],arr[low]);
        i = low;
        j = high;
        return;
    }

    int mid = low;
    int pivot = arr[high];
    while (mid <= high){
        if (arr[mid] <  pivot){
            std::swap(arr[low], arr[mid]);
            low++;
            mid++;
        }
        else if (arr[mid] == pivot){
            mid++;
        }
        else if (arr[mid] > pivot){
            std::swap(arr[mid],arr[high--]);
        
        }
        i = low -1;
        j = mid;

    }

}

void custom_quicksort_recursive(int* arr, int low, int high) {

    if (low < high) { 
        

        int split_index = hoare_partition(arr, low, high);

        custom_quicksort_recursive(arr, low, split_index);
        
        custom_quicksort_recursive(arr, split_index + 1, high);
    }
}
void heapify(int* arr, int n, int i){

    int largest = i;

    int l = 2 * i +1;

    int r = 2 * i + 2;


    if (l < n && arr[l] > arr[largest])
        largest = l;

    if (r < n && arr[r] > arr[largest])
        largest = r;

    if (largest != i){
        std::swap(arr[i], arr[largest]);

        heapify(arr,n,largest);
    }   
}




extern "C" {
    

    void custom_quicksort_c(int* arr, int size) {

        if (size > 1) {
            custom_quicksort_recursive(arr, 0, size - 1);
        }
        printf("--- 1. Quick Sort (Standard) executed successfully ---\n"); 
    }
    
    void c_insertion_sort(int* arr, int n) {

        
        for(int i = 1;i< n;++i){
            int key = arr[i];
            int j = i -1;

            while(j >= 0 && arr[j] > key){
                arr[j+1] = arr[j];
                j = j - 1;
            }
            arr[j + 1] = key;
        }
        printf("--- 2. Insertion Sort executed successfully ---\n");
    }


    void c_heapsort(int* arr, int n) {

        for (int i = n / 2-1;i>= 0;i--)
            heapify(arr,n,i);

        for (int i = n -1; i> 0;i--){

            std::swap(arr[0], arr[i]);
            heapify(arr, i, 0);
        }


        printf("--- 3. Heapsort is active (Ready for logic) ---\n");
    }


    void c_three_way_quicksort(int* arr, int size) {
        int high  = size-1;
        int low = 0;

        int i,j;
        three_way_quicksort_recursive(arr, low,high);

    }


    void c_shell_sort(int* arr, int size) {
        printf("--- 5. Shell Sort is active (Ready for logic) ---\n");
    }


    void c_merge_sort(int* arr, int size) {

        printf("--- 6. Merge Sort is active (Ready for logic) ---\n");
    }
}
