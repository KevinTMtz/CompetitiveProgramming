#include <iostream>
#include <math.h>
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;

    // Pages needed
    int n1 = 2*n;
    int n2 = 5*n;
    int n3 = 8*n;
    
    int r1 = (2*n)%k;
    int r2 = (5*n)%k;
    int r3 = (8*n)%k;
    
    int sum1 = (n1-r1)/k + ((r1==0)? 0: 1);
    int sum2 = (n2-r2)/k + ((r2==0)? 0: 1);
    int sum3 = (n3-r3)/k + ((r3==0)? 0: 1);
    
    cout << sum1+sum2+sum3 << endl;

    return 0;
}
