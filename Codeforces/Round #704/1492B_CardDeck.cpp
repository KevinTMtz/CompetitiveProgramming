//
//  B.cpp
//  CodeForces Round #704
//
//  Created by Kevin Torres Martínez on 24/2/21.
//  Copyright © 2021 Kevin Torres Martínez. All rights reserved.
//
//  Round: https://codeforces.com/contest/1492
//  Problem: https://codeforces.com/contest/1492/problem/B
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

    int numsArr[n], numsPositions[n];
    for (int k = 0; k < n; k++)
    {
      cin >> numsArr[k];
      numsPositions[numsArr[k] - 1] = k;
    }

    int num = n - 1, last = n;
    while (num >= 0)
    {
      int numPosition = numsPositions[num];

      if (numPosition >= last)
      {
        num--;
        continue;
      }

      for (int k = numPosition; k < last; k++)
        cout << numsArr[k] << " ";

      last = numPosition;
    }
    cout << "\n";
  }

  return 0;
}
