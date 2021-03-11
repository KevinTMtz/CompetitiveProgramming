//
//  K.cpp
//  2020-2021 ICPC - Gran Premio de Mexico  - Repechaje
//
//  Created by Kevin Torres Martínez on 10/3/21.
//  Copyright © 2021 Kevin Torres Martínez. All rights reserved.
//
//  Round: https://codeforces.com/gym/102966
//  Problem: https://codeforces.com/gym/102966/problem/K
//

#include <iostream>
#include <numeric>

using namespace std;

int main()
{
  int n1, n2;
  cin >> n1 >> n2;

  int nums1[n1], nums2[n2];
  for (int i = 0; i < n1; i++)
    cin >> nums1[i];
  for (int i = 0; i < n2; i++)
    cin >> nums2[i];

  cout << (accumulate(nums2, nums2 + n2, 0) - accumulate(nums1, nums1 + n1, 0)) << endl;
}