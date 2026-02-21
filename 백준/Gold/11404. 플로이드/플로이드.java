import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	public static final int MAX = Integer.MAX_VALUE / 2;
	
	public static void main(String[] args) throws IOException {
		// Input Start
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		int m = Integer.parseInt(br.readLine());
		
		int[][] dp = new int[n+1][n+1];
		for (int i = 1; i <= n; i++) {
			Arrays.fill(dp[i], MAX);
			dp[i][i] = 0;
		}
		
		StringTokenizer st;
		while (m-- > 0) {
			st = new StringTokenizer(br.readLine());
			int u = Integer.parseInt(st.nextToken());
			int v = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			
			dp[u][v] = Math.min(dp[u][v], c);
		}
		
		// Input End
		br.close();
		
		// Solve
		for (int k = 1; k <= n; k++) {
			for (int i = 1; i <= n; i++) {
				for (int j = 1; j <= n; j++) {
					dp[i][j] = Math.min(dp[i][j], dp[i][k] + dp[k][j]);
				}
			}
		}
		
		// Output Start
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= n; j++) {
				bw.write(Integer.toString((dp[i][j] == MAX) ? 0 : dp[i][j]));
				
				if (j < n) bw.write(" ");
			}
			bw.write("\n");
		}
		
		bw.flush();
		
		// Output End
		bw.close();
	}
}