#include <chrono>
#include<iostream> 
#include <stdio.h>
using namespace std; 

int main() { 
    //ios_base::sync_with_stdio(true);
    //cout.tie(NULL);
    
    chrono::time_point<std::chrono::system_clock> start1, end1, start2, end2;
  
    // cout
    start1 = chrono::system_clock::now();
    for (int i=0; i<1000000; i++) cout << i;
    end1 = chrono::system_clock::now();

    // printf
    start2 = chrono::system_clock::now();
    for (int i=0; i<1000000; i++) printf("%i", i);
    end2 = chrono::system_clock::now();

    // Get and print execution time first operation -cout-
    chrono::duration<double> elapsed_seconds = end1 - start1; 
    time_t end_time = chrono::system_clock::to_time_t(end1);

    cout << endl << "Finished computation at: " << ctime(&end_time) << "Elapsed time: " << elapsed_seconds.count() << "s\n";
    
    // Get and print execution time second operation -printf-
    elapsed_seconds = end2 - start2; 
    end_time = chrono::system_clock::to_time_t(end2);

    cout << endl << "Finished computation at: " << ctime(&end_time) << "Elapsed time: " << elapsed_seconds.count() << "s\n";

    return 0; 
}