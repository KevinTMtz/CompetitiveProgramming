#include <chrono>
#include<iostream>
using namespace std; 

int main() { 
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    chrono::time_point<std::chrono::system_clock> start1, end1, start2, end2;
    int num1[1000000];
    
    // cin
    start1 = chrono::system_clock::now();
    for (int i=0; i<1000000; i++) cin >> num1[i];
    end1 = chrono::system_clock::now();

    // Get and print execution time first operation -cin-
    chrono::duration<double> elapsed_seconds = end1 - start1; 
    time_t end_time = chrono::system_clock::to_time_t(end1);

    cout << "Cin" << endl << "Finished computation at: " << ctime(&end_time) << "Elapsed time: " << elapsed_seconds.count() << "s\n";

    return 0; 
}