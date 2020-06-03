#include <iostream>
#include <math.h>
using namespace std;
 
int main() {
    int n, k;
    cin >> n >> k;
 
    int nums[n];
    for (int i=0; i<n; i++)
        cin >> nums[i];
 
    int count = 0;
    bool stop = false;
    for (int i=0; i<n; i++) {
        if (nums[i]<=k) count++;
        else { stop = true; break; }
    }
 
    if (stop) {
        for (int i=n-1; n>=0; i--) {
            if (nums[i]<=k) {
                count++;
            } else {
                break;
            }
        }
    }
 
    cout << count << endl;
    
    return 0;
}