import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		// Input 시작
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		// 물품의 수 n, 버틸 수 있는 무게 k 입력
		int n = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken());
		
		// 각 물건의 무게 w, 물건의 가치 v 입력
		int[] weights = new int[n+1];
		int[] values = new int[n+1];
		for (int i = 1; i <= n; i++) {
			st = new StringTokenizer(br.readLine());
			weights[i] = Integer.parseInt(st.nextToken());
			values[i] = Integer.parseInt(st.nextToken());
		}
		
		// Input 종료
		br.close();
		
		// Knapsack DP
		int[][] dp = new int[n+1][k+1];
		
		for (int weight = 1; weight <= k; weight++) {
			for (int thing = 1; thing <= n; thing++) {
				if (weights[thing] <= weight)
					dp[thing][weight] = Math.max(dp[thing-1][weight], dp[thing-1][weight - weights[thing]] + values[thing]);
				else
					dp[thing][weight] = dp[thing-1][weight];
			}
		}
		
		// Output 시작
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		bw.write(dp[n][k] + "\n");
		bw.flush();
		
		// Output 종료
		bw.close();
	}
}
