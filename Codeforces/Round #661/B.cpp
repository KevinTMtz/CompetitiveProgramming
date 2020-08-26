//
//  B.cpp
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
        
        int minCandy = 1000000001; 
        int minOrange = 1000000001;
        
        int candy[n];
        for (int k=0; k<n; k++) {
            cin >> candy[k];

            if (candy[k] < minCandy)
                minCandy = candy[k];
        }

        int orange[n];
        for (int k=0; k<n; k++) {
            cin >> orange[k];

            if (orange[k] < minOrange)
                minOrange = orange[k];
        }
        
        long long movements = 0;
        
        for (int k=0; k<n; k++) {
            int difference = 0;
            if (candy[k] > minCandy && orange[k] > minOrange) {
                difference = min(candy[k] - minCandy, orange[k] - minOrange);
                candy[k] -= difference;
                orange[k] -= difference;
                movements += difference;
            }
            
            if (candy[k] > minCandy) {
                difference = candy[k] - minCandy;
                candy[k] -= difference;
                movements += difference;
            }

            if (orange[k] > minOrange) {
                difference = orange[k] - minOrange;
                orange[k] -= difference;
                movements += difference;
            }
        }
        
        cout << movements << endl;  
    }
}