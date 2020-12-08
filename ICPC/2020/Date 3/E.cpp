#include <iostream>

using namespace std;

int main() {
    int n, b;
    cin >> n >> b;

    int originalPerformancePoints[n];
    int performacePoints[n];
    for (int i = 0; i < n; i++) {
        cin >> originalPerformancePoints[i];
        performacePoints[i] = 0;
    }
    
    for (int i = 0; i < n; i++) {
        if (originalPerformancePoints[i] == 0)
            continue;
        
        int currentOriginalPoints = originalPerformancePoints[i];
        int leftPoints = 0, rigthPoints = 0;
        
        if (i == 0)
            leftPoints = originalPerformancePoints[n-1];
        else
            leftPoints = originalPerformancePoints[i-1];
        
        if (i == n-1)
            rigthPoints = originalPerformancePoints[0];
        else
            rigthPoints = originalPerformancePoints[i+1];

        int pointsToChange = 1;
        if (currentOriginalPoints > leftPoints && currentOriginalPoints > rigthPoints)
            pointsToChange += max(leftPoints, rigthPoints);
        else if (currentOriginalPoints > leftPoints && leftPoints != 0)
            pointsToChange += leftPoints;
        else if (currentOriginalPoints > rigthPoints  && rigthPoints != 0)
            pointsToChange += rigthPoints;

        performacePoints[i] = pointsToChange;
    }
    
    for (int i = 0; i < n; i++)
        
    
        cout << performacePoints[i] * b << " ";
}
