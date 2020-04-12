#include <iostream>
#include <math.h>
#include <string>
using namespace std;

int main() {
    int n, v;
    cin >> n >> v;
    
    int result = (n-1 >= v)? v: n-1;
    int liters = result-1;
    for (int i=2; i<=n; i++) {
        if (n-i > liters) {
            result += i;
            liters++;
        }
        liters--;
    }
    cout << result << endl;
    return 0;
}
