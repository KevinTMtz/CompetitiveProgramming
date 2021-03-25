//
//  Pawri Meme
//  March Cook-Off 2021 Division 3
//
//  Created by Kevin Torres Martínez on 24/3/21.
//  Copyright © 2021 Kevin Torres Martínez. All rights reserved.
//
//  Round: https://www.codechef.com/COOK127C
//  Problem: https://www.codechef.com/COOK127C/problems/PAWRI
//

#include <iostream>
#include <string>

using namespace std;

int main()
{
  int t;
  cin >> t;
  cin.ignore(256, '\n');

  for (int k = 0; k < t; k++)
  {
    string str;
    getline(cin, str);

    int pos = 0;
    while (pos < str.length())
    {
      pos = str.find("party", pos);

      if (pos != string::npos)
      {
        str.replace(str.begin() + pos + 2, str.begin() + pos + 5, "wri");
        pos += 1;
      }
    }

    cout << str << endl;
  }

  return 0;
}
