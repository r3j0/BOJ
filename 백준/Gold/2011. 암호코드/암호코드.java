import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class Main {
	public static void main(String[] args) throws IOException {
		// Input Start
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String s = br.readLine();
		
		// Input End
		br.close();
		
		// Solve : DP
		int len = s.length();
		int[] dp = new int[len+1];
		dp[0] = 1;
		
		
		for (int i = 1; i <= len; i++) {
			if (i >= 2) {
				int now = Integer.parseInt(s.substring(i-2, i));
				if (10 <= now && now <= 26) dp[i] = (dp[i] + dp[i-2]) % 1000000;
			}
			if (Integer.parseInt(s.substring(i-1, i)) != 0) {
				dp[i] = (dp[i] + dp[i-1]) % 1000000;
			}
		}
		
		int answer = dp[len]; 
		
		// Output Start
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		bw.write(answer + "\n");
		bw.flush();
		
		// Output End
		bw.close();
	}
}