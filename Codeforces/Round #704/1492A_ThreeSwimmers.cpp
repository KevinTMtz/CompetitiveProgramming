//
//  A.cpp
//  CodeForces Round #704
//
//  Created by Kevin Torres Martínez on 24/2/21.
//  Copyright © 2021 Kevin Torres Martínez. All rights reserved.
//
//  Round: https://codeforces.com/contest/1492
//  Problem: https://codeforces.com/contest/1492/problem/A
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
    long long p, a, b, c;
    cin >> p >> a >> b >> c;

    if (p % a == 0 || p % b == 0 || p % c == 0)
      cout << 0;
    else
      cout << (long long) min({a - p % a, b - p % b, c - p % c});
    cout << endl;
  }
}