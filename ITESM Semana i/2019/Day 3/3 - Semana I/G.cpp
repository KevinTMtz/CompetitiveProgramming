#include <iostream>
#include <string>
using namespace std;

int main() {
    int n;
    cin >> n;
    
    string str;
    getline(cin, str);
    getline(cin, str);
    
    int count = 0, max = 0;
    for (int i=0; i<n; i++) {
        if (str[i]==32) {
            if (count > max) max = count;
            count = 0;
        }
        if (str[i]>=65 && str[i]<='Z')
            count++;
    }
    if (count > max) max = count;
    cout << max << endl;
}
