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
		int[][] dp = new int[n+1][k+1]; // dp[i][j] : i번째 물건까지 넣었을 때, 무게 j 까지 넣을 수 있는 상황에서의 최대 가치
		
		for (int thing = 1; thing <= n; thing++) {
			for (int weight = 1; weight <= k; weight++) {
				if (weights[thing] <= weight) 
					// 지금 물건을 담을 수 있다면,
					// 1. 이전 물건을 담을 때 무게 (weight) 까지 넣을 수 있는 상황에서의 최대 가치
					//		-> 즉, 지금 물건을 넣지 않을 때의 가치
					// 2. 이전 물건을 담을 때 무게 (weight - 현재 물건의 무게) 까지 넣을 수 있는 상황에서의 가치 + 지금 넣을 물건의 가치
					//		-> 즉, 지금 물건을 넣을 때의 가치
					// 중 얻을 수 있는 최대 가치 를 따라간다.
					dp[thing][weight] = Math.max(dp[thing-1][weight], dp[thing-1][weight - weights[thing]] + values[thing]);
				else 
					// 지금 물건을 담을 수 없다면, 위의 1번 (지금 물건을 넣지 않을 때의 가치) 를 따라간다.
					dp[thing][weight] = dp[thing-1][weight];
			}
		}
		
		// Output 시작
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		// n번째 물건까지 넣었을 때, 무게 k 까지 넣을 수 있는 상황에서의 최대 가치 출력
		bw.write(dp[n][k] + "\n"); 
		bw.flush();
		
		// Output 종료
		bw.close();
	}
}
