#include <stdio.h>
#include <string>
using namespace std;

int main() {
    int piles;
    scanf("%i", &piles);
    int* nums = new int[piles];
    for (int i=0; i<piles; i++) scanf("%i", &nums[i]);
    
    int* sums = new int[piles];
    sums[0] = nums[0];
    for (int i=1; i<piles; i++) sums[i] = nums[i] + sums[i-1];
    
    int juicyWorms;
    scanf("%i", &juicyWorms);
    int* wormsToS = new int[juicyWorms];
    for (int i=0; i<juicyWorms; i++) scanf("%i", &wormsToS[i]);

    for (int x=0; x<juicyWorms; x++) {
        int index = (int) (lower_bound(sums, sums+piles, wormsToS[x]) - sums);
        printf("%i %s", index+1, "\n");
    }
}
