//
//  B.cpp
//  CodeForces Round #702
//
//  Created by Kevin Torres Martínez on 17/2/21.
//  Copyright © 2021 Kevin Torres Martínez. All rights reserved.
//
//  Round: https://codeforces.com/contest/1490
//  Problem: https://codeforces.com/contest/1490/problem/B
//

#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int t;
    cin >> t;

    for (int i = 0; i < t; i++)
    {
        int n;
        cin >> n;

        int arrNums[n];
        for (int k = 0; k < n; k++)
            cin >> arrNums[k];

        int count[3];
        for (int k = 0; k < 3; k++)
            count[k] = 0;

        for (int k = 0; k < 3; k++)
            for (int j = 0; j < n; j++)
                if (arrNums[j] % 3 == k)
                    count[k]++;

        int res = 0;
        while (*min_element(count, count + 3) != n / 3)
            for (int k = 0; k < 3; k++)
                if (count[k] > n / 3)
                {
                    res++;
                    count[k]--;
                    count[(k + 1) % 3]++;
                }

        cout << res << endl;
    }
}