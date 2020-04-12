#include <iostream>
#include <math.h>
#include <string>
using namespace std;

int main() {
    int n;
    cin >> n;
    int billsArr[5] = {100,20,10,5,1};
    
    int bills = 0;
    for (int i=0; i<5; i++) {
        bills += n/billsArr[i];
        n = n%billsArr[i];
    }

    cout << bills << endl;
    
    return 0;
}
