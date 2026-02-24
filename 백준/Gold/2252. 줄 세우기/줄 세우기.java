import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
import java.util.List;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Arrays;
import java.lang.StringBuilder;

public class Main {
	public static void main(String[] args) throws IOException {
		// Input Start
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		int[] inorder = new int[n+1];
		ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
		for (int i = 0; i <= n; i++) {
			graph.add(new ArrayList<>());
		}
		
		while (m-- > 0) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			
			inorder[b] += 1;
			graph.get(a).add(b);
		}
		
		// Input End
		br.close();
		
		// Solve
		Queue<Integer> q = new LinkedList<>();
		for (int i = 1; i <= n; i++) {
			if (inorder[i] == 0) {
				q.add(i);
			}
		}
		
		StringBuilder result = new StringBuilder();
		int cnt = 0;
		while(!q.isEmpty()) {
			int now = q.poll();
			cnt += 1;
			result.append(Integer.toString(now) + (cnt < n ? " " : ""));
			
			for (int next : graph.get(now)) {
				inorder[next] -= 1;
				if (inorder[next] == 0) {
					q.add(next);
				}
			}
		}
		
		// Output Start
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		bw.write(result.toString());
		bw.flush();
		
		// Output End
		bw.close();
	}
}