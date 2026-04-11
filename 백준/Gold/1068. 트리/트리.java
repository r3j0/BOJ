// 1068 : 트리
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.util.ArrayList;

public class Main {
    public static ArrayList<Integer>[] edge;
    public static void main(String[] args) throws IOException {
        // Input Start
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        edge = new ArrayList[n];
        for (int i = 0; i < n; i++) edge[i] = new ArrayList<>();

        int start = 0;
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            int x = Integer.parseInt(st.nextToken());
            if (x == -1) {
                start = i;
                continue;
            }

            edge[x].add(i);
        }

        int k = Integer.parseInt(br.readLine());

        // Input End
        br.close();

        // Solve
        int answer = 0;
        if (start != k) answer = dfs(start, k);

        // Output Start
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(answer + "\n");
        bw.flush();

        // Output End
        bw.close();
    }

    public static int dfs(int now, int k) {
        int cnt = 0;
        for (int nxt : edge[now]) {
            if (k == nxt) continue;
            cnt += dfs(nxt, k);
        }

        return Math.max(1, cnt);
    }
}