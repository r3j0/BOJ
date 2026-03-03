import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
	public static void main(String[] args) throws IOException {
		// Input Start
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		int[] inorder = new int[n+1];
		ArrayList<ArrayList<Integer>> edges = new ArrayList<>();
		for (int i = 0; i <= n; i++) {
			edges.add(new ArrayList<>());
		}
		
		while (m-- > 0) {
			st = new StringTokenizer(br.readLine());
			
			int p = Integer.parseInt(st.nextToken());
			int prev = -1;
			while (p-- > 0) {
				int x = Integer.parseInt(st.nextToken());
				if (prev != -1) {
					edges.get(prev).add(x);
					inorder[x] += 1;
				}
				prev = x;
			}
		}
		
		// Input End
		br.close();
		
		// Solve
		Queue<Integer> q = new LinkedList<>();
		for (int i = 1; i <= n; i++) {
			if (inorder[i] == 0) {
				q.offer(i);
			}
		}
		
		ArrayList<Integer> ans = new ArrayList<>();
		
		while(!q.isEmpty()) {
			int now = q.poll();
			
			ans.add(now);
			for (int next : edges.get(now)) {
				inorder[next] -= 1;
				if (inorder[next] == 0) {
					q.offer(next);
				}
			}
		}
		
		// Output Start
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		if (ans.size() == n) {
			for (int a : ans) {
				bw.write(a + "\n");
			}
		}
		else {
			bw.write("0");
		}
		bw.flush();
		
		// Output End
		bw.close();
	}
}