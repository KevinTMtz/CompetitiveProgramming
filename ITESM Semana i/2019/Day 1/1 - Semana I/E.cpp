#include <iostream>
#include <math.h>
using namespace std;

int main() {
    long long n, x, y;
    cin >> n >> y >> x;

    long long distance1 = x-1 + y-1 - min(x-1, y-1);
    long long distance2 = n-x + n-y - min(n-x, n-y);
    
    if (distance1<=distance2) cout << "White" << endl;
    else cout << "Black" << endl;
    
    return 0;
}
