import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
    public static final int MOD = 1_000_000_000;
    public static void main(String[] args) throws IOException {
        // Input Start
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        // Input End
        br.close();

        // Solve : DP
        int[][] dp = new int[n+1][k+1]; // dp[i][j] : 수 i 를 정수 j개를 사용해서 만들 때 경우의 수
        dp[0][0] = 1;

        for (int c = 1; c <= k; c++) { // 사용한 정수 개수 c
            for (int i = 1; i <= n; i++) { // 만들려는 숫자 i
                for (int j = 0; j < i; j++) {
                    for (int v = 0; v < c; v++) {
                        dp[i][c] = (dp[i][c] + dp[j][v]) % MOD;
                    }
                }
            }
        }

        int result = 0;
        for (int i = 0; i <= k; i++) {
            result = (result + dp[n][i]) % MOD;
        }

        // Output Start
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(result + "\n");
        bw.flush();

        // Output End
        bw.close();
    }
}