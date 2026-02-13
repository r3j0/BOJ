import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
import java.util.ArrayList;
import java.util.List;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    public static void main(String[] args) throws IOException {
	    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        // 노드 개수 n 입력받기
        int n = Integer.parseInt(st.nextToken());

        // n 개에 노드에 연결된 다른 노드들에 대한 정보 배열
        ArrayList<ArrayList<Integer>> edges = new ArrayList<>();
        for (int i = 0; i < n + 1; i++) {
            edges.add(new ArrayList<>());
        }

        // n - 1 개의 간선 정보를 양방향으로 저장
        for (int i = 0; i < n - 1; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            
            edges.get(u).add(v);
            edges.get(v).add(u);
        }

        // BFS 를 위한 큐 선언. 시작 노드 1 추가.
        Queue<Integer> q = new LinkedList<>();
        q.add(1);

        // 방문 여부 확인 배열에 [해당 노드를 방문한 부모 노드] 기록
        int[] visited = new int[n + 1];

        // BFS
        while (!q.isEmpty()) {
            int now = q.poll();

            for (int v : edges.get(now)) {
                if (visited[v] == 0) {
                    q.add(v);
                    visited[v] = now;
                }
            }
        }

        // 1번 노드를 제외한 노드들의 부모 노드 출력
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        for (int i = 2; i <= n; i++) {
            bw.write(visited[i] + "\n");
        }
        
        bw.flush();
        bw.close();
    }
}