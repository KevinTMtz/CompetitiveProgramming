#include <iostream>
#include <math.h>
using namespace std;

int main() {
    string s, t;
    cin >> s >> t;
    
    bool check = true;
    if (s.size()==t.size()) {
        for (int i=0; i<s.size(); i++) {
            if ( ((s[i]=='a'||s[i]=='e'||s[i]=='i'||s[i]=='o'||s[i]=='u') &&
                  !(t[i]=='a'||t[i]=='e'||t[i]=='i'||t[i]=='o'||t[i]=='u')) ||
                 (!(s[i]=='a'||s[i]=='e'||s[i]=='i'||s[i]=='o'||s[i]=='u') &&
                   (t[i]=='a'||t[i]=='e'||t[i]=='i'||t[i]=='o'||t[i]=='u')) ) {
                check = false;
            }
        }
    } else {
        check = false;
    }
    
    
    string result = (check)? "YES": "NO";
    cout << result << endl;

    return 0;
}
