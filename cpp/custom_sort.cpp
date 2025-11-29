#include <cstdio>
#include <utility>
#include <vector>
#include <cstring> 


void merge_recursive(int* arr, int left, int mid, int right);
void mergeSort_recursive(int* arr, int left, int right);

void custom_quicksort_recursive(int* arr, int low, int high);
int hoare_partition(int* arr, int low, int high);

void three_way_partition(int* arr, int low, int high, int& i, int& j);
void three_way_quicksort_recursive(int* arr, int low, int high);
void heapify(int* arr, int n, int i);

// --- THE MISSING 3-WAY RECURSIVE DEFINITION ---

void three_way_quicksort_recursive(int* arr, int low, int high) {

    if (low >= high) {
        return;
    }
    
    int i, j; 
    three_way_partition(arr, low, high, i, j); 
    three_way_quicksort_recursive(arr, low, i);
    three_way_quicksort_recursive(arr, j, high);
}

void mergeSort_recursive(int* arr, int left, int right){
    
    if (left >= right)
        return;

    int mid = left + (right - left) / 2;
    mergeSort_recursive(arr, left, mid);
    mergeSort_recursive(arr, mid + 1, right);

    merge_recursive(arr, left, mid, right);
}


void  merge_recursive(int* arr,int left,int mid,int right){
    int n1 = mid - left + 1;
    int n2 = right - mid;

    std::vector<int> L(n1), R(n2);
    for (int i = 0;i < n1;i++)
        L[i] = arr[left + i];
    for (int j= 0;j<n2;j++)
        R[j] = arr[mid + 1 + j];

    int i = 0, j = 0;
    int k = left;

    while (i < n1 && j < n2){
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        }
        else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }
    
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }


    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}
int Lomuto_partition(int* arr, int low, int high) {

    int pivot = arr[high]; 


    int i = low - 1; 


    for (int j = low; j <= high - 1; j++) {
        if (arr[j] <= pivot) {
            i++; 
            std::swap(arr[i], arr[j]);
        }
    }

    std::swap(arr[i + 1], arr[high]);
    
  
    return (i + 1);

}

void  three_way_partition(int* arr,int low,int high ,int& i,int& j){
    
 
    if (high - low <= 1) {
        if (arr[high] < arr[low])
            std::swap(arr[high], arr[low]);
        i = low;
        j = high;
        return;
    }

    int lt = low;     
    int gt = high;    
    int mid = low + 1;
    int pivot = arr[low]; 

    while (mid <= gt) {
        if (arr[mid] < pivot) {
            std::swap(arr[lt], arr[mid]);
            lt++;
            mid++;
        } else if (arr[mid] > pivot) {
            std::swap(arr[mid], arr[gt]);
            gt--;
        } else {
            mid++;
        }
    }
    

    i = lt - 1; 
    j = gt + 1;

}

void custom_quicksort_recursive(int* arr,int low ,int high) {

    if (low < high) { 
        
        int split_index = Lomuto_partition(arr,low,high);

        custom_quicksort_recursive(arr, low, split_index - 1);
        
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
   
        custom_quicksort_recursive(arr, 0, size - 1);
        printf("--- 4. Three-Way Quicksort executed successfully ---\n");
    }


    void c_shell_sort(int* arr, int size) {
        
        for (int gap = size/2;gap > 0;gap /=2){
            
            for (int i = gap;i < size;i++){
                int temp = arr[i];
                int j = i;

                while (j >=gap && arr[j - gap] > temp){
                    arr[j] = arr[j - gap];
                    j-=gap;
                }
                arr[j] = temp;

            }
        }
        printf("--- 5. Shell Sort executed successfully ---\n");
    }


    void c_merge_sort(int* arr, int size) {

        mergeSort_recursive(arr, 0, size - 1);
        printf("--- 6. Merge Sort executed successfully ---\n");
    }
}