#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <cctype>
using namespace std; 

int main() {
    string message, gS, cS, outputStr, temp;
    cin >> message >> gS >> cS;

    int g = stoi(gS.substr(1, gS.size())); 
    int c = stoi(cS.substr(1, cS.size()));
    
    char operationToDo = message[0];
    message = message.substr(1, message.size());
    
    int start = 0, end = g-1;
    if (operationToDo == 'e' || operationToDo == 'E') {
        transform(message.begin(), message.end(), message.begin(), ::toupper);
        while (start < message.size()) {
            if (end < message.size()) {
                if (message.size()==1) {
                    temp = message;
                } else {
                    temp = message.substr(start, g);
                }
            } else {
                temp = message.substr(start, g);
            }
            
            for (int i=temp.size()-1; i>=0; i--)
                outputStr += temp[i] + c;

            start += g; end += g;
        }
    } else {
        while (start < message.size()) {
            if (end < message.size()) {
                if (message.size()==1) {
                    temp = message;
                } else {
                    temp = message.substr(start, g);
                }
            } else {
                temp = message.substr(start, g);
            }
            
            for (int i=temp.size()-1; i>=0; i--)
                outputStr += temp[i] - c;

            start += g; end += g;
        } 
    }
    cout << outputStr;
}