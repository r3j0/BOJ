import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
public class Main {
	public static void main(String[] args) throws IOException {
		// Input Start
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String a = br.readLine();
		String b = br.readLine();
		
		// Input End
		br.close();
		
		// Solve
		int aLen = a.length();
		int bLen = b.length();
		
		int[][] dp = new int[aLen + 1][bLen + 1];
		
		// LCS DP
		for (int i = 1; i <= aLen; i++) {
			for (int j = 1; j <= bLen; j++) {
				dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
				
				if (a.charAt(i-1) == b.charAt(j-1)) {
					dp[i][j] = Math.max(dp[i][j], dp[i-1][j-1] + 1);
				}
			}
		}
		
		int result = dp[aLen][bLen];
		
		// Output Start
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		bw.write(result + "\n");
		bw.flush();
		
		// Output End
		bw.close();
	}
}