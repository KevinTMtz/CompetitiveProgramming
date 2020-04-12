#include <iostream>
#include <algorithm> 
using namespace std; 
  
long long int n, m, result, half;

void binarySearch (int treesHeight [], int left, int right);

int main() { 
    scanf("%i %i", &n, &m);
    
    int treesHeight [n];
    for(long long int i=0; i<n; i++) {
        scanf("%i", &treesHeight[i]);  
    }
    
    sort (treesHeight, treesHeight+n);
    
    long long int left=0, right=treesHeight[n-1];
    binarySearch(treesHeight, left, right);
    
    cout << result;
    
    return 0;
} 

void binarySearch(int treesHeight [], int left, int right) {
    half = (left+right) / 2;
    
    long long int cut = 0;
    bool temp = false;
    
    for (long long int i = n-1; i >= 0; i--) {
        if ((treesHeight[i]-half) >= 0) cut += (treesHeight[i] - half);
        
        else break;
    }

    if (cut >= m) {
        if (result < half) result = half;
        temp = true;        
    }
    
    if (left < right) {
        (temp)? left = half + 1: right = half;
        binarySearch(treesHeight, left, right);
    }
}