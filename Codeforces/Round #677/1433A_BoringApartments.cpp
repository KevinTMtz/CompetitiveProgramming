//
//  A.cpp
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
    int t, n, ans;
    cin >> t;
    
    for (int i=0; i<t; i++) {
        cin >> n;

        int start = 10;
        int tempSum = 1;
        
        ans = ((n % start) - 1) * 10;
        
        while (n > 0) {
            ans += tempSum;
            tempSum += 1;

            n = n - (n % start);

            start *= 10;
        }

        cout << ans << endl;
    }
}