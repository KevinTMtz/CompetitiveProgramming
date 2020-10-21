//
//  C.cpp
//  CodeForces Round #677
//
//  Created by Kevin Torres Martínez on 21/10/20.
//  Copyright © 2020 Kevin Torres Martínez. All rights reserved.
//

#include <iostream>
#include <math.h>
#include <algorithm>

using namespace std;

int main() {
    int t, n;
    cin >> t;
    
    for (int i=0; i<t; i++) {
        int ans = 0;

        cin >> n;        
        int piranhasArr [n];

        for (int k=0; k<n; k++) {
            cin >> piranhasArr[k];
        }

        // TODO: Make the algorithm
        // http://codeforces.com/contest/1433/problem/C

        cout << ans << endl;
    }
}