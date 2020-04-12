/*
MARBLES - Marbles
#combinatorics #ad-hoc-1

Hänschen dreams he is in a shop with an infinite amount of marbles. He is allowed to select n marbles. There are marbles of k different colors. From each color there are also infinitely many marbles. Hänschen wants to have at least one marble of each color, but still there are a lot of possibilities for his selection. In his effort to make a decision he wakes up. Now he asks you how many possibilites for his selection he would have had. Assume that marbles of equal color can't be distinguished, and the order of the marbles is irrelevant.

Input
    The first line of input contains a number T <= 100 that indicates the number of test cases to follow. Each test case consists of one line containing n and k, where n is the number of marbles Hänschen selects and k is the number of different colors of the marbles. You can assume that 1<=k<=n<=1000000.

Output
    For each test case print the number of possibilities that Hänschen would have had. You can assume that this number fits into a signed 64 bit integer.

Example
    Input:
        2
        10 10
        30 7

    Output:
        1
        475020
*/

#include <iostream>
using namespace std;

int main() {
    int queries, n, k;
    cin >> queries;
    
    long long int result;
    for (int queriesCount=0; queriesCount<queries; queriesCount++) {
        cin >> n >> k;
        k = ((n-k) < (k-1))? n-k+1 : k;
        
        result = 1;
        for (int i=1; i<=k-1; i++) {
            result *= (n-i);
            result /= i;
        }
        cout << result << endl;
    }
    return 0;
}
