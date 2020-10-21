//
//  E.cpp
//  CodeForces Round #677
//
//  Created by Kevin Torres Martínez on 21/10/20.
//  Copyright © 2020 Kevin Torres Martínez. All rights reserved.
//

#include <iostream>
#include <math.h>

using namespace std;

unsigned  long  long fact(int n) {
    if (n == 0 || n == 1)
        return 1;
    else
        return n * fact(n - 1);
}

int main() {
    int n;
    cin >> n;
    
    unsigned  long  long ans = fact(n) / (pow((n/2), 2) * 2);
    cout << ans << endl;
}