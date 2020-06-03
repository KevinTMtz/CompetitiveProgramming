#include <iostream>
#include <math.h>
using namespace std;
 
int main() {
    int b, k;
    cin >> b >> k;
 
    int nums[k];
    for (int i=0; i<k; i++)
        cin >> nums[i];    
    
    int evens = 0, odds = 0;
    for (int i=0, x=k-1; i<k; i++, x--) {
        if (nums[i]%2 == 0) evens++;
        else odds++;
    }
 
    if (b%2 == 0) {
        if (nums[k-1]%2 == 0) {
            cout << "even" << endl;
        } else { 
            cout << "odd" << endl;
        }
    } else {
        if (odds%2==0) {
            cout << "even" << endl;
        } else {
            cout << "odd" << endl;
        }
    }
    return 0;
}