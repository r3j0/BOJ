import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
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
		
		// Input End
		br.close();
		
		// Solve : LIS with Binary Search
		int[] dp = new int[n];
		int right = 0;
		
		for (int i = 0; i < n; i++) {
			int idx = lower_bound(dp, right, arr[i]);
			right = Math.max(right, idx + 1);
			
			dp[idx] = arr[i];
		}
		
		// Output Start
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		bw.write(right + "\n");
		bw.flush();
		
		// Output End
		bw.close();
		
	}
	
	public static int lower_bound(int[] dp, int r, int k) {
		int l = 0;
		while (l < r) {
			int mid = (l + r) / 2;
			
			if (dp[mid] >= k) r = mid;
			else l = mid + 1;
		}
		
		return l;
	}
}
