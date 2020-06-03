#include <iostream>
#include <math.h>
using namespace std;

int main() {
    int queries;
    cin >> queries;

    for (int i=0; i<queries; i++) {
        long long x, y;
        cin >> x >> y;
        
        if (x == y + 1)
            cout << "NO" << endl;
        else
            cout << "YES" << endl;
    }

    return 0;
}
