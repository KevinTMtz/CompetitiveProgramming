#include <iostream>
#include <math.h>
#include <string>
using namespace std;
 
int main() {
    int n;
    cin >> n;
    
    int* num = new int[n];
    for (int i=0; i<n; i++) cin >> num[i];
 
    if (n == 1) { cout << "YES" << endl; return 0; }
 
    bool increase = false, constant = false, decrease = false;
    if (num[0]<num[1]) increase = true;
    if (num[0]==num[1]) constant = true;
    if (num[0]>num[1]) decrease = true;
 
    bool check = true;
    for (int i=0; i<n-1; i++) {
        if (increase == true && num[i]==num[i+1]) {
            increase = false;
            constant = true;
            continue;
        } else if (increase == true && num[i]>num[i+1]) {
            increase = false;
            decrease = true;
            continue;
        }
        
        if (constant == true && num[i]>num[i+1]) {
            constant = false;
            decrease = true;
            continue;
        } else if (constant == true && num[i]<num[i+1]) {
            check = false;
            break;
        }
        
        if (decrease == true && num[i]<=num[i+1]) {
            check = false;
            break;
        }
    }
    
    if (check) cout << "YES" << endl;
    else cout << "NO" << endl;
 
    return 0;
}
