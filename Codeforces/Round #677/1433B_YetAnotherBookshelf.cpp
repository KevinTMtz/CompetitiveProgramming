//
//  B.cpp
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
        
        int bookShelfArr [n];

        for (int k=0; k<n; k++) {
            cin >> bookShelfArr[k];
        }

        int tempCount = 0;
        int oneIndex = -1;
        for (int k=0; k<n; k++) {
            if (oneIndex == -1 && bookShelfArr[k] == 1) {
                oneIndex = k;
                tempCount = 0;
            } else if (bookShelfArr[k] == 1) {
                ans += tempCount;
                tempCount = 0;
                oneIndex = k;
            } else {
                tempCount ++;
            }
        }

        cout << ans << endl;
    }
}