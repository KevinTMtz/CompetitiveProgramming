#include<iostream>
#include<algorithm>

using namespace std;

int main() {
    int n, m, k, tape = 0;
    
    int* arr = new int[1000000];
    int* diferences = new int[1000000];
    
    cin>> n >> m >> k;
    
    for(int i=0; i<n; i++)
        cin >> arr[i];
    
    for(int i=0; i<n; i++)
        diferences[i] = arr[i+1] - arr[i];
    
    tape = arr[n-1] - arr[0] + 1;
    
    sort(diferences, diferences+n);
    for(int i=n-1; i>n-k; i--)
        tape = tape - diferences[i] + 1;
    
    cout << tape << endl;
    return 0;
}
