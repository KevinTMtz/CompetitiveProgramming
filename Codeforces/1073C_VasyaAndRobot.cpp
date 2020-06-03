#include <iostream>
#include <math.h>
#include <string>
#include <vector>
using namespace std;
 
int main() {
    long long n, x, y;
    cin >> n;
    
    int num = 2e5+10;
    
    char* steps = new char[num];
    
    cin >> (steps+1) >> x >> y;
    
    int* stepsX = new int[num];
    int* stepsY = new int[num];
    
    if((abs(x) + abs(y)) > n || ((int) (n -abs(x) -abs(y)) % 2))
        cout << "-1" << endl;
    else {
        long long result = 0;
        
        for(int i=1; i<=n; i++) {
            if(steps[i]=='U') stepsY[i]++;
            if(steps[i]=='D') stepsY[i]--;
            if(steps[i]=='L') stepsX[i]--;
            if(steps[i]=='R') stepsX[i]++;
            stepsX[i] += stepsX[i-1];
            stepsY[i] += stepsY[i-1];
        }
        
        if (stepsX[n] == x && stepsY[n] == y) result = 0;
        else {
            long long left = 1, right = n;
            
            while(left < right) {
                long long half = (right + left) >> 1;
                
                bool check = false;
                for(long long i = half; i<=n; i++) {
                    if( abs(stepsX[i] -stepsX[i-half] +x -stepsX[n]) +
                        abs(stepsY[i] -stepsY[i-half] +y -stepsY[n]) <= half &&
                       (int)(half -abs(stepsX[i] -stepsX[i -half]+x -stepsX[n]) +
                        abs(stepsY[i] -stepsY[i -half] +y -stepsY[n]))%2 == 0) {
                        check = true;
                    }
                }
                if (check) right = half;
                else left = half + 1;
            }
            result = left;
        }
        cout << result << endl;
    }
    return 0;
}
