// 1707 : 이분 그래프
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // Input Output Start
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        ArrayList<Integer>[] graph;
        int[] vis;

        int k = Integer.parseInt(br.readLine());
        while (k-- > 0) {
            st = new StringTokenizer(br.readLine());
            int v = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());

            graph = new ArrayList[v+1];
            for (int i = 1; i <= v; i++) graph[i] = new ArrayList<>();
            vis = new int[v+1];

            for (int i = 0; i < e; i++) {
                st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());

                graph[a].add(b);
                graph[b].add(a);
            }

            // Solve : BFS
            // 주요 아이디어 : BFS 중 visited 배열 1 / 2 처리
            Queue<Integer> q = new LinkedList<>();

            boolean ans = true;
            for (int i = 1; i <= v; i++) {
                if (vis[i] == 0) {
                    vis[i] = 1;
                    q.add(i);

                    while (!q.isEmpty()) {
                        int now = q.poll();

                        for (int next : graph[now]) {
                            if (vis[next] == 0) {
                                vis[next] = vis[now] ^ 3; // 01 ^ 11 -> 10, 10 ^ 11 -> 01
                                q.add(next);
                                continue;
                            }

                            if (vis[now] == vis[next]) {
                                ans = false;
                                break;
                            }
                        }

                        if (!ans) break;
                    }
                }

                if (!ans) break;
            }

            bw.write(ans ? "YES\n" : "NO\n");
        }

        bw.flush();

        // Input Output End
        br.close();
        bw.close();
    }
}