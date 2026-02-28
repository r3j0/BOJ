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
		
		int[][] dp = new int[aLen+1][bLen+1];
		int[][] bt = new int[aLen+1][bLen+1]; // 1 : 대각선에서 옴 2 : 위쪽에서 옴 3 : 왼쪽에서 옴 
		
		// LCS DP
		for (int i = 1; i <= aLen; i++) {
			for (int j = 1; j <= bLen; j++) {
				if (a.charAt(i-1) == b.charAt(j-1)) { // 1. 대각선에서 옴
					dp[i][j] = dp[i-1][j-1] + 1;
					bt[i][j] = 1;
				}
				else if (dp[i-1][j] > dp[i][j-1]) { // 2. 위쪽에서 옴
					dp[i][j] = dp[i-1][j];
					bt[i][j] = 2;
				}
				else { // 3. 왼쪽에서 옴
					dp[i][j] = dp[i][j-1];
					bt[i][j] = 3;
				}
					
			}
		}
		
		int result = dp[aLen][bLen];
		
		StringBuilder resultString = new StringBuilder();
		
		int[] now = new int[]{aLen, bLen};
		int[] dx = new int[]{0, -1, -1, 0};
		int[] dy = new int[]{0, -1, 0, -1};
		while (now[0] != 0 && now[1] != 0) {
			int dir = bt[now[0]][now[1]];
			
			if (dir == 1) 
				resultString.append(a.charAt(now[0]-1));
			
			now[0] += dx[dir];
			now[1] += dy[dir];
		}
		resultString = resultString.reverse();
		
		// Output Start
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		bw.write(result + "\n" + resultString);
		bw.flush();
		
		// Output End
		bw.close();
	}
}