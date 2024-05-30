#include <stdio.h>

typedef struct GraphType {
    int n; // number of vertices
    int **adj_mat;
    int *visited;
} GraphType;

void init(GraphType* g, int n) {
    g->n = 0;
    g->adj_mat = (int**)malloc(sizeof(int*) * n);
    for (int i = 0; i < n; i++) {
        g->adj_mat[i] = (int*)malloc(sizeof(int) * n);
        for (int j = 0; j < n; j++) {
            g->adj_mat[i][j] = 0;
        }
    }
    g->visited = (int*)malloc(sizeof(int) * n);
    for (int i = 0; i < n; i++) {
        g->visited[i] = 0;
    }
}

void insert_vertex(GraphType* g, int v) {
    if (((g->n) + 1) > 100) {
        printf("그래프 정점의 개수 초과\n");
        return;
    }
    g->n++;
}

void insert_edge(GraphType* g, int start, int end, int weight) {
    if (start >= g->n || end >= g->n) {
        printf("정점 번호 오류\n");
        return;
    }
    g->adj_mat[start][end] = weight;
    g->adj_mat[end][start] = weight;
}

void dfs_search(GraphType* g, int v, int visited[]) {
    visited[v] = 1;
    printf("%d ", v);
    for (int w = 0; w < g->n; w++) {
        if (g->adj_mat[v][w] && !visited[w]) {
            dfs_search(g, w, visited);
        }
    }
}

int main() {
    int t;
    scanf("%d", &t);

    for(int i = 0; i < t; i++) {
        GraphType g;

        int n;  // # of vertices
        scanf("%d", &n);
        init(&g, n);

        int u, v, d;  // u : uth vertex, v : vth vertex, d : distance
        for(int j = 0; j < n; j++) {
            scanf("%d %d %d", &u, &v, &d);
            insert_vertex(&g, u);
            insert_vertex(&g, v);
            insert_edge(&g, u, v, d);
        }
    }
}