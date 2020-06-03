#include <iostream>
#include <math.h>
#include <string>
using namespace std;

int main() {
    int n;
    cin >> n;
    
    int* nums = new int[n];
    for (int i=0; i<n; i++) cin >> nums[i];
    
    int max = 0;
    int count = 1;
    for (int i=1; i<n; i++) {
        if (nums[i] >= nums[i-1]) {
            count++;
        } else {
            if (count > max) max = count;
            count = 1;
        }
    }
    if (count > max) max = count;

    cout << max << endl;
    
    return 0;
}
