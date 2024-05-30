#include <stdio.h>

typedef struct GraphType {
    int n; // number of vertices
    int **adj_mat;
    int *visited;
} GraphType;

int max_dist = 0;

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
        printf("Vertex Overflow\n");
        return;
    }
    g->n++;
}

void insert_edge(GraphType* g, int start, int end, int weight) {
    if (start >= g->n || end >= g->n) {
        printf("Vertex does not exist\n");
        return;
    }
    g->adj_mat[start][end] = weight;
    g->adj_mat[end][start] = weight;
}

// 가장 거리가 먼 두 마을을 찾을 것이다.
int dfs_search(GraphType* g, int v, int visited[]) {
    visited[v] = 1;
    int max = 0;
    int second_max = 0;
    for (int i = 0; i < g->n; i++) {
        if (g->adj_mat[v][i] != 0 && visited[i] == 0) {
            int path_length = g->adj_mat[v][i] + dfs_search(g, i, visited);
            if (path_length > max) {
                second_max = max;
                max = path_length;
            }
            else if (path_length > second_max) {
                second_max = path_length;
            }
        }
    }

    // 가장 긴 두 경로의 합이 최대 거리가 된다.
    if (max + second_max > max_dist) {
        max_dist = max + second_max;
    }

    // 가장 긴 경로의 길이를 반환한다.
    return max;
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

        printf("%d\n", dfs_search(&g, 0, g.visited));
    }
}