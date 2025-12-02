#include <cstdio>
#include <utility>
#include <vector>
#include <cstring> 

int MAX_ITERATE_COUNT = 10000000;
volatile bool G_FAIL_FLAG = false;
volatile long long ITERATION_COUNTER  = 0;

void custom_quicksort_recursive(int* arr, int low, int high);
int DualPivot_partition(int* arr, int low, int high);

void three_way_quicksort_recursive(int* arr, int low, int high);
void three_way_partition(int* arr, int low, int high, int& i, int& j);

void mergeSort_recursive(int* arr, int left, int right);
void merge_recursive(int* arr, int left, int mid, int right);

void heapify(int* arr, int n, int i); 



int DualPivot_partition(int* arr, int low, int high,int* lp) {


    if (ITERATION_COUNTER > MAX_ITERATE_COUNT){
        G_FAIL_FLAG = true;
    }
    ITERATION_COUNTER ++;
    if (arr[low] > arr[high]){
        ITERATION_COUNTER ++;
        std::swap(arr[low],arr[high]);
    }

    int j = low + 1;
    int g = high -1 ,k = low+1,p = arr[low] ,q = arr[high];
    while(k <= g){
        ITERATION_COUNTER ++;
        if (arr[k]<p){
            ITERATION_COUNTER ++;
            std::swap(arr[k],arr[j]);
            j++;
        }
        
        else if (arr[k >= q]){
            ITERATION_COUNTER +=2;
            while(arr[g] > q && k < g){
                g--;
            }
            ITERATION_COUNTER ++;
            std::swap(arr[k],arr[g]);
            g--;
            ITERATION_COUNTER ++;
            if (arr[k] < p){
                ITERATION_COUNTER ++;
                std::swap(arr[k],arr[j]);
                j++;
            }
        }
        k++;
    }
    j--;
    g++;
    ITERATION_COUNTER ++;
    std::swap(arr[low], arr[j]);
    ITERATION_COUNTER ++;
    std::swap(arr[high], arr[g]);
    *lp = j;
    return g;




}

void custom_quicksort_recursive(int* arr,int low ,int high) {

    if (low < high) { 

        int lp,rp;

        
        int rp = DualPivot_partition(arr,low,high,&lp);

        custom_quicksort_recursive(arr, low, lp - 1);
        custom_quicksort_recursive(arr, lp+1, rp - 1);
        custom_quicksort_recursive(arr, rp+1, high); 
    }
}




void three_way_partition(int* arr, int low, int high, int& i, int& j) {
    ITERATION_COUNTER ++;
    if  (ITERATION_COUNTER  > MAX_ITERATE_COUNT) {
         G_FAIL_FLAG = true; return; 
        }
    
    if (high - low <= 1) {

        if (arr[high] < arr[low])
            ITERATION_COUNTER++;
            ITERATION_COUNTER ++;
            std::swap(arr[high], arr[low]);
        }else{
            i = low;
            j = high;
            return;
        }

    int lt = low;     
    int gt = high;    
    int mid = low + 1;
    int pivot = arr[low]; 

    while (mid <= gt) {
        ITERATION_COUNTER ++;
        if  (ITERATION_COUNTER  > MAX_ITERATE_COUNT) {
            G_FAIL_FLAG = true; return; 
        };

        if (arr[mid] < pivot) {
            ITERATION_COUNTER++;
            std::swap(arr[lt], arr[mid]);
            lt++;
            mid++;
        
        }
        else if (arr[mid] > pivot) {
            ITERATION_COUNTER +=2;
            std::swap(arr[mid], arr[gt]);
            gt--;
        } else {
            ITERATION_COUNTER ++;
            mid++;
        }
    }
    
    i = lt - 1; 
    j = gt + 1;
}

void three_way_quicksort_recursive(int* arr, int low, int high) {

    if (low >= high) {
        return;
    }
    if  (G_FAIL_FLAG) {
            return; 
    };
    int i, j;
    three_way_partition(arr, low, high, i, j);

    three_way_quicksort_recursive(arr, low, i);
    three_way_quicksort_recursive(arr, j, high);
}




