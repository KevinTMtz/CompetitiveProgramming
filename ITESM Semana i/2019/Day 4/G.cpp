#include <iostream>
#include <math.h>
#include <string>
using namespace std;

int main() {
    int n, d;
    string str;
    cin >> n >> d >> str;
    
    int count = 0;
    for (int i=0; i<n-1;) {
        bool check = true;
        for (int k= (i+d<n)? i+d : n-1; k>i; k--){
            if (str[k]=='1') {
                count++;
                i = k;
                check = false;
            }
        }
        if (check) {
            cout << -1 << endl;
            return 0;
        }
    }
    cout << count << endl;
    return 0;
}
