#include <stdio.h>
#include <stdlib.h>
#define MAX_HEAP 1000001
#define MAX_VERTEX 10001
typedef long long LL;

// 우선순위 큐에 들어갈 노드 구조체
typedef struct _Node {
    LL current_distance;
    int current_destination;
    int current_speed;
} Node;

// 우선순위 큐 구조체
typedef struct _Heap {
    Node data[MAX_HEAP];
    int heap_size;
} Heap;

// 인접리스트 노드
typedef struct _GraphNode {
    int dest; 
    LL length; 
    int limit;
} GraphNode;

// 인접리스트 그래프
typedef struct _Graph {
    GraphNode data;
    struct _Graph* next;
    struct _Graph* last;
} Graph;
Graph g[MAX_VERTEX];

LL distances[MAX_VERTEX][10] = {0,};

// 그래프에 간선 정보 추가
void newnode(Graph* now, int input_dest, LL input_length, int input_limit) {
    Graph* tmp = (Graph*)malloc(sizeof(Graph));
    (tmp->data).dest = input_dest;
    (tmp->data).length = input_length * 3628800;
    (tmp->data).limit = input_limit;
    tmp->next = NULL;
    tmp->last = NULL;

    if (now->next == NULL) now->next = tmp;
    else now->last->next = tmp;
    now->last = tmp;
}

// 우선 순위 정렬 조건
int heapq_compare(Node a, Node b) {
    if ((a.current_distance > b.current_distance) || (a.current_distance == b.current_distance && a.current_destination > b.current_destination) || (a.current_distance == b.current_distance && a.current_destination == b.current_destination && a.current_speed > b.current_speed)) return 1;
    return 0;
}

// 우선순위 큐에 노드 추가
void addHeapQ(Heap* heapq, LL cdist, int cdest, int cspeed) {
    heapq->heap_size += 1;
    heapq->data[heapq->heap_size].current_distance = cdist;
    heapq->data[heapq->heap_size].current_destination = cdest;
    heapq->data[heapq->heap_size].current_speed = cspeed;

    int now = heapq->heap_size;
    int parent = now / 2;

    while (parent) {
        if (heapq_compare(heapq->data[parent], heapq->data[now])) {
            Node tmp = heapq->data[parent];
            heapq->data[parent] = heapq->data[now];
            heapq->data[now] = tmp;

            now = parent;
            parent = now / 2;
        }
        else break;
    }
}

// 우선순위 큐에서 노드 제거
Node removeHeapQ(Heap* heapq) {
    Node result = heapq->data[1];
    heapq->data[1] = heapq->data[heapq->heap_size--];

    int now = 1;
    int child = 2;
    while (child <= heapq->heap_size) {
        if (child + 1 <= heapq->heap_size && heapq_compare(heapq->data[child], heapq->data[child+1])) child += 1;

        if (heapq_compare(heapq->data[now], heapq->data[child])) {
            Node tmp = heapq->data[now];
            heapq->data[now] = heapq->data[child];
            heapq->data[child] = tmp;

            now = child;
            child = now * 2;
        }
        else break;
    }

    return result;
}

void dijkstra(int start) {
    distances[start][0] = 0;

    // 우선순위 큐 초기화
    Heap* heapq = (Heap*)malloc(sizeof(Heap));
    heapq->heap_size = 0;

    addHeapQ(heapq, 0, start, 1);

    while(heapq->heap_size) {
        Node now = removeHeapQ(heapq);

        if (distances[now.current_destination][now.current_speed - 1] < now.current_distance) continue;
        
        for (int speedd = 1; speedd >= -1; speedd--) {
            int now_speed = now.current_speed + speedd;
            if (now_speed <= 0) continue;

            Graph* search = g[now.current_destination].next;
            while(search) {
                if ((search->data).limit >= now_speed) {
                    LL distance = now.current_distance + ((search->data).length / now_speed);
                    if (distances[(search->data).dest][now_speed - 1] == -1 || distance < distances[(search->data).dest][now_speed - 1]) {
                        distances[(search->data).dest][now_speed - 1] = distance;
                        addHeapQ(heapq, distance, (search->data).dest, now_speed);
                    }
                }
                search = search->next;
            }
        }
    }
    free(heapq);
}

int main(void) {
    int n, m;
    scanf("%d %d", &n, &m);

    // 그래프 초기화
    for (int i = 1; i <= n; i++) {
        g[i].data.dest = 0;
        g[i].data.length = 0;
        g[i].data.limit = 0;
        g[i].next = NULL;
        g[i].last = NULL;
    }
    // 다익스트라 - distances 초기화
    for (int i = 1; i <= n; i++) {
        for (int j = 0; j < 10; j++)
            distances[i][j] = -1;
    }

    int a, b, k;
    LL l;
    for (int i = 0; i < m; i++) {
        scanf("%d %d %lld %d", &a, &b, &l, &k);
        newnode(&g[a], b, l, k);
        newnode(&g[b], a, l, k);
    }
    
    dijkstra(1);

    int min_idx = 0;
    for (int i = 1; i < 10; i++) {
        if ((distances[n][min_idx] == -1 && distances[n][i] != -1) || (distances[n][min_idx] != -1 && distances[n][i] != -1 && distances[n][min_idx] > distances[n][i])) min_idx = i;
    }
    LL result_distance1 = distances[n][min_idx] / 3628800;
    LL tmp_result = distances[n][min_idx] % 3628800;
    long double tmp_result2 = tmp_result / (long double)3628800;
    printf("%lld", result_distance1);
    LL tmp_result3 = (LL)(tmp_result2 * 10000000000);
    if (tmp_result3 % 10 >= 5) tmp_result3 = (tmp_result3 + 10);
    tmp_result3 /= 10;
    printf(".%09lld", tmp_result3);

    return 0;

}