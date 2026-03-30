// 11066 : 파일 합치기
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        // Input Output Start
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int t = Integer.parseInt(br.readLine());
        while(t-- > 0) {
            int n = Integer.parseInt(br.readLine());

            StringTokenizer st = new StringTokenizer(br.readLine());
            long[] arr = new long[n+1];
            for (int i = 1; i <= n; i++) {
                arr[i] = Long.parseLong(st.nextToken());
            }

            // Solve : DP
            long[] sarr = new long[n+1];
            long[][] dp = new long[n+1][n+1];
            for (int i = 1; i <= n; i++) {
                Arrays.fill(dp[i], Long.MAX_VALUE / 2);
                sarr[i] = sarr[i-1] + arr[i];
                dp[i][i] = 0;
                if (i > 1)
                    dp[i-1][i] = arr[i-1] + arr[i];
            }

            // size : 3~
            for (int size = 3; size <= n; size++) {
                for (int i = 1; i < n - size + 2; i++) {
                    for (int j = i + 1; j < i + size; j++) {
                        dp[i][i+size-1] = Math.min(dp[i][i+size-1], (dp[i][j-1] + dp[j][i+size-1] + (sarr[i+size-1] - sarr[i-1])));
                    }
                }
            }

            bw.write(dp[1][n] + "\n");
        }

        bw.flush();

        // Input Output End
        br.close();
        bw.close();
    }
}