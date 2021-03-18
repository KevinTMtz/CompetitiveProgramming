//
//  A.cpp
//  CodeForces Round #706
//
//  Created by Kevin Torres Martínez on 17/3/21.
//  Copyright © 2021 Kevin Torres Martínez. All rights reserved.
//
//  Round: https://codeforces.com/contest/1496
//  Problem: https://codeforces.com/contest/1496/problem/A
//

#include <iostream>
#include <string>

using namespace std;

int main()
{
  int t;
  cin >> t;

  for (int j = 0; j < t; j++)
  {
    int n, k;
    string str;
    cin >> n >> k >> str;

    bool ans = true;
    if (n < 2 * k + 1)
    {
      ans = false;
    }
    else
    {
      for (int i = 0; i < k; i++)
        if (str[i] != str[n - 1 - i])
        {
          ans = false;
          break;
        }
    }

    cout << (ans ? "YES" : "NO") << endl;
  }

  return 0;
}
