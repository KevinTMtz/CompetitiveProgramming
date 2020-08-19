//
//  A.cpp
//  CodeForces Round #634
//
//  Created by Kevin Torres Martínez on 19/08/20.
//  Copyright © 2020 Kevin Torres Martínez. All rights reserved.
//

#include <iostream>
#include <math.h>

using namespace std;
 
int main() {
    int t, n;
    cin >> t;
    
    for (int i=0; i<t; i++) {
        cin >> n;
        cout << int (floor((n-1)/2)) << endl;
    }
}
