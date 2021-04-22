//
//  C.cpp
//  2020-2021 ICPC - Gran Premio de Mexico  - Repechaje
//
//  Created by Kevin Torres Martínez on 21/4/21.
//  Copyright © 2021 Kevin Torres Martínez. All rights reserved.
//
//  Round: https://codeforces.com/gym/102966
//  Problem: https://codeforces.com/gym/102966/problem/C
//

#include <iostream>
#include <iomanip>

using namespace std;

double **getMatrix(double **a, double **b, int n)
{
  double **newMat = new double *[256];
  for (int i = 0; i < 256; ++i)
    newMat[i] = new double[256];

  for (int i = 1; i <= n; i++)
    for (int j = 1; j <= n; j++)
      for (int k = 1; k <= n; k++)
        newMat[i][j] += a[i][k] * b[k][j];

  return newMat;
}

int main()
{
  int n, m;
  cin >> n >> m;

  double **m1 = new double *[256];
  double **m1Copy = new double *[256];
  double **ans = new double *[256];

  for (int i = 1; i <= n; i++)
  {
    m1[i] = new double[256];
    m1Copy[i] = new double[256];
    ans[i] = new double[256];

    ans[i][i] = 1;

    for (int j = 1; j <= n; j++)
    {
      cin >> m1[i][j];
      m1Copy[i][j] = m1[i][j];
    }
  }

  int temp = m - 1;
  while (temp > 0)
  {
    if (temp & 1)
      ans = getMatrix(ans, m1, n);

    m1 = getMatrix(m1, m1, n);
    temp >>= 1;
  }

  for (int i = 1; i <= n; i++)
  {
    double temp = 0;
    for (int j = 1; j <= n; j++)
      temp += ans[1][j] * m1Copy[j][i];

    cout << setprecision(4) << temp << endl;
  }

  return 0;
}