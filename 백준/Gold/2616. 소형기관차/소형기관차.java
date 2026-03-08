import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		// Input Start
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		int[] arr = new int[n];
		for (int i = 0; i < n; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		int k = Integer.parseInt(br.readLine());
		
		// Input End
		br.close();
		
		// Solve : DP
		
		// 주요 아이디어 : 문제를 바꾸어 말하면, 길이가 k인 연속된 구간 3개를 사용하여
		// 최대한 배열 원소의 합이 크게 만드는 것이다.
		// 그리디로 접근했을 때 정해가 나오지 않을 확률이 있으므로,
		// ( 큰 원소만을 따라가면 더 작은 수를 선택할 수 있음 )
		// dp[i][j] : i번 객차까지 j개의 객차를 사용해서 최대 운송 가능한 손님 수
		// DP를 사용해서 최적해를 구해낸다.
		
		// 1. 배열 연속합을 빠르게 구하기 위한 누적합
		int[] sarr = new int[n+1];
		for (int i = 1; i <= n; i++) {
			sarr[i] = sarr[i-1] + arr[i-1];
		}
		
		int[][] dp = new int[n+1][4];
		
		for (int i = k; i <= n; i++) {
			for (int j = 1; j <= 3; j++) {
				dp[i][j] = Math.max(dp[i-1][j], dp[i-k][j-1] + (sarr[i] - sarr[i-k]));
			}
		}
		
		int result = dp[n][3];
		
		// Output Start
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		bw.write(result + "\n");
		bw.flush();
		
		// Output End
		bw.close();
	}
}