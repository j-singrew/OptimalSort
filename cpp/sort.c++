#include <iostream>
using namespace std;
#include <cstdio>

extern "C" {

void  custom_quicksort_c( int* arr, int size){
    printf("Quicksort connection established\n");
    printf("Got array with size%d\n",size);

}
}