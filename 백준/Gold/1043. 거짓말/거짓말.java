import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
import java.util.List;
import java.util.ArrayList;
import java.util.Stack;

public class Main {
    // 사람들의 그룹 번호 (어디 그룹에 속해있는지) 를 기록하는 parent 배열
    public static int[] parent;
    
    public static void main(String[] args) throws IOException {
        // Input Start
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        // [입력] 사람의 수 N, 파티의 수 M
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        parent = new int[n+1];
        for (int i = 1; i <= n; i++) { 
            parent[i] = i; // 초기 그룹 번호는 자기 자신
        }

        // [입력] 이야기의 진실을 아는 사람 수와 번호
        st = new StringTokenizer(br.readLine());
        int k = Integer.parseInt(st.nextToken());
        while (k-- > 0) {
            // 진실을 아는 사람은 모두 0번 그룹 (이후 이 사람들과 union 한다면 0번으로 갱신됨)
            parent[Integer.parseInt(st.nextToken())] = 0; 
        }

        // 각 파티마다 오는 사람의 번호를 기록하는 parties ArrayList 선언
        ArrayList<ArrayList<Integer>> parties = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            parties.add(new ArrayList<>());

            // [입력] i번 파티에 오는 사람의 수와 번호
            st = new StringTokenizer(br.readLine());
            int p = Integer.parseInt(st.nextToken());
            while (p-- > 0) {
                parties.get(i).add(Integer.parseInt(st.nextToken()));
            }
        }

        // Input End
        br.close();

        
        // Solve
        int result = 0; 

        // 각 파티의 참여자들은 각 파티의 0번째 사람과 union 을 수행한다. 
        for (int i = 0; i < m; i++) {
            for (int j = 1; j < parties.get(i).size(); j++) {
                union(parties.get(i).get(0), parties.get(i).get(j));
            }
        }

        // 각 파티의 0번째 사람이 진실을 아는 그룹이 아니라면 (0번 그룹이 아니라면) result += 1
        for (int i = 0; i < m; i++) {
            if (find(parties.get(i).get(0)) > 0) 
                result += 1;
        }
        
        // Output Start
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(result + "\n");
        bw.flush();

        // Output End
        bw.close();
    }

    // 두 그룹 번호를 union
    public static void union(int a, int b) {
        a = find(a);
        b = find(b);

        // 작은 번호의 그룹을 우선시 한다. (0번 그룹을 위해)
        if (a > b) {
            int tmp = a;
            a = b;
            b = tmp;
        }
        
        parent[b] = a;
    }

    // 특정 사람이 속한 그룹의 root를 구하는 find
    public static int find(int a) {
        if (parent[a] == a) return a;

        // 재귀 연산 대신 Stack 을 활용한 비재귀 find 구현
        Stack<Integer> s = new Stack<>();
        while (parent[a] != a) {
            s.push(a);
            a = parent[a];
        }

        // root를 a로 구했다면, 지나왔던 그룹 번호 또한 root 로 갱신
        while (!s.isEmpty()) {
            parent[s.pop()] = a;
        }
        
        return a;
    }
}