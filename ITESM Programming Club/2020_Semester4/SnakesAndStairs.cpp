//
//  main.cpp
//  Snakes & Stairs
//
//  Created by Kevin Torres Martínez on 19/02/20.
//  Copyright © 2020 Kevin Torres Martínez. All rights reserved.
//

#include <iostream>
#include <queue>
using namespace std;

int getMinThrows(int board[], int boardLength);

int main(int argc, const char * argv[]) {
    /*
    - Input format: (starting at 0)
    Board length (# of tiles)
    Ladders num
    Snakes num
    
    Ladder start & ladder end (smaller & bigger)
    Snake start & snake end (smaller & bigger)
    
    - Example:
    100
    2
    3
    1 18
    7 18
     
    24 2
    22 20
    13 6
     
    30
    4
    4
    11 26
    3 22
    5 8
    20 29
    
    1 27
    4 17
    9 21
    7 19
    */
    
    int boardlength = 0;
    int laddersNum = 0;
    int snakesNum = 0;
    cin >> boardlength >> laddersNum >> snakesNum;
    
    int board[boardlength];
    for (int i=0; i<boardlength; i++)
        board[i] = -1;
    
    int ladderStart, ladderEnd;
    for (int i=0; i<laddersNum; i++) {
        cin >> ladderStart >> ladderEnd;
        board[ladderStart-1] = ladderEnd-1;
    }
    
    int snakeStart, snakeEnd;
    for (int i=0; i<snakesNum; i++) {
        cin >> snakeStart >> snakeEnd;
        board[snakeEnd-1] = snakeStart-1;
    }
    
    cout << getMinThrows(board, boardlength) << endl;
    return 0;
}

struct queueEntry {
    int numOfVertex;
    int distanceVertexToSource;
};

int getMinThrows(int board[], int boardLength) {
    bool *visited = new bool[boardLength];
    for (int i=0; i<boardLength; i++)
        visited[i] = false;
    visited[0] = true;
    
    // Queue for BFS
    queue<queueEntry> bfsQueue;
    queueEntry distance = {0,0};
    bfsQueue.push(distance);
    
    // BFS from 0
    queueEntry queueEntryBfs;
    
    while (!bfsQueue.empty()) {
        queueEntryBfs = bfsQueue.front();
        int vertexNum = queueEntryBfs.numOfVertex;
        
        if (vertexNum == boardLength-1)
            break;
        
        bfsQueue.pop();
        
        for (int i=vertexNum+1; i<=(vertexNum+6) && i < boardLength; ++i) {
            if (!visited[i]) {
                queueEntry temp;
                temp.distanceVertexToSource = queueEntryBfs.distanceVertexToSource + 1;
                visited[i] = true;
                
                if (board[i] != -1)
                    temp.numOfVertex = board[i];
                else
                    temp.numOfVertex = i;
                
                bfsQueue.push(temp);
            }
        }
    }
    
    return queueEntryBfs.distanceVertexToSource;
}
