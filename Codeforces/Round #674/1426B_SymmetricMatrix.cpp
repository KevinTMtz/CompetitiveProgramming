//
//  B.cpp
//  CodeForces Round #674
//
//  Created by Kevin Torres Martínez on 28/10/20.
//  Copyright © 2020 Kevin Torres Martínez. All rights reserved.
//

#include <iostream>

using namespace std;

int main()
{
    int t;
    cin >> t;

    for (int i = 0; i < t; i++) {
        int n, m;
        cin >> n >> m;

        int arrOfTiles[n*4];
        for (int k = 0; k < n*4; k++)
            cin >> arrOfTiles[k];

        string ans = "";
        if (m % 2 != 0) {
            ans = "NO";
        } else {
            bool check = false;
            for (int k = 0; k < n*4-3; k += 4)
                if (arrOfTiles[k+1] == arrOfTiles[k+2]) {
                    check = true;
                    break;
                }

            ans = check ? "YES" : "NO";
        }

        cout << ans << endl;
    }
}