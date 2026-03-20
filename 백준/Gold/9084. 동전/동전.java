// 9084 : 동전
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        // Input Output Start
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        int t = Integer.parseInt(br.readLine());
        while (t-- > 0) {
            // Test Case Input
            int n = Integer.parseInt(br.readLine());

            st = new StringTokenizer(br.readLine());
            int[] coins = new int[n];
            for (int i = 0; i < n; i++) {
                coins[i] = Integer.parseInt(st.nextToken());
            }


            int m = Integer.parseInt(br.readLine());

            // Solve : DP
            int[] dp = new int[m+1];
            dp[0] = 1;

            for (int c = 0; c < n; c++) {
                for (int p = coins[c]; p <= m; p++) {
                    dp[p] += dp[p - coins[c]];
                }
            }

            // Test Case Output
            int ans = dp[m];
            bw.write(ans + "\n");
        }

        bw.flush();

        // Input Output End
        br.close();
        bw.close();
    }
}