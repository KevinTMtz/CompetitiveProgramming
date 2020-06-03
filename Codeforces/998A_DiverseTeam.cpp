#include <iostream>
#include <math.h>
using namespace std;
 
int main() {
    int n, k;
    cin >> n >> k;
 
    int* nums = new int[n];
    for (int i=0; i<n; i++)
        cin >> nums[i];
    
    int* arr = new int[k];
    int* indexes = new int[k];
    for (int i=0; i<k; i++) {
        arr[k] = 0;
        indexes[k] = 0;
    }
    
    int index=0;
    for (int i=0; i<n; i++) {
        if (index==k) break;
        bool check = true;
        
        for (int x=0; x<k; x++)
            if (nums[i]==indexes[x]) check = false;
        
        if (check) {
            indexes[index] = nums[i];
            arr[index] = i+1;
            index++;
        }
    }
    
    if (index==k) {
        cout << "YES" << endl;
        for (int i=0; i<k; i++)
            cout << arr[i] << " ";
        cout << endl;
    } else cout << "NO";
    return 0;
}