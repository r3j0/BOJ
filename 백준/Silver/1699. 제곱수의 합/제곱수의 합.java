import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class Main {
	public static void main(String[] args) throws IOException {
		// Input Start
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		
		// Input End
		br.close();
		
		// Solve : DP
		// dp[i] : 자연수 i를 제곱수들의 합으로 표현할 때에 그 항의 최소 개수
		int[] dp = new int[n+1];
		Arrays.fill(dp, Integer.MAX_VALUE / 2);
		dp[0] = 0;
		dp[1] = 1;
		
		for (int i = 2; i <= n; i++) {
			for (int j = 1; i - (int)Math.pow(j, 2) >= 0; j++) {
				dp[i] = Math.min(dp[i], dp[i - (int)Math.pow(j, 2)] + 1);
			}
		}
		
		int result = dp[n];
		
		// Output Start
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		bw.write(result + "\n");
		bw.flush();
		
		// Output End
		bw.close();
	}
}