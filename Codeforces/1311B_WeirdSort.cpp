//
//  main.cpp
//  CodeForces Round #624
//
//  Created by Kevin Torres Martínez on 26/02/20.
//  Copyright © 2020 Kevin Torres Martínez. All rights reserved.
//
 
#include <iostream>
using namespace std;
 
int main(int argc, const char * argv[]) {
    int num=0;
    cin >> num;
    
    int arrLength=0, posLength=0;
    string ans;
    for(int i=0; i<num; i++) {
        ans = "NO";
        cin >> arrLength >> posLength;
        
        int nums[arrLength];
        for (int j=0; j<arrLength; j++)
            cin >> nums[j];
 
        int pos[posLength];
        for (int j=0; j<posLength; j++) {
            cin >> pos[j];
            pos[j] -= 1;
        }
        
        bool check = false;
        int temp = 0;
        
        do {
            check = false;
           for (int j=0; j<posLength; j++) {
               if (nums[pos[j]]>nums[pos[j]+1]) {
                   temp = nums[pos[j]];
                   nums[pos[j]] = nums[pos[j]+1];
                   nums[pos[j]+1] = temp;
                   check = true;
               }
           }
        }
        while (check);
        
        bool ansCheck = true;
        for (int j=0; j<arrLength-1; j++) {
            if (nums[j]>nums[j+1]) {
                ansCheck = false;
            }
        }
        
        if (ansCheck)
            ans = "YES";
        
        cout << ans << endl;
    }
    
    return 0;
}