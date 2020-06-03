#include <iostream>
#include <math.h>
#include <string>
#include <set>
#include <iterator>
using namespace std;
 
bool checkIfGood(string x, string y);
 
int main() {
    int queries;
    cin >> queries;
    
    string x, y;
    for (int i=0; i<queries; i++) {
        cin >> x >> y;
        
        if (x==y) {
            cout << "YES" << endl;
            continue;
        }
        
        if ((x.size()==1 && x!=y) || !checkIfGood(x, y))
            cout << "NO" << endl;
        else
            cout << "YES" << endl;
    }
}
 
bool checkIfGood(string x, string y) {
    set<char> char_set1(x.begin(), x.end());
    set<char> char_set2(y.begin(), y.end());
    
    set<char>::iterator atIndex1 = char_set1.begin();
    for (int i=0; i<char_set1.size(); i++) {
        set<char>::iterator atIndex2 = char_set2.begin();
        for (int k=0; k<char_set2.size(); k++) {
            if (*atIndex1==*atIndex2)
                return true;
        atIndex2++;
        }
        atIndex1++;
    }
    return false;
}