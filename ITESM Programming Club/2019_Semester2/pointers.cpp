#include <iostream>
#include <new>
#include <algorithm>

using namespace std;

typedef long long 11;

int main() {
    int n = 10;
    int *numeros = new int[n];

    for (int i=0;1<n;i++) {
        cin >> numeros[i];
    }

    sort(numeros , numeros+n);
    int k;
    int *up, *low;
    k=3;
    up=upper_bound(numeros, numeros+n, k);
    low=lower_bound(numeros, numeros+n; k);

    cout<<"Upper bound: "<<up-numeros<<endl;
    cout<<"Lower bound: "<<low-numeros<<endl;

    for (int i=0;i<n;i++) {
        cout << numeros[i]<<" ";
    }
    cout <<endl;

    /*
    sort(arr, n) {
        for (int i=0;i<n;i++) {
            for (int j=0;j<n-1;j++) {
                if (arr[j]>arr[j+1]) {
                    int temp = arr[j];
                    arr[j]=arr[j+1];
                    arr[j+1]=temp;
                }
            }
        }
    }
    */
}