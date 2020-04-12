#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <math.h>
#include <iomanip>
using namespace std; 

double findCircleRadius(double furthestPoints[3][2]);

int main() {
    int n, m, l, questions;
    cin >> n >> m >> l;

    int coordenadas[l][2];
    for (int i=0; i<l; i++)
        cin >> coordenadas[i][0] >> coordenadas[i][1];

    cin >> questions;
    int numOfHumans;
    for (int i=0; i<questions; i++) {
        cin >> numOfHumans;
        int arrIdentifiers[numOfHumans];
        
        double xMin = 1000000000, xMax = 1, yMin = 1000000000, yMax = 1;
        for (int k=0; k<numOfHumans; k++) {
            // Llenar vectores de personas que asistirán en el array
            cin >> arrIdentifiers[k];
            
            // Get min/max X and Y values
            if (coordenadas[arrIdentifiers[k]-1][0] < xMin) xMin = coordenadas[arrIdentifiers[k]-1][0];
            if (coordenadas[arrIdentifiers[k]-1][0] > xMax) xMax = coordenadas[arrIdentifiers[k]-1][0];
            if (coordenadas[arrIdentifiers[k]-1][1] < yMin) yMin = coordenadas[arrIdentifiers[k]-1][1];
            if (coordenadas[arrIdentifiers[k]-1][1] > yMax) yMax = coordenadas[arrIdentifiers[k]-1][1];
        }
        
        // Casos de solo 1 y 2 puntos:
        if (numOfHumans == 1) { cout << 0 << endl; continue; }
        if (numOfHumans == 2) { cout << setprecision(10) << (sqrt((coordenadas[arrIdentifiers[0]-1][0]-coordenadas[arrIdentifiers[1]-1][0])*(coordenadas[arrIdentifiers[0]-1][0]-coordenadas[arrIdentifiers[1]-1][0])+(coordenadas[arrIdentifiers[0]-1][1]-coordenadas[arrIdentifiers[1]-1][1])*(coordenadas[arrIdentifiers[0]-1][1]-coordenadas[arrIdentifiers[1]-1][1]))/2) << endl; continue; }
        
        // Si hay más de dos puntos:
        // Get the center of the smallest rectangle
        double xCoor = (xMax+xMin)/2 , yCoor = (yMax+yMin)/2;
        
        // Get the three furthest points to the center of the rectangle
        double furthestPoints[3][2];
        for (int k=0; k<3; k++) { furthestPoints[i][0] = xCoor; furthestPoints[i][1] = yCoor; }
        double furthestPointsDistance[3] = {0,0,0};
        double length;
        for (int k=0; k<numOfHumans; k++) {
            length = sqrt((coordenadas[arrIdentifiers[k]-1][0]-(xCoor))*(coordenadas[arrIdentifiers[k]-1][0]-(xCoor))+(coordenadas[arrIdentifiers[k]-1][1]-(yCoor))*(coordenadas[arrIdentifiers[k]-1][1]-(yCoor)));
            
            if (length > furthestPointsDistance[0]) {
                furthestPointsDistance[2] = furthestPointsDistance[1];
                furthestPoints[2][0] = furthestPoints[1][0];
                furthestPoints[2][1] = furthestPoints[1][1];
                furthestPointsDistance[1] = furthestPointsDistance[0];
                furthestPoints[1][0] = furthestPoints[0][0];
                furthestPoints[1][1] = furthestPoints[0][1];
                furthestPointsDistance[0] = length;
                furthestPoints[0][0] = coordenadas[arrIdentifiers[k]-1][0];
                furthestPoints[0][1] = coordenadas[arrIdentifiers[k]-1][1];
            } else if (length > furthestPointsDistance[1]) {
                furthestPointsDistance[2] = furthestPointsDistance[1];
                furthestPoints[2][0] = furthestPoints[1][0];
                furthestPoints[2][1] = furthestPoints[1][1];
                furthestPointsDistance[1] = length;
                furthestPoints[1][0] = coordenadas[arrIdentifiers[k]-1][0];
                furthestPoints[1][1] = coordenadas[arrIdentifiers[k]-1][1];
            } else if (length > furthestPointsDistance[2]) {
                furthestPointsDistance[2] = length;
                furthestPoints[2][0] = coordenadas[arrIdentifiers[k]-1][0];
                furthestPoints[2][1] = coordenadas[arrIdentifiers[k]-1][1];
            }
        }

        // Buscar el lado más grande del triangulo
        double l1To2 = sqrt((furthestPoints[0][0]-furthestPoints[1][0])*(furthestPoints[0][0]-furthestPoints[1][0])+(furthestPoints[0][1]-furthestPoints[1][1])*(furthestPoints[0][1]-furthestPoints[1][1]));
        double l2To3 = sqrt((furthestPoints[1][0]-furthestPoints[2][0])*(furthestPoints[1][0]-furthestPoints[2][0])+(furthestPoints[1][1]-furthestPoints[2][1])*(furthestPoints[1][1]-furthestPoints[2][1]));
        double l3To1 = sqrt((furthestPoints[2][0]-furthestPoints[0][0])*(furthestPoints[2][0]-furthestPoints[0][0])+(furthestPoints[2][1]-furthestPoints[0][1])*(furthestPoints[2][1]-furthestPoints[0][1]));
        
        int outPoint;
        bool withThreePoints = true;
        if ((l1To2>=l2To3)&&(l1To2>=l3To1)) {
            outPoint = 2;
            if ((l1To2/2) > furthestPointsDistance[outPoint]) withThreePoints = false;
        } else if ((l2To3>=l1To2)&&(l2To3>=l3To1)) {
            outPoint = 0;
            if ((l2To3/2) > furthestPointsDistance[outPoint]) withThreePoints = false;
        } else {
            outPoint = 1;
            if ((l3To1/2) > furthestPointsDistance[outPoint]) withThreePoints = false;
        }

        double radius;
        if (!withThreePoints) {
            if (outPoint == 2) {
                radius = l1To2/2;
            } else if (outPoint == 0) {
                radius = l2To3/2;
            } else {
                radius = l3To1/2;
            }
        } else {
            radius = findCircleRadius(furthestPoints);
        }
        cout << setprecision(10) << radius << endl;
    }
    return 0;
}

