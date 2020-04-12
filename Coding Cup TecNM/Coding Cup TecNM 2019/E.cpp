#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std; 

int main() {
    int instancias, asignaciones;
    cin >> instancias >> asignaciones;
    int referencias = instancias;

    string arr[instancias], referenceArr[instancias];    
    if (asignaciones != 0) {
        string exit;
        getline(cin, arr[0]);
        for (int i=0; i<instancias; i++) {
            cin >> arr[i] >> arr[i];
            getline(cin, exit);
            referenceArr[i] = arr[i];
        }

        string left, right;
        for (int i=0; i<asignaciones; i++) {
            cin >> left >> exit >> right;
            right = right.substr(0,right.size()-1);

            for (int k=0; k<instancias; k++) {
                if (arr[k]==left) {
                    referenceArr[k] = right; 
                }
            }
        }

        referencias = 0;
        for (int i=0; i<instancias; i++) {
            for (int k=0; k<instancias; k++) {
                if (arr[i]==referenceArr[k]) {
                    referencias++; break;
                }
            }
        }
    }
    cout << referencias;
}