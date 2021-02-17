//
//  A.cpp
//  CodeForces Round #702
//
//  Created by Kevin Torres Martínez on 17/2/21.
//  Copyright © 2020 Kevin Torres Martínez. All rights reserved.
//
//  Round: https://codeforces.com/contest/1490
//  Problem: https://codeforces.com/contest/1490/problem/A
//

#include <iostream>

using namespace std;

int main()
{
    int t;
    cin >> t;

    for (int i = 0; i < t; i++)
    {
        int n;
        cin >> n;

        int numArr[n]; 
        for (int i = 0; i < n; i++) {
          cin >> numArr[i];
        }

        int count = 0;
        for (int i = 0; i < n-1; i++) {
          if (numArr[i+1] > numArr[i] * 2) {
            int temp = numArr[i];
            while(temp * 2 < numArr[i+1]) {
              temp *= 2;
              count++;
            }
          } else if (numArr[i] > numArr[i+1] * 2) {
            int temp = numArr[i+1];
            while(temp * 2 < numArr[i]) {
              temp *= 2;
              count++;
            }
          }
        }

        cout << count << endl;
    }
}