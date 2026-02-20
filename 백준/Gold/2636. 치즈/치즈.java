import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
	public static class Point {
		int x;
		int y;
		
		public Point (int x, int y) {
			this.x = x;
			this.y = y;
		}
	}
	
	public static void main(String[] args) throws IOException {
		// Input Start
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		boolean[][] board = new boolean[n][m];
		int cheese = 0;
		
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < m; j++) {
				if (Integer.parseInt(st.nextToken()) == 1) {
					board[i][j] = true;
					cheese += 1;
				}
			}
		}
		
		// Input End
		br.close();
		
		// Solve
		int time = 0;
		int last = cheese;
		
		int[] dx = new int[]{-1, 1, 0, 0};
		int[] dy = new int[]{0, 0, -1, 1};
		
		Queue<Point> queue_cheese = new LinkedList<>();
		Queue<Point> queue_air = new LinkedList<>();
		boolean[][] visited = new boolean[n][m];
		
		queue_air.add(new Point(0, 0));
		visited[0][0] = true;
		
		
		while (cheese > 0) {
			last = cheese;
			
			// Air BFS
			while(!queue_air.isEmpty()) {
				Point now = queue_air.poll();
				
				for (int d = 0; d < 4; d++) {
					int nx = now.x + dx[d];
					int ny = now.y + dy[d];
					
					if (0 <= nx && nx < n && 0 <= ny && ny < m && (!visited[nx][ny])) {
						visited[nx][ny] = true;
						
						if (board[nx][ny]) {
							queue_cheese.add(new Point(nx, ny));
						}
						else { 
							queue_air.add(new Point(nx, ny));
						}
					}
				}
			}
			
			// Cheese BFS
			int s = queue_cheese.size();
			while (s-- > 0) {
				Point now = queue_cheese.poll();
				
				cheese -= 1;
				board[now.x][now.y] = false;
				
				for (int d = 0; d < 4; d++) {
					int nx = now.x + dx[d];
					int ny = now.y + dy[d];
					
					if (0 <= nx && nx < n && 0 <= ny && ny < m && (!visited[nx][ny])) {
						visited[nx][ny] = true;
						
						if (board[nx][ny]) {
							queue_cheese.add(new Point(nx, ny));
						}
						else { 
							queue_air.add(new Point(nx, ny));
						}
					}
				}
			}
			
			time += 1;
		}
		
		
		// Output Start
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		bw.write(time + "\n");
		bw.write(last + "\n");
		bw.flush();
		
		// Output End
		bw.close();
	}
}