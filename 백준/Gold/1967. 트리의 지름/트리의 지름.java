// 1967 : 트리의 지름
import org.w3c.dom.Node;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
import java.util.ArrayList;
import java.util.PriorityQueue;

class Edge {
    int idx, cost;
    public Edge (int idx, int cost) {
        this.idx = idx;
        this.cost = cost;
    }
}

public class Main {
    public static ArrayList<Edge>[] graph;
    public static int answer = 0;

    public static void main(String[] args) throws IOException {
        // Input Start
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        StringTokenizer st;
        graph = new ArrayList[n+1];
        for (int i = 0; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < n - 1; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            graph[u].add(new Edge(v, c));
        }

        // Input End
        br.close();

        // Solve : DFS
        answer = Math.max(dfs(1), answer);

        // Output Start
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(answer + "\n");
        bw.flush();

        // Output End
        bw.close();
    }

    public static int dfs(int now) {
        PriorityQueue<Integer> edges = new PriorityQueue<>();
        for (Edge e : graph[now]) {
            edges.add(-(dfs(e.idx) + e.cost));
        }

        int[] res = new int[]{0, 0};
        for (int i = 0; i < 2; i++) {
            if (!edges.isEmpty()) {
                res[i] = -edges.poll();
            }
        }
        
        answer = Math.max(answer, res[0] + res[1]);
        return res[0];
    }
}