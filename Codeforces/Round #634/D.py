#
#  D.cpp
#  CodeForces Round #634
#
#  Created by Kevin Torres Martínez on 2/09/20.
#  Copyright © 2020 Kevin Torres Martínez. All rights reserved.
#

t = int(input())

for i in range(0, t):
    for k in range(0, 9):
        str = input()
        newStr = str.replace('1', '2')
        print(newStr)
