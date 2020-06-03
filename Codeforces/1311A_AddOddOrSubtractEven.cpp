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
    
    int n1=0, n2=0, ans=0;
    for(int i=0; i<num; i++) {
        cin >> n1 >> n2;
        
        if (n1==n2) {
            ans = 0;
        } else if (n1-n2 < 0) {
            if ((n1-n2)%2==0) {
                ans = 2;
            } else {
                ans = 1;
            }
        } else if (n1-n2 > 0) {
            if (n1-n2==1) {
                ans = 2;
            } else if ((n1-n2)%2==0) {
                ans = 1;
            } else {
                ans = 2;
            }
        }
        
        cout << ans << endl;
    }
    
    return 0;
}
