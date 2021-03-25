//
//  Guess the Number
//  March Cook-Off 2021 Division 3
//
//  Created by Kevin Torres Martínez on 24/3/21.
//  Copyright © 2021 Kevin Torres Martínez. All rights reserved.
//
//  Round: https://www.codechef.com/COOK127C
//  Problem: https://www.codechef.com/COOK127C/problems/GUESSIT
//

#include <iostream>
#include <string>

using namespace std;

int main()
{
  int t;
  cin >> t;

  for (int k = 0; k < t; k++)
  {
    for (int i = 1; i <= 2000; i++)
    {
      cout << (i * i) << endl;

      int check;
      cin >> check;
      if (check == 1)
        break;
    }
  }

  return 0;
}
