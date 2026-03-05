import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		// Input Start
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int n = Integer.parseInt(br.readLine());
		
		int[][] matrix = new int[n][2];
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			
			matrix[i][0] = Integer.parseInt(st.nextToken());
			matrix[i][1] = Integer.parseInt(st.nextToken());
		}
		
		// Input End
		br.close();
		
		// Solve : DP
		int[][] dp = new int[n][n];
		for (int i = 0; i < n; i++) {
			Arrays.fill(dp[i], Integer.MAX_VALUE / 2);
			dp[i][i] = 0;
		}
		
		for (int size = 2; size <= n; size++) {
			for (int i = 0; i < n - size + 1; i++) {
				for (int j = i + 1; j < i + size; j++) {
					dp[i][i+size-1] = Math.min(dp[i][i+size-1], dp[i][j-1] + dp[j][i+size-1] + (matrix[i][0] * matrix[j][0] * matrix[i+size-1][1]));
				}
			}
		}
		
		
		int result = dp[0][n-1];
		
		// Output Start
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		bw.write(result + "\n");
		bw.flush();
		
		// Output End
		bw.close();
	}
}