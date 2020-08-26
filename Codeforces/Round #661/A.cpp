//
//  A.cpp
//  CodeForces Round #661
//
//  Created by Kevin Torres Martínez on 26/08/20.
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
        cin >> n;

        int arr[n];
        for (int k=0; k<n; k++)
            cin >> arr[k];
        sort(arr, arr+n);

        bool check = true;
        for(int k=0; k<n-1; k++) {
            if (arr[k+1]-arr[k] > 1) {
                cout << "NO" << endl;
                check = false;
                break;
            }
        }

        if (check)
            cout << "YES" << endl;
    }
}