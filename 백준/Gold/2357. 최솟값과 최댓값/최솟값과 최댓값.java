// 2357 : 최솟값과 최댓값
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
    public static int[] arr;
    public static int[][] tree;

    public static int[] NONE = {Integer.MAX_VALUE, 0};

    public static void main(String[] args) throws IOException {
        // Input Start
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        arr = new int[n];
        tree = new int[n*4][2];

        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        int[][] query = new int[m][2];
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 2; j++) {
                query[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        // Input End
        br.close();

        // Solve : Segment Tree
        build(0, n - 1, 1); // 1. 세그먼트 트리 생성
        for (int i = 0; i < m; i++) { // 2. 쿼리마다 구간 최솟값, 최댓값 찾기
            int left = query[i][0] - 1;
            int right = query[i][1] - 1;

            query[i] = solve(0, n - 1, 1, left, right);
        }

        // Output Start
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        for (int i = 0; i < m; i++) {
            bw.write(query[i][0] + " " + query[i][1] + "\n");
        }
        bw.flush();

        // Output End
        bw.close();
    }

    public static void build(int start, int end, int idx) {
        if (start == end) {
            for (int i = 0; i < 2; i++) {
                tree[idx][i] = arr[start];
            }
            return;
        }

        int mid = (start + end) / 2;
        build(start, mid, idx * 2);
        build(mid + 1, end, idx * 2 + 1);

        // 최솟값 갱신
        tree[idx][0] = Math.min(tree[idx * 2][0], tree[idx * 2 + 1][0]);
        // 최댓값 갱신
        tree[idx][1] = Math.max(tree[idx * 2][1], tree[idx * 2 + 1][1]);
    }

    public static int[] solve(int start, int end, int idx, int left, int right) {
        if (end < left || right < start) return NONE;
        if (left <= start && end <= right) return tree[idx];

        int mid = (start + end) / 2;
        int[] leftv = solve(start, mid, idx * 2, left, right);
        int[] rightv = solve(mid + 1, end, idx * 2 + 1, left, right);

        return new int[]{Math.min(leftv[0], rightv[0]), Math.max(leftv[1], rightv[1])};
    }
}