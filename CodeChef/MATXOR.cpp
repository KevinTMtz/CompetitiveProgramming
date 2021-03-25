//
//  Matrix XOR
//  March Cook-Off 2021 Division 3
//
//  Created by Kevin Torres Martínez on 24/3/21.
//  Copyright © 2021 Kevin Torres Martínez. All rights reserved.
//
//  Round: https://www.codechef.com/COOK127C
//  Problem: https://www.codechef.com/COOK127C/problems/MATXOR
//

#include <iostream>

using namespace std;

int main()
{
  int t;
  cin >> t;

  for (int a = 0; a < t; a++)
  {
    int n, m, k;
    cin >> n >> m >> k;

    int arrDiff[n + m + 5];
    for (int i = 0; i < n + m + 5; i++)
    {
      arrDiff[i] = 0;
    }

    for (int i = 1; i <= n; i++)
    {
      arrDiff[i + 1]++;
      arrDiff[i + m + 1]--;
    }

    int ans = 0;
    for (int i = 2; i <= n + m; i++)
    {
      arrDiff[i] += arrDiff[i - 1];

      if (arrDiff[i] % 2 != 0)
        ans ^= (k + i);
    }

    cout << ans << endl;
  }

  return 0;
}
