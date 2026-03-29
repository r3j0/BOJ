// 2293 : 동전 1
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        // Input Start
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        // Input End
        br.close();

        // Solve : DP
        Arrays.sort(arr);

        int[] dp = new int[k+1];
        dp[0] = 1;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j + arr[i] <= k; j++) {
                dp[j + arr[i]] += dp[j];
            }
        }

        // Output Start
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(dp[k] + "\n");
        bw.flush();

        // Output End
        bw.close();
    }
}