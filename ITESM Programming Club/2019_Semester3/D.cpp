#include <stdio.h>
using namespace std; 

int main() {
    int n, k, result = 0;
    scanf("%i %i", &n, &k);
    
    int mafiaMembers[n];
    for (int i=1; i<n; i++) scanf("%i", &mafiaMembers[i]);

    //for (int i=1; i<n; i++) printf("%i", mafiaMembers[i]);
    printf("%i", result);

    return 0; 
}