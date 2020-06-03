#include <iostream>
#include <math.h>
#include <string>
using namespace std;

int main() {
    int queries;
    cin >> queries;
    
    int digits, count;
    string str;
    for (int x=0; x<queries; x++) {
        count = 0;
        cin >> digits >> str;
        
        if (digits==2 && ((int)str[0] >= (int)str[1])) {
            cout << "NO" << endl;
        } else {
            cout << "YES" << endl << 2 << endl;
            cout << str[0] << " " << str.substr(1, digits) << endl;
        }
    }
    return 0;
}
