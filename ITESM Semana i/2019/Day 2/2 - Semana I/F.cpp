#include <bits/stdc++.h>
#include <iostream>
#include <math.h>
#include <string>
#include <vector>
using namespace std;

int main() {
    long long n;
    cin >> n;
    
    vector<int> choices;
    int temp;
    for (int i=0; i<n; i++) {
        cin >> temp;
        choices.push_back(abs(temp));
    }
    
    sort(choices.begin(), choices.end());
    
    long long count = 0;
    for (long long i=0; i<n; i++) {
        long long index = upper_bound(choices.begin(), choices.end(), 2*choices[i]) - choices.begin() -1;
        
        count += abs(i - index);
    }
    cout << count << endl;
    
    return 0;
}
