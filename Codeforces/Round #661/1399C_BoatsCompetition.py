#
#  C.py
#  CodeForces Round #661
#
#  Created by Kevin Torres Martínez on 09/09/20.
#  Copyright © 2020 Kevin Torres Martínez. All rights reserved.
#

t = int(input())
for i in range(0, t):
    n =  int(input())
    weightArr = list(map(int, input().split()))
    weightArr.sort()

    frequencies = {}
    for k in range(0, n):
        if weightArr[k] in frequencies:
            frequencies[weightArr[k]] += 1
        else:
            frequencies[weightArr[k]] = 1

    maxNum = 0
    for k in range(1, 2*n):
        total = 0

        for key in frequencies:
            tempNum = k - key
            if (tempNum >= 1 and tempNum in frequencies):
                total += min(frequencies[key], frequencies[tempNum])

        total = int(total / 2)
        maxNum = max(maxNum, total)
    
    print(maxNum)
