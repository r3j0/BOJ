import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) throws IOException {
        // Input Start
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] arr = new int[n+1];
        for (int i = 1; i <= n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int m = Integer.parseInt(br.readLine());
        ArrayList<int[]> query = new ArrayList<>();
        while(m-- > 0) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());

            query.add(new int[]{s, e});
        }

        // Input End
        br.close();

        // Solve : DP
        boolean[][] dp = new boolean[n+1][n+1]; // dp[i][j] : (i, j) 가 팰린드롬인가?

        // 초기 길이가 1, 2인 팰린드롬 세팅
        for (int i = 1; i <= n; i++) {
            dp[i][i] = true;

            if (i == n) continue;
            if (arr[i] == arr[i+1]) {
                dp[i][i+1] = true;
            }
        }

        // 길이가 3 이상인 팰린드롬 세팅
        for (int size = 3; size <= n; size++) {
            for (int i = 1; i <= n - size + 1; i++) {
                // 중간이 팰린드롬이고 앞 뒤가 같다면 팰린드롬
                if (arr[i] == arr[i+size-1] && dp[i+1][i+size-2]) {
                    dp[i][i+size-1] = true;
                }
            }
        }

        // Output Start
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int lenQ = query.size();
        for (int i = 0; i < lenQ; i++) {
            int[] now = query.get(i);
            bw.write((dp[now[0]][now[1]] ? "1" : "0") + "\n");
        }

        bw.flush();

        // Output End
        bw.close();
    }
}