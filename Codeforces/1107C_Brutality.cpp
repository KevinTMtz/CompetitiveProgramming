#include <bits/stdc++.h>
#include <iostream>
#include <math.h>
#include <string>
#include <vector>
using namespace std;
 
int main() {
    long long n, k;
    cin >> n >> k;
    
    int* damage = new int[n];
    for (int i=0; i<n; i++) cin >> damage[i];
    
    string keysToPress;
    cin >> keysToPress;
    
    long long result = 0;
    int index = 0;
    for (int i = 1; i <= n; i++) {
        if ((i == n) || (keysToPress[i] != keysToPress[i-1])) {
            if (i - index > k) sort(damage + index, damage + i);
            
            for (int j = 0; (j < k) && ((i-j-1) >= index); j++)
                result += damage[i - j - 1];
            
            index = i;
        }
    }
    cout << result << endl;
    return 0;
}