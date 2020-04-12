#include <iostream>
#include <string>
using namespace std; 

int addIdentifier(string input);

int main() {
    int queries;
    cin >> queries;
    string toPrint = "", tempString, message;
    for (int i=0; i<queries; i++) {
        cin >> tempString;
        message += tempString;
    }

    for (int i=15; i<message.size(); i+=16)
        if (message[i]!='X'&&(message[i-1]!='I'||message[i-1]!='O')) toPrint += message[i];

    int size = toPrint[toPrint.size()-1]-64;
    
    int option = addIdentifier(toPrint.substr(0, toPrint.size()-1));
    switch (option) {
    case 1:
        for (int i=1; i<=size; i++) {
            for (int k=0; k<i; k++) cout << '*';
            cout << endl;
        }
        break;
    case 2:
        for (int i=0; i<size; i++) {
            for (int k=0; k<size; k++) cout << '*';
            cout << endl;
        }
        break;
    case 3:
        for (int i=0; i<size; i++) {
            for (int k=0; k<size-i-1; k++) cout << ' ';
            for (int k=0; k<1+i*2; k++) cout << '*';
            cout << endl;
        }
        break;
    case 4: 
        cout << toPrint << endl;
    }
    return 0;
}

int addIdentifier(string input) {
    if( input == "TRIANGULO" ) return 1;
    if( input == "CUADRADO" ) return 2;
    if( input == "PIRAMIDE" ) return 3;
    return 4;
}