double findCircleRadius(double furthestPoints[3][2]) {
    double x12 = furthestPoints[0][0] - furthestPoints[1][0]; 
    double x13 = furthestPoints[0][0] - furthestPoints[2][0]; 
    double y12 = furthestPoints[0][1] - furthestPoints[1][1]; 
    double y13 = furthestPoints[0][1] - furthestPoints[2][1]; 
    double y31 = furthestPoints[2][1] - furthestPoints[0][1]; 
    double y21 = furthestPoints[1][1] - furthestPoints[0][1]; 
    double x31 = furthestPoints[2][0] - furthestPoints[0][0];
    double x21 = furthestPoints[1][0] - furthestPoints[0][0]; 
  
    double sx13 = pow(furthestPoints[0][0], 2) - pow(furthestPoints[2][0], 2); 
    double sy13 = pow(furthestPoints[0][1], 2) - pow(furthestPoints[2][1], 2); 
    double sx21 = pow(furthestPoints[1][0], 2) - pow(furthestPoints[0][0], 2); 
    double sy21 = pow(furthestPoints[1][1], 2) - pow(furthestPoints[0][1], 2); 
  
    double f = ((sx13) * (x12) + (sy13) * (x12) + (sx21) * (x13) + (sy21) * (x13)) / (2 * ((y31) * (x12) - (y21) * (x13))); 
    double g = ((sx13) * (y12) + (sy13) * (y12) + (sx21) * (y13) + (sy21) * (y13)) / (2 * ((x31) * (y12) - (x21) * (y13))); 
  
    double c = - pow(furthestPoints[0][0], 2) - pow(furthestPoints[0][1], 2) - 2 * g * furthestPoints[0][0] - 2 * f * furthestPoints[0][1]; 
  
    double h = -g; 
    double k = -f;
  
    double r = sqrt(h * h + k * k - c);
    return r;
}