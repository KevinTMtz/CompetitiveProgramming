#include <iostream>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

int main() {
    int y = 0, x = 0;
    cin >> y >> x;
    
    char lettersArr [y][x];

    for (int i=0; i<y; i++) {
        string tempStr = "";
        cin >> tempStr;
        for (int k=0; k<x; k++) {
            lettersArr[i][k] = tempStr[k];
            // cout << tempStr[k] << " ";
        }
        // cout << endl;
    }

    int n = 0, minLength = 41, maxLength = 1;
    cin >> n;
    vector<map<char,int>> mapsVect;
    for (int i=0; i<n; i++) {
        string tempStr = "";
        cin >> tempStr;
        // cout << tempStr << endl;

        minLength = min(minLength, static_cast<int>(tempStr.length()));
        maxLength = max(maxLength, static_cast<int>(tempStr.length()));

        mapsVect.push_back({});
        for (int k=0; k<tempStr.length(); k++)
            mapsVect[i][tempStr[k]]++;

        // for (const auto& t : mapsVect[i])
        //     cout << t.first << " " 
        //         << t.second << "\n";
        // cout << endl;
    }

    // cout << minLength << " " << maxLength;
}
