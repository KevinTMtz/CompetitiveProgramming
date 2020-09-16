//
//  C.cpp
//  CodeForces Round #661
//
//  Created by Kevin Torres Martínez on 09/09/20.
//  Copyright © 2020 Kevin Torres Martínez. All rights reserved.
//

#include <iostream>
#include <math.h>
#include <algorithm>
#include <map>

using namespace std;
 
int main() {
    int t, n;
    cin >> t;

    for (int k; k<t; k++) {
        cin >> n;
        int weightArr[n];
        
        map<int,int> frequencies;
        for (int i=0; i<n; i++) {
            int temp;
            cin >> temp;
            frequencies[temp]++;
        }

        int maxNum=0;
        for(int i=1; i<=(2*n); i++){
            int total = 0;
            for(auto keyAndValue : frequencies){
                int other = i - keyAndValue.first;
                if(other >= 1 && frequencies.count(other))
                    total += min(keyAndValue.second, frequencies[other]);
            }
            total /= 2;
            maxNum = max(maxNum,total);
        }
        cout << maxNum << endl;
    }
}