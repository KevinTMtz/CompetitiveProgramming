#include <iostream>
#include <string>
#include <vector>
using namespace std; 

int main() {
    int queries, queriesProf;
    vector< vector<string> > vectOfConnectedCities;
    
    string temp;
    vector<string> tempArr;
    cin >> queries;
    for (int i=0; i<queries; i++) {
        tempArr.clear();
        cin >> queriesProf;
        for (int k=0; k<queriesProf; k++) {
            cin >> temp;
            tempArr.push_back(temp);
        }
        vectOfConnectedCities.push_back(tempArr);
    }
    
    string startingCity, endingCity; 
    cin >> startingCity >> endingCity;
    
    // Unir los vectores
    for (int i1=0; i1<vectOfConnectedCities.size(); i1++) {
        for (int i2=0; i2<vectOfConnectedCities.size(); i2++) {
            if (i1 == i2) continue;
            bool toBreak = false;
            for (int k1=0; k1<vectOfConnectedCities[i1].size(); k1++) {
                for (int k2=0; k2<vectOfConnectedCities[i2].size(); k2++) {
                    toBreak = false;
                    if (vectOfConnectedCities[i1][k1] == vectOfConnectedCities[i2][k2]) {
                        vectOfConnectedCities[i1].erase(vectOfConnectedCities[i1].begin()+k1);
                        vectOfConnectedCities[i1].insert(vectOfConnectedCities[i1].end(),vectOfConnectedCities[i2].begin(),vectOfConnectedCities[i2].end());
                        vectOfConnectedCities.erase(vectOfConnectedCities.begin()+i2);
                        toBreak = true;
                        break; 
                    }
                }
                if (toBreak) { i2--; break; }
            }
        }
    }
    
    /*
    // Imprimir
    for (int i=0; i<vectOfConnectedCities.size(); i++) {
        for (int k=0; k<vectOfConnectedCities[i].size(); k++) {
            cout << vectOfConnectedCities[i][k] << " ";
        }
        cout << endl;
    }
    */
    
    // Imprimir
    for (int i=0; i<vectOfConnectedCities.size(); i++) {
        for (int k=0; k<vectOfConnectedCities[i].size(); k++) {
            cout << vectOfConnectedCities[i][k] << " ";
        }
        cout << endl;
    }
    

/*
5
2 celaya campeche
3 num7 num2 num3
3 num5 num6 num7
2 num5 num9 num8
2 campeche num8
celaya
num2
*/
    
    bool check1, check2;
    for (int i=0; i<vectOfConnectedCities.size(); i++) {
        check1 = false; check2 = false;
        for (int k=0; k<vectOfConnectedCities[i].size(); k++) {
            if (vectOfConnectedCities[i][k] == startingCity) check1 = true;
            if (vectOfConnectedCities[i][k] == endingCity) check2 = true;
        }
        if (check1 && check2) { break; } 
    }

    cout << ((check1 && check2)? "posible":"imposible") << endl;

    return 0;
}