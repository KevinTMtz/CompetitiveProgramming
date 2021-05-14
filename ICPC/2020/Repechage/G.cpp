//
//  G.cpp
//  2020-2021 ICPC - Gran Premio de Mexico  - Repechaje
//
//  Created by Kevin Torres Martínez on 14/5/21.
//  Copyright © 2021 Kevin Torres Martínez. All rights reserved.
//
//  Round: https://codeforces.com/gym/102966
//  Problem: https://codeforces.com/gym/102966/problem/G
//

#include <iostream>
#include <numeric>

using namespace std;

int main()
{
  long long L, G;
  cin >> L >> G;

  long long time = 0;
  for (int i = 0; i < G; i++)
  {
    long long p, d;
    cin >> p >> d;

    if (d == 1)
    {
      time = max(time, L - p);
    }
    else
    {
      time = max(time, p);
    }
  }
  cout << time << endl;

  return 0;
}
