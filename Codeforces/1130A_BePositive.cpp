#include <iostream>
#include <math.h>
using namespace std;
 
int main() {
    double n;
    cin >> n;
 
    int nums[(int) n];
    int positives=0, negatives=0, zero=0;
    for (int i=0; i<n; i++) {
        cin >> nums[i];
 
        if (nums[i] == 0) {
            zero++;
        } else if (nums[i]>0) {
            positives++;
        } else {
            negatives++;
        }
    }
    
    if (positives >= n/2) {
        cout << 1 << endl;
    } else if (negatives >= n/2) {
        cout << -1 << endl;
    } else {
        cout << 0 << endl;
    }
    
    return 0;
}