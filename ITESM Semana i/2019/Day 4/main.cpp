#include <bits/stdc++.h>
#include <iostream>
#include <math.h>
#include <vector>
using namespace std;

//bool checkIfGood(long long num);

int main() {
    long long n;
    cin >> n;
    
    vector<long long> vect;
    for (int i=1; (i*(i+1))/2 <= n; i++)
        vect.push_back((i*(i+1))/2);
    
    for (int i=0; i<vect.size(); i++) {
        if (binary_search(vect.begin(), vect.end(), n-vect[i])) {
            cout << "YES" << endl;
            return 0;
        }
    }
    cout << "NO" << endl;
}

/*
bool checkIfGood(long long num) {
    if (floor((sqrt(8*num+1) - 1) / 2) == ceil((sqrt(8*num+1) - 1) / 2))
        return true;
    return false;
}
*/
