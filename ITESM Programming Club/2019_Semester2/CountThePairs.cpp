#include <iostream>
#include <new>
#include <algorithm>

using namespace std;

int main() {
    int n, k, count=0;
    int* num;
    cin>>n>>k;

    int arr[n];

    for (int i=0;i<n;i++) {
        cin>>arr[i];
    }

    sort (arr, arr+n);

    for (int i=0;i<n-k;i++) {
        num = lower_bound(arr,arr+n,arr[i]+k);
        if (*num == arr[i]+k) {
            count++;
        }
    }

    /*
    for (int i=0;i<n;i++) {
        for (int j=0;j<n;j++) {
            if ((arr[i]+k-arr[i+1+j])==0) {
                count++;
            }
        }
    }
    */

    cout<<count<<endl;
}