void mergeSort_recursive(int* arr, int left, int right){
    ITERATION_COUNTER ++;
    if (left >= right)
        return;

    if  (ITERATION_COUNTER  > MAX_ITERATE_COUNT) {
            G_FAIL_FLAG = true; return; 
    };

    int mid = left + (right - left) / 2;

    merge_recursive(arr, left, mid, right);
    mergeSort_recursive(arr, left, mid);
    mergeSort_recursive(arr, mid + 1, right);

}

void  merge_recursive(int* arr,int left,int mid,int right){
    int n1 = mid - left + 1;
    int n2 = right - mid;

    std::vector<int> L(n1), R(n2);
    if (G_FAIL_FLAG) return;

    for (int i = 0;i < n1;i++)

        L[i] = arr[left + i];


    for (int j= 0;j<n2;j++)

        R[j] = arr[mid + 1 + j];

    int i = 0, j = 0;
    int k = left;


    while (i < n1 && j < n2){
        ITERATION_COUNTER ++;
        if  (ITERATION_COUNTER  > MAX_ITERATE_COUNT) {
            G_FAIL_FLAG = true; return; 
        };

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
        if (G_FAIL_FLAG) return;
        arr[k] = L[i];
        i++;
        k++;

    }

    while (j < n2) {
        if (G_FAIL_FLAG) return;
        arr[k] = R[j];
        j++;
        k++;
    }
}




void heapify(int* arr, int n, int i){
    int largest = i;
    int l = 2 * i +1;
    int r = 2 * i + 2;

    if  (ITERATION_COUNTER  > MAX_ITERATE_COUNT) {
            G_FAIL_FLAG = true; return; 
        };

    if (l < n && arr[l] > arr[largest])
        largest = l;

    if  (ITERATION_COUNTER  > MAX_ITERATE_COUNT) {
            G_FAIL_FLAG = true; return; 
        };
    if (r < n && arr[r] > arr[largest])
        largest = r;
    if  (ITERATION_COUNTER > MAX_ITERATE_COUNT) {
            G_FAIL_FLAG = true; return; 
        };
    if (largest != i){
        std::swap(arr[i], arr[largest]);
        ITERATION_COUNTER++;
        heapify(arr, n, largest);
    }   
}



void shell_sort_impl(int* arr, int size) {

    if (G_FAIL_FLAG) return;

    for (int gap = size/2;gap > 0;gap /=2){
        for (int i = gap;i < size;i++){
            int temp = arr[i];
            int j = i;
            while (j >=gap && arr[j - gap] > temp){
                ITERATION_COUNTER++;
                if (ITERATION_COUNTER > MAX_ITERATE_COUNT) { 
                    G_FAIL_FLAG = true; 
                    return; 
                }
                
     
                ITERATION_COUNTER++;
                arr[j] = arr[j - gap];
                j-=gap;
            }
            arr[j] = temp;
        }
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

    if (G_FAIL_FLAG) return; 

    for(int i = 1; i < n; ++i) {
        int key = arr[i];
        int j = i - 1;
        
        while(j >= 0 && arr[j] > key){
            
     
            ITERATION_COUNTER++; 
            

            if (ITERATION_COUNTER  > MAX_ITERATE_COUNT) { 
                G_FAIL_FLAG = true; 
                return; 
            }
            
          
            ITERATION_COUNTER++; 
            

            arr[j + 1] = arr[j];
            j = j - 1;
        }
        

        arr[j + 1] = key;
    }
    printf("--- 2. Insertion Sort executed successfully ---\n");
    }

    void c_heapsort(int* arr, int n) {
        if (G_FAIL_FLAG) return;
        
        for (int i = n / 2-1;i>= 0;i--){

            heapify(arr,n,i);
        }
        for (int i = n -1; i> 0;i--){

            std::swap(arr[0], arr[i]);      
            heapify(arr, i, 0);
        }
        printf("--- 3. Heapsort executed successfully ---\n");
    }


    void c_three_way_quick_sort(int* arr, int size) {
        three_way_quicksort_recursive(arr, 0, size - 1);
        printf("--- 4. Three-Way Quicksort executed successfully ---\n");
    }


    void c_shell_sort(int* arr, int size) {
        shell_sort_impl(arr, size);
        printf("--- 5. Shell Sort executed successfully ---\n");
    }

    void c_merge_sort(int* arr, int size) {
        mergeSort_recursive(arr, 0, size - 1);
        printf("--- 6. Merge Sort executed successfully ---\n");
    }
}