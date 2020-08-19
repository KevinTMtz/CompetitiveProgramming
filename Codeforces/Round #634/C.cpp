//
//  C.cpp
//  CodeForces Round #634
//
//  Created by Kevin Torres Martínez on 19/08/20.
//  Copyright © 2020 Kevin Torres Martínez. All rights reserved.
//

#include <iostream>
#include <math.h>
#include <algorithm>
#include <vector>

using namespace std;
 
int main() {
    int t, n;
    cin >> t;

    for (int i=0; i<t; i++) {
        cin >> n;

        int arr[n];
        for (int k=0; k<n; k++)
            cin >> arr[k];
        
        if (n == 1) {
            cout << 0 << endl;
        } else {
            sort(arr, arr+n);
            int maxSame = 0;

            int lastCounted = 0, frequenciesIndex = -1;
            vector<int> frequencies;
            for (int k=0; k<n; k++) {
                if (lastCounted == arr[k]) {
                    frequencies[frequenciesIndex]++;
                } else {
                    frequenciesIndex++;
                    frequencies.push_back(1);
                    lastCounted = arr[k];
                }
                maxSame = max(maxSame, frequencies[frequenciesIndex]);
            }

            int unique = frequencies.size();
            if (maxSame == unique-1) {
                cout << maxSame << endl;
            } else {
                int min1 = min(maxSame, unique-1);
                int min2 = min(maxSame-1, unique);
                cout << max(min1, min2) << endl;
            }
        }
    }
}
