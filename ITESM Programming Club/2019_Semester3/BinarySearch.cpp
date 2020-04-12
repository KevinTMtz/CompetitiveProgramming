#include <iostream>
#include <stdio.h>
using namespace std;

long long int binarySearch(int arr[], int l, int r, int x);

int main(void){
    int arrL, queries;
    scanf("%i %i", &arrL, &queries);
    
    int arr[arrL];
    for (int i=0; i<arrL; i++) scanf("%i", &arr[i]);
    
    int toSearch;
    for (int i=0; i<queries; i++) {
        scanf("%i", &toSearch);
        cout << toSearch << " ";
        cout << binarySearch(arr, 0, arrL, toSearch) << endl;
    }
}

long long int binarySearch(int arr[], int l, int r, int x) {
    if (l>r) return -1;
    
    long long int m = (l+r)/2;
    if (arr[m] == x) {
        return m;
    } else if (arr[m] < x) {
        return binarySearch(arr, m+1, r, x);
    } else {
        return binarySearch(arr, l, m-1, x);
    }
}
