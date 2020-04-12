#include <iostream>
#include <string>
using namespace std;

int main() {
    int n;
    cin >> n;
    
    string str;
    getline(cin, str);
    getline(cin, str);
    
    if (n<=0) cout << "NO" << endl;
    
    for (int i=0; i<n-1; i++) {
        if (str[i]!=str[i+1]) {
            cout << "YES" << endl << str[i] << str[i+1] << endl;
            return 0;
        }
    }
    cout << "NO" << endl;
}
