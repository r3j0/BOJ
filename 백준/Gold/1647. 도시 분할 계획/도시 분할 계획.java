// 1647 : 도시 분할 계획
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.StringTokenizer;
import java.util.PriorityQueue;

class Edge {
    int u, v, cost;
    public Edge(int u, int v, int cost) {
        this.u = u;
        this.v = v;
        this.cost = cost;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        // Input Start
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        PriorityQueue<Edge> edges = new PriorityQueue<>((a, b) -> a.cost - b.cost);

        while (m-- > 0) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            edges.add(new Edge(a, b, c));
        }

        // Input End
        br.close();

        // Solve : MST
        int[] parent = new int[n+1];
        for (int i = 1; i <= n; i++) parent[i] = i;

        int answer = 0;
        int last_edge = 0;
        while (!edges.isEmpty()) {
            Edge e = edges.poll();
            if (union(parent, e.u, e.v)) {
                answer += e.cost;
                last_edge = e.cost;
            }
        }

        answer -= last_edge; // 두 마을 분할

        // Output Start
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(answer + "\n");
        bw.flush();

        // Output End
        bw.close();
    }

    public static int find(int[] p, int a) {
        if (p[a] == a) return a;
        return p[a] = find(p, p[a]);
    }
    public static boolean union(int[] p, int a, int b) {
        a = find(p, a);
        b = find(p, b);
        if (a > b) {
            int tmp = a; a = b; b = tmp;
        }

        if (a != b) {
            p[b] = a;
            return true;
        }
        return false;
    }
}