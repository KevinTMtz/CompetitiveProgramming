#include <iostream>
#include <math.h>
using namespace std;

int main() {
    int x, y, z, a, b, c;
    cin >> x >> y >> z >> a >> b >> c;
    
    bool check = false;
    if (x <= a) {
        int num1 =  a - x + b;
        if (y <= num1) {
            int num2 = num1 - y + c;
            if (z <= num2) {
                check = true;
            }
        }
    }
    
    string result = (check)? "YES": "NO";
    cout << result << endl;

    return 0;
}
