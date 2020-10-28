//
//  A.cpp
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

    for (int i = 0; i < t; i++)
    {
        int numOfApartment, x;
        cin >> numOfApartment >> x;

        int ans = 0;
        if (numOfApartment <= 2) {
            ans = 1;
        } else {
            ans = ((numOfApartment-3)/x) + 2;
        }

        cout << ans << endl;
    }
}