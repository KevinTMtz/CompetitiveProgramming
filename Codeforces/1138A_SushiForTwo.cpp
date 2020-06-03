#include <iostream>
#include <string>
#include <vector>
using namespace std;
 
int main() {
    int n;
    cin >> n;
    
    int* nums = new int[n];
    for (int i=0; i<n; i++) cin >> nums[i];
 
    vector<int> continuosCount;
    continuosCount.push_back(1);
    
    int index = 0, temp = nums[0];
    for (int i=1; i<n; i++) {
       if (temp != nums[i]) {
            temp = nums[i];
            continuosCount.push_back(1);
            index++;
       } else {
           continuosCount[index]++;
       }
    }
    
    int max = 0;
    for (int i=0; i<continuosCount.size()-1; i++) {
        int minNum = min(continuosCount[i],continuosCount[i+1]);
        if (max < minNum) {
            max = minNum;
        }
    }
    
    cout << max*2 << endl;
}