#include <iostream>
using namespace std;
 
int main() {
    int n, t;
    cin >> n >> t;
 
    int timeAndInterval[n][2];
    int diference[n];
    for (int i=0; i<n; i++) {
        cin >> timeAndInterval[i][0] >> timeAndInterval[i][1];
 
        if (timeAndInterval[i][0]==t) {
            diference[i] = 0;
        } else {
            if (timeAndInterval[i][0]>t) {
                diference[i] = timeAndInterval[i][0]-t;
            } else {
                int sum = timeAndInterval[i][0];
                while (true) {
                    sum += timeAndInterval[i][1];
                    if (sum>=t) break;
                } 
                diference[i] = sum-t;
            }
        }
    }
 
    int route = 1, min = diference[0];
    for (int i=1; i<n; i++) {
        if (diference[i]<min) {
            route = i+1;
            min = diference[i];
        }
    }
    cout << route;
 
    return 0;
}