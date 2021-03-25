//
//  Weight Balance
//  March Cook-Off 2021 Division 3
//
//  Created by Kevin Torres Martínez on 24/3/21.
//  Copyright © 2021 Kevin Torres Martínez. All rights reserved.
//
//  Round: https://www.codechef.com/COOK127C
//  Problem: https://www.codechef.com/COOK127C/problems/WEIGHTBL
//

#include <iostream>

using namespace std;

int main()
{
  int t;
  cin >> t;

  for (int k = 0; k < t; k++)
  {
    int w1, w2, x1, x2, M;
    cin >> w1 >> w2 >> x1 >> x2 >> M;

    int ans = 0,
        minIncrease = M * x1,
        maxIncrease = M * x2,
        difference = w2 - w1;

    cout << ((difference >= minIncrease && difference <= maxIncrease) ? 1 : 0) << endl;
  }

  return 0;
}
