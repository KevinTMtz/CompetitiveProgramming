//
//  C.cpp
//  CodeForces Educationarl Round #33
//
//  Created by Kevin Torres Martínez on 7/4/21.
//  Copyright © 2021 Kevin Torres Martínez. All rights reserved.
//
//  Round: https://codeforces.com/contest/893
//  Problem: https://codeforces.com/problemset/problem/893/C
//

#include <iostream>
#include <vector>

using namespace std;

vector<long long> friendsArr[100000];

long long dfs(long long current, long long *goldPrice, bool *visited, long long n)
{
  long long goldToPay, friendNode;
  visited[current] = true;
  goldToPay = goldPrice[current];
  for (long long i = 0; i < friendsArr[current].size(); i++)
  {
    friendNode = friendsArr[current][i];
    if (!visited[friendNode])
    {
      goldToPay = min(goldToPay, dfs(friendNode, goldPrice, visited, n));
    }
  }
  return goldToPay;
}

int main()
{
  long long n, nPairs;
  cin >> n >> nPairs;

  long long goldPrice[n];
  bool visited[n];
  for (long long i = 0; i < n; i++)
  {
    cin >> goldPrice[i];
    visited[i] = false;
  }

  for (long long i = 0; i < nPairs; i++)
  {
    long long n1, n2;
    cin >> n1 >> n2;

    friendsArr[n1 - 1].push_back(n2 - 1);
    friendsArr[n2 - 1].push_back(n1 - 1);
  }

  long long ans = 0;
  for (long long i = 0; i < n; i++)
    if (!visited[i])
      ans += dfs(i, goldPrice, visited, n);

  cout << ans << endl;

  return 0;
}
