#include <bits/stdc++.h>
#include <iostream>
#include <math.h>
#include <string>
#include <algorithm>
using namespace std;

bool checkIfGood(string num);

int main() {
    int x, y;
    cin >> x >> y;
    
    for (int i=x; i<=y; i++) {
        if (checkIfGood(to_string(i))) {
            cout << i << endl;
            return 0;
        }
    }
    cout << -1 << endl;
}

bool checkIfGood(string num) {
    for (int i=0; i<num.size(); i++)
        if (count(num.begin(), num.end(), num[i]) > 1) return false;
    return true;
}
