import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        // Input Start
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        ArrayList<Integer> plus = new ArrayList<>();
        ArrayList<Integer> minus = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            int now = Integer.parseInt(st.nextToken());
            if (now > 0) plus.add(now);
            else minus.add(-now);
        }
        Collections.sort(plus);
        Collections.sort(minus);

        // Input End
        br.close();

        // Solve : Binary Search
        int[] answer = new int[2];
        for (int i = 0; i < 2; i++) {
            answer[i] = Integer.MAX_VALUE / 2;
        }

        // 1. 플러스 요소 중 가장 절댓값 작은 2개
        if (plus.size() > 1) {
            check(answer, plus.get(0), plus.get(1));
        }

        // 2. 마이너스 요소 중 가장 절댓값 작은 2개
        if (minus.size() > 1) {
            check(answer, -minus.get(0), -minus.get(1));
        }

        // 3. 플러스 요소 차례대로 지정 -> 마이너스 요소 이분 탐색
        boolean done = false;
        for (int p : plus) {
            int start = 0;
            int end = minus.size() - 1;
            while (start < end) {
                int mid = (start + end) / 2;
                if (minus.get(mid) < p) {
                    start = mid + 1;
                }
                else if (minus.get(mid) > p) {
                    end = mid - 1;
                }
                else {
                    check(answer, -minus.get(mid), p);
                    done = true;
                    break;
                }
            }

            if (done) break;

            for (int i = -1; i <= 1; i++) {
                if (start + i < 0 || minus.size() <= start + i) continue;
                check(answer, -minus.get(start + i), p);
            }
        }

        // Output Start
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(answer[0] + " " + answer[1] + "\n");
        bw.flush();

        // Output ENd
        bw.close();
    }

    public static void check(int[] answer, int first, int second) {
        if (Math.abs(answer[0] + answer[1]) > Math.abs(first + second)) {
            answer[0] = Math.min(first, second);
            answer[1] = Math.max(first, second);
        }
    }
}