#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int n = 0;
    cin >> n;
    
    int numsArr [n];
    int expected [n];

    for (int i=0; i<n; i++) {
        cin >> numsArr[i];
        expected[i] = numsArr[i];
    }

    sort(expected, expected+n);
    
    int ans=n;
    for (int i=0, j=0; i<n; i++) {
        if (numsArr[i] == expected[j]) {
            j++;
            ans--;
        }
    }
    
    cout << ans << endl;
}
