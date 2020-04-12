#include <iostream>
#include <algorithm>
#include <math.h>
using namespace std; 

int main() {
    int range, numOfSensors;
    cin >> range >> numOfSensors;

    int sensorsCoordinates[numOfSensors][2];
    int xMin = 0, xMax = 0, yMin = 0, yMax = 0;
    
    int maxMinCuadrante[4][2]; 
    for (int i=0; i<4; i++)  { maxMinCuadrante[i][0] = 0; maxMinCuadrante[i][1] = 0; }
    
    for (int i=0; i<numOfSensors; i++) {
        cin >> sensorsCoordinates[i][0] >> sensorsCoordinates[i][1];

        // Buscar máximos y mínimos totales
        if (sensorsCoordinates[i][0]<xMin) xMin = sensorsCoordinates[i][0];
        if (sensorsCoordinates[i][0]>xMax) xMax = sensorsCoordinates[i][0];
        if (sensorsCoordinates[i][1]<yMin) yMin = sensorsCoordinates[i][1];
        if (sensorsCoordinates[i][1]>yMax) yMax = sensorsCoordinates[i][1];

        // Buscar más lejanos del origen en cada cuadrante
        if (sensorsCoordinates[i][0]>0 && sensorsCoordinates[i][1]>0) {
            if (sensorsCoordinates[i][0] > maxMinCuadrante[0][0])
                maxMinCuadrante[0][0] = sensorsCoordinates[i][0];
            
            if (maxMinCuadrante[0][1] < sensorsCoordinates[i][1])
                maxMinCuadrante[0][1] = sensorsCoordinates[i][1];
        } else if (sensorsCoordinates[i][0]<0 && sensorsCoordinates[i][1]>0) {
            if (sensorsCoordinates[i][0] < maxMinCuadrante[1][0])
                maxMinCuadrante[1][0] = sensorsCoordinates[i][0];
            
            if (maxMinCuadrante[1][1] < sensorsCoordinates[i][1])
                maxMinCuadrante[1][1] = sensorsCoordinates[i][1];
        } else if (sensorsCoordinates[i][0]<0 && sensorsCoordinates[i][1]<0) {
            if (sensorsCoordinates[i][0] < maxMinCuadrante[2][0])
                maxMinCuadrante[2][0] = sensorsCoordinates[i][0];
            
            if (maxMinCuadrante[2][1] > sensorsCoordinates[i][1])
                maxMinCuadrante[2][1] = sensorsCoordinates[i][1];
        } else if (sensorsCoordinates[i][0]>0 && sensorsCoordinates[i][1]<0) {
            if (sensorsCoordinates[i][0] > maxMinCuadrante[3][0])
                maxMinCuadrante[3][0] = sensorsCoordinates[i][0];
            
            if (maxMinCuadrante[3][1] > sensorsCoordinates[i][1])
                maxMinCuadrante[3][1] = sensorsCoordinates[i][1];
        }
    }
    
    int gridWidth = 1 + xMax - xMin, gridHeight = 1 + yMax - yMin;
    char grid[gridHeight][gridWidth];
    
    // Llenar de espacios
    for (int i=0; i<gridHeight; i++) {
        for (int k=0; k<gridWidth; k++) {
            grid[i][k] = ' ';
        }
    }
    
    // Definir origen
    int originX = - xMin, originY = yMax;
    grid[originY][originX] = '#';
    
    // Llenar primer cuadrante
    for (int i=originY; i>=originY-maxMinCuadrante[0][1]; i--) {
        for (int k=originX+1; k<=originX+maxMinCuadrante[0][0]; k++) {
            grid[i][k] = 'o';
        }
    }
    
    // Llenar segundo cuadrante
    for (int i=originY-1; i>=originY-maxMinCuadrante[1][1]; i--) {
        for (int k=originX; k>=originX+maxMinCuadrante[1][0]; k--) {
            grid[i][k] = 'o';
        }
    }
    
    // Llenar tercer cuadrante
    for (int i=originY; i<=originY-maxMinCuadrante[2][1]; i++) {
        for (int k=originX-1; k>=originX+maxMinCuadrante[2][0]; k--) {
            grid[i][k] = 'o';
        }
    }
    
    // Llenar cuarto cuadrante
    for (int i=originY+1; i<=originY-maxMinCuadrante[3][1]; i++) {
        for (int k=originX; k<=originX+maxMinCuadrante[3][0]; k++) {
            grid[i][k] = 'o';
        }
    }

    // Colocar dispositivos
    for (int i=0; i<numOfSensors; i++) {
        bool checkIfInRange = false;

        if (sqrt(sensorsCoordinates[i][0]*sensorsCoordinates[i][0]+sensorsCoordinates[i][1]*sensorsCoordinates[i][1]) <= range) checkIfInRange = true;

        grid[originY-sensorsCoordinates[i][1]][originX+sensorsCoordinates[i][0]] = (checkIfInRange)? '+' : 'x';
    }

    // Imprimir grid
    for (int i=0; i<gridHeight; i++) {
        for (int k=0; k<gridWidth; k++) {
            cout << grid[i][k];
        }
        cout << endl;
    }
}