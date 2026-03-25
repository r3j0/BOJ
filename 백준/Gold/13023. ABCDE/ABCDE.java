import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
import java.util.ArrayList;

public class Main {
    public static ArrayList<ArrayList<Integer>> graph;
    public static boolean[] visited;
    public static void main(String[] args) throws IOException {
        // Input Start
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        graph = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            graph.get(a).add(b);
            graph.get(b).add(a);
        }

        // Input End
        br.close();

        // Solve : DFS
        // 주요 아이디어 : DFS 를 했을 때 도달 길이가 4 이상이면 존재한다.
        int answer = 0;

        visited = new boolean[n];
        for (int i = 0; i < n; i++) {
            visited[i] = true;
            if (dfs(i, 0)) {
                answer = 1;
                break;
            }
            visited[i] = false;
        }

        // Output Start
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(answer + "\n");
        bw.flush();

        // Output End
        bw.close();
    }

    public static boolean dfs(int now, int depth) {
        if (depth == 4) return true;

        for (int next : graph.get(now)) {
            if (!visited[next]) {
                visited[next] = true;
                if (dfs(next, depth + 1)) {
                    return true;
                }
                visited[next] = false;
            }
        }

        return false;
    }
}