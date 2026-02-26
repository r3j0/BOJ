import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
	static int n;
	static int m;
	static int[][] arr;
	static int[][] dp;
	static boolean[][] vis;
	public static void main(String[] args) throws IOException {
		// Input Start
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		
		arr = new int[n][m];
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < m; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		// Input End
		br.close();
		
		// Solve
		// 주요 아이디어 : 	브루트포스로 경로를 다 탐색할 수 없다. 
		// 				따라서 현재 칸이 이미 목표 지점까지 갔던 기록이 있다면 바로 카운트하고 스킵한다.
		//				DFS 로 먼저 경로 하나를 먼저 탐색하고, DP 배열에 여길 지나온 경로의 수를 기록한다.
		//					dp[i][j] = (i, j) 부터 목표 지점까지 갔던 경로의 수
		
		dp = new int[n][m];
		vis = new boolean[n][m];
		int result = dfs(0, 0);
		
		// Output Start
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		bw.write(result + "\n");
		bw.flush();
		
		// Output End
		bw.close();
	}
	
	static int[] dy = {-1, 1, 0, 0};
	static int[] dx = {0, 0, -1, 1};
	public static int dfs(int y, int x) {
		vis[y][x] = true;
		if (y == n - 1 && x == m - 1) return dp[y][x] = 1;
		
		int cnt = 0;
		for (int d = 0; d < 4; d++) {
			int ny = y + dy[d];
			int nx = x + dx[d];
			
			if (0 > ny || ny >= n || 0 > nx || nx >= m) continue;
			if (arr[y][x] <= arr[ny][nx]) continue;
			if (vis[ny][nx]) {
				cnt += dp[ny][nx];
				continue;
			}
			
			cnt += dfs(ny, nx);
			
		}
		
		return dp[y][x] = cnt;
	}
}