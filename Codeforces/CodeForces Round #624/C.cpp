//
//  main.cpp
//  CodeForces Round #624
//
//  Created by Kevin Torres Martínez on 11/03/20.
//  Copyright © 2020 Kevin Torres Martínez. All rights reserved.
//

#include <iostream>
#include <algorithm>
using namespace std;

int main(int argc, const char * argv[]) {
    int num = 0;
    cin >> num;
    
    int strLength = 0, mistakes = 0;
    int ans[26];
    
    string combo = "";
    for (int l=0; l<num; l++) {
        for (int i=0; i<26; i++)
            ans[i] = 0;
        
        cin >> strLength >> mistakes >> combo;
        int mistakePos[mistakes];
        
        for (int i=0; i<mistakes; i++)
            cin >> mistakePos[i];
        
        sort(mistakePos, mistakePos+mistakes);
        
        /*
        1 a
        3 abc
        Final: abca
        */
        
        for (int i=0; i<mistakes; i++) {
            for (int j=0; j<mistakePos[]; j++) {
                
            }
        }
        
        /*
        for (int i=0; i<strLength; i++) {
            ans[combo[i]-97] += 1;
            
            
            
            for (int j=0; j<mistakes; j++) {
                if (mistakePos[j]-1 >= i) {
                    ans[combo[i]-97] += 1;
                }
            }
        }
        */
        
        for (int i=0; i<26; i++)
            cout << ans[i] << " ";
        cout << endl;
    }
    return 0;
}
