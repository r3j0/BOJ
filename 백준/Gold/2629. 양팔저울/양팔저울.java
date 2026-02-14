import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
	static int MAX_BEAD_WEIGHT = 40000; 
	public static void main(String[] args) throws IOException {
		// Input 시작
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		// 추의 개수 n 입력
		int n = Integer.parseInt(br.readLine());
		
		// 추들의 무게 입력
		int[] weights = new int[n+1];
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 0; i < n; i++)
			weights[i] = Integer.parseInt(st.nextToken());
		
		// 구슬의 개수 k 입력
		int k = Integer.parseInt(br.readLine());
		
		// 구슬들의 무게 입력
		int[] beads = new int[k+1];
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < k; i++)
			beads[i] = Integer.parseInt(st.nextToken());
		
		// Input 종료
		br.close();
		
		// Knapsack DP : 추들을 더하거나 뺐을 때 특정 구슬의 무게를 얻을 수 있는가?
		boolean[] dp = new boolean[MAX_BEAD_WEIGHT*2]; 
		
		dp[0] = true;  // 구슬의 무게가 0인 경우는 얻을 수 있다.
		
		for (int weight = 0; weight < n; weight++) {
			for (int bead_weight = MAX_BEAD_WEIGHT; bead_weight >= 0; bead_weight--) {
				if (dp[bead_weight]) dp[bead_weight + weights[weight]] = true;
			}
			for (int bead_weight = 0; bead_weight <= MAX_BEAD_WEIGHT; bead_weight++) {
				if (dp[bead_weight]) dp[Math.abs(bead_weight - weights[weight])] = true;
			}
		}
		
		// Output 시작
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		// n번째 추까지 사용했을 때, 구슬 무게인 beads[i] 를 얻을 수 있는가?
		for (int i = 0; i < k; i++) {
			if (dp[beads[i]])
				bw.write("Y");
			else
				bw.write("N");
			
			if (i != k - 1)
				bw.write(" ");
		}
		bw.flush();
		
		// Output 종료
		bw.close();
	}
}
