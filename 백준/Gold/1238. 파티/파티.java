// 1238 : 파티
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.util.ArrayList;
import java.util.PriorityQueue;

class Edge {
    int next;
    int cost;

    public Edge(int next, int cost) {
        this.next = next;
        this.cost = cost;
    }
}

class Node {
    int c;
    int v;

    public Node(int c, int v) {
        this.c = c;
        this.v = v;
    }
}

public class Main {
    public static int n;
    public static ArrayList<Edge>[] edges;

    public static void main(String[] args) throws IOException {
        // Input Start
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int x = Integer.parseInt(st.nextToken());

        edges = new ArrayList[n+1];
        for (int i = 0; i < n+1; i++) {
            edges[i] = new ArrayList<Edge>();
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            edges[a].add(new Edge(b, c));
        }

        // Input End
        br.close();

        // Solve
        int[][] times = new int[n+1][n+1];
        for (int i = 1; i <= n; i++) {
            times[i] = dijkstra(i);
        }

        int answer = 0;
        for (int i = 1; i <= n; i++) {
            answer = Math.max(answer, times[x][i] + times[i][x]);
        }

        // Output Start
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(answer + "\n");
        bw.flush();

        // Output End
        bw.close();
    }

    public static int[] dijkstra(int start) {
        int[] distances = new int[n+1];
        Arrays.fill(distances, Integer.MAX_VALUE / 2);
        PriorityQueue<Node> pq = new PriorityQueue<>((a, b) -> a.c - b.c);

        pq.add(new Node(0, start));
        distances[start] = 0;

        while(!pq.isEmpty()) {
            Node now = pq.poll();
            if (distances[now.v] < now.c) continue;

            for (Edge e : edges[now.v]) {
                int new_cost = now.c + e.cost;
                if (distances[e.next] > new_cost) {
                    distances[e.next] = new_cost;
                    pq.add(new Node(new_cost, e.next));
                }
            }
        }

        return distances;
    }
}