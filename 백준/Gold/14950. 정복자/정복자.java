import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Stack;

public class Main {
	public static void main(String[] args) throws IOException {
		// Input Start
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		int t = Integer.parseInt(st.nextToken());
		
		ArrayList<int[]> edges = new ArrayList<>();
		while (m-- > 0) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			
			edges.add(new int[]{a, b, c});
		}
		
		// Input End
		br.close();
		
		// Solve
		Collections.sort(edges, (a, b) -> a[2] - b[2]);
		int[] parent = new int[n+1];
		for (int i = 1; i <= n; i++) {
			parent[i] = i;
		}
		
		int result = t * ((n - 2) * (n - 1) / 2);
		for (int[] e : edges) {
			if (union(parent, e[0], e[1])) {
				result += e[2];
			}
		}
		
		// Output Start
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		bw.write(result + "\n");
		bw.flush();
		
		// Output End
		bw.close();
	}
	
	public static int find(int[] parent, int a) {
		Stack<Integer> s = new Stack<>();
		int now = a;
		while (now != parent[now]) {
			s.push(now);
			now = parent[now];
		}
		
		int res = now;
		while (!s.isEmpty()) {
			int x = s.pop();
			parent[x] = res;
		}
		
		return res;
	}
	
	public static boolean union(int[] parent, int a, int b) {
		a = find(parent, a);
		b = find(parent, b);
		
		if (a == b) return false;
		
		if (a > b) {
			int tmp = a;
			a = b;
			b = tmp;
		}
		
		parent[b] = a;
		return true;
	}
}