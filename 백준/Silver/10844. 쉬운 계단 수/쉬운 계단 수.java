import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;

public class Main {
    public static final int MOD = 1_000_000_000;
    public static void main(String[] args) throws IOException {
        // Input Start
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        // Input End
        br.close();

        // Solve : DP
        int[] dp = new int[10];
        int[] tmp = new int[10];

        // 길이가 1인 계단 수
        for (int i = 1; i <= 9; i++) {
            dp[i] = 1;
        }

        for (int i = 2; i <= n; i++) {
            // 마지막 자리가 digit 이고 -1, 1 로 인접할 때
            // 길이가 i인 계단 수 구하기
            for (int digit = 0; digit <= 9; digit++) {
                for (int k = -1; k <= 1; k += 2) {
                    int now = digit + k;
                    if (now < 0 || now > 9) continue;

                    tmp[digit] = (tmp[digit] + dp[now]) % MOD;
                }
            }

            for (int digit = 0; digit <= 9; digit++) {
                dp[digit] = tmp[digit];
                tmp[digit] = 0;
            }
        }

        int answer = 0;
        for (int digit = 0; digit <= 9; digit++) {
            answer = (answer + dp[digit]) % MOD;
        }

        // Output Start
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(answer + "\n");
        bw.flush();

        // Output End
        bw.close();
    }
}