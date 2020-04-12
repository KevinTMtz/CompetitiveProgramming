#include <stdio.h>
#include <climits>

const int max = 100000;

void dijkstra(int startingCity, int endingCity, int numOfCities, int graph[max][max]);
int minimumDist(int dist[], bool Dset[], int numOfCities);

int main() {
    int queries;
    int cities, highways, startingCity, endingCity;

    int graph[100000][100000];
    
    while (queries != 0) {
        scanf("%i %i %i %i", &cities, &highways, &startingCity, &endingCity);
        
        for (int i=0; i<cities; i++)
            for (int k=0; k<cities; k++)
                graph[i][k] = 0;
        
        int city1, city2;
        for (int i=highways; i<highways; i++)
            scanf("%i %i %i", &city1, &city2, &graph[city1-1][city2-1]);

        dijkstra(startingCity, endingCity, cities, graph);

        queries--;
    }
    return 0;
}

void dijkstra(int startingCity, int endingCity, int numOfCities, int graph[max][max]) {
    int dist[numOfCities];
    bool Dset[numOfCities];
    for(int i=0;i<numOfCities;i++) {
        dist[i]=INT_MAX;
        Dset[i]=false;
    }
    
    dist[startingCity] = 0;
    for(int c=0; c<numOfCities; c++) {
        int u=minimumDist(dist,Dset, numOfCities);
        Dset[u]=true;
        for(int v=0; v<numOfCities; v++)
            if(!Dset[v] && graph[u][v] && dist[u]!=INT_MAX && dist[u]+graph[u][v]<dist[v])
                dist[v]=dist[u]+graph[u][v];
    }
    
    if (dist[endingCity] > 1000) printf("%s", "NONE\n");
    else printf("%i %s", dist[endingCity], "\n");
}

int minimumDist(int dist[], bool Dset[], int numOfCities) {
    int min=INT_MAX, index;
    for(int v=0;v<numOfCities;v++)
        if(Dset[v]==false && dist[v]<=min) {
            min=dist[v];
            index=v;
        }
    return index;
}
