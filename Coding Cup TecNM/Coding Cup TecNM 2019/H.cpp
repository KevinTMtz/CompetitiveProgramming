#include <stdio.h>
#include <algorithm>
using namespace std; 

int main() {
    int numbers, left, right, count=0;
    scanf("%i", &numbers);
    int nums[numbers];
    for (int i=0; i<numbers; i++) scanf("%i", &nums[i]);
    scanf("%i %i", &left, &right);

    sort(nums, nums+numbers);

    for (int i=0; i<numbers; i++) {
        if (nums[i]>right) break;
        if (nums[i]>=left&&nums[i]<=right) count++;
    }
    printf("%i", count);

    return 0;
}