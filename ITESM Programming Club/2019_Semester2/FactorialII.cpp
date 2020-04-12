#include<iostream>
using namespace std;

int main(){
    int t;
    
    std::cout<<"Cases:";
    std::cin>>t;
    
    int arr[t];

    for(int i = 0;i<t;i++) {
         cin>>arr[i];
    }

    for(int i=0;i<t;i++){
        long zeros = 0;
            
        for(int k=5;(arr[i]/k)>=1;k*=5){
             zeros += (arr[i]/k); 
        }
        std::cout<<zeros<<endl;
    }
    return 0;
}