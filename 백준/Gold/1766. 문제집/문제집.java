// 1766 : 문제집
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
import java.util.ArrayList;
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) throws IOException {
        // Input Start
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        ArrayList<Integer>[] edge = new ArrayList[n+1];
        for (int i = 0; i <= n; i++) edge[i] = new ArrayList<>();
        int[] inorder = new int[n+1];

        while(m-- > 0) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            edge[a].add(b);
            inorder[b] += 1;
        }

        // Input End
        br.close();

        // Solve
        ArrayList<Integer> ans = new ArrayList<>();
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int i = 1; i <= n; i++) {
            if (inorder[i] == 0) pq.add(i);
        }

        while (!pq.isEmpty()) {
            int now = pq.poll();
            ans.add(now);

            for (int nxt : edge[now]) {
                inorder[nxt] -= 1;
                if (inorder[nxt] == 0) pq.add(nxt);
            }
        }

        // Output Start
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        for (int a : ans) bw.write(a + " ");
        bw.flush();

        // Output End
        bw.close();
    }
}