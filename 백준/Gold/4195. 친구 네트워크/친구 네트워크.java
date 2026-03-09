import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
import java.util.Map;
import java.util.HashMap;
import java.util.Stack;

public class Main {
	public static void main(String[] args) throws IOException {
		// Input - Output Start
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out)); 
		
		int t = Integer.parseInt(br.readLine());
		while (t-- > 0) {
			int f = Integer.parseInt(br.readLine());
			
			StringTokenizer st;
			Map<String, Integer> names = new HashMap<>();
			int[] parent = new int[f * 2 + 1];
			int[] groups = new int[f * 2 + 1];
			int top = 0;
			
			for (int i = 0; i < f * 2 + 1; i++) {
				parent[i] = i;
			}
			
			while(f-- > 0) {
				st = new StringTokenizer(br.readLine());
				
				String[] name = new String[2];
				int[] keys = new int[2];
				for (int i = 0; i < 2; i++) {
					name[i] = st.nextToken();
					
					if (!names.containsKey(name[i])) {
						keys[i] = top;
						names.put(name[i], top);
						groups[top++] = 1;
					}
					else {
						keys[i] = names.get(name[i]);
					}
				}
				
				if(find(parent, keys[0]) != find(parent, keys[1])) {
					union(parent, groups, keys[0], keys[1]);
				}
				
				bw.write(groups[find(parent, keys[0])] + "\n");
			}
		}
		
		bw.flush();
		
		// Input - Output End
		br.close();
		bw.close();
	}
	
	public static int find(int[] parent, int a) {
		Stack<Integer> s = new Stack<>();
		int now = a;
		while (now != parent[now]) {
			s.push(now);
			now = parent[now];
		}
		
		while (!s.isEmpty()) {
			int g = s.pop();
			parent[g] = now;
		}
		
		return now;
	}
	
	public static void union(int[] parent, int[] groups, int a, int b) {
		a = find(parent, a);
		b = find(parent, b);
		
		if (a > b) {
			int tmp = a;
			a = b;
			b = tmp;
		}
		
		parent[b] = a;
		groups[a] += groups[b];
		groups[b] = 0;
	}
}