//
//  A.cpp
//  CodeForces Round #708
//
//  Created by Kevin Torres Martínez on 17/3/21.
//  Copyright © 2021 Kevin Torres Martínez. All rights reserved.
//
//  Round: https://codeforces.com/contest/1497
//  Problem: https://codeforces.com/contest/1497/problem/A
//

#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

int main()
{
  int t;
  cin >> t;

  for (int k = 0; k < t; k++)
  {
    int n;
    cin >> n;

    vector<int> nonRepeated;
    vector<int> repeated;
    set<int> numsSet;
    for (int i = 0; i < n; i++)
    {
      int temp;
      cin >> temp;

      if (numsSet.find(temp) != numsSet.end())
        repeated.push_back(temp);
      else
        nonRepeated.push_back(temp);

      numsSet.insert(temp);
    }

    sort(nonRepeated.begin(), nonRepeated.end());

    for (int i = 0; i < nonRepeated.size(); i++)
      cout << nonRepeated[i] << " ";
    for (int i = 0; i < repeated.size(); i++)
      cout << repeated[i] << " ";
    cout << endl;
  }

  return 0;
}
