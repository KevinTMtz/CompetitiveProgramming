#include <bits/stdc++.h>
#include <iostream>
#include <math.h>
#include <string>
using namespace std;
 
int main() {
    int n;
    cin >> n;
    
    int* nums = new int[n];
    int zeros = 0, negatives = 0, positives = 0;
    long long result = 0;
    for (int i=0; i<n; i++) {
        cin >> nums[i];
        
        if (nums[i]==0)
            zeros++;
        if (nums[i]>0)
            result += nums[i]-1;
        if (nums[i]<0) {
            result += abs(nums[i]+1);
            negatives++;
        }
    }
    if (zeros > 0) result += zeros;
    else if (negatives%2 == 1) result += 2;
    
    cout << result << endl;
}