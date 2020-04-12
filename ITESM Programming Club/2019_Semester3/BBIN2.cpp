#include <stdio.h>
#include <bits/stdc++.h>
using namespace std;

long long int binarySearch(int arr[], int l, int r, int x);

int main(void){
    int arrL, queries;
    scanf("%i %i", &arrL, &queries);
    
    int arr[arrL];
    for (int i=0; i<arrL; i++) scanf("%i", &arr[i]);
    
    int toSearch, num;
    for (int i=0; i<queries; i++) {
        scanf("%i", &toSearch);
        num = upper_bound(arr, arr+arrL, toSearch) - arr;

        printf("%i %s", (arr[num-1] == toSearch)? num-1 : -1, "\n");
    }
}
