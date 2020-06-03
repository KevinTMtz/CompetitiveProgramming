#include <iostream>
#include <string>
using namespace std;
 
int main() {
    int n;
    cin >> n;
    int* nums = new int[n];
    for (int i=0; i<n; i++) cin >> nums[i];
    
    if (n==1) {
        cout << 0 << endl;
        return 0;
    }
    
    int result = 0;
    for (int i=1; i<n-1; i++) {
        if ((nums[i]==nums[i-1]+1) && (nums[i]==nums[i+1]-1)) {
            int count = 0;
            
            if (nums[i]==2) count++;
            while (i<n-1) {
                if((nums[i-1]+1==nums[i]) && (nums[i]==nums[i+1]-1))
                    count++;
                else break;
                i++;
            }
            
            if (i==n-1 && (nums[n-2]==nums[n-1]-1) && (nums[n-1]==1000))
                count++;
                
            result = max(count, result);
        }
    }
    
    if(n>2 && result==0 && ((nums[0]==1 && nums[1]==2) || (nums[n-2]==999 && nums[n-1]==1000)))
        result++;
    
    if(n==2 && (nums[0]==nums[1]-1) && (nums[0]==1 || nums[1]==1000))
        result++;
    
    cout << result << endl;
}