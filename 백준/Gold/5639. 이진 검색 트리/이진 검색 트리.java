// 5639 : 이진 검색 트리
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;

public class Main {
    public static ArrayList<Integer> a;
    public static ArrayList<Integer> ans;
    public static void main(String[] args) throws IOException {
        // Input Start
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        a = new ArrayList<>();
        ans = new ArrayList<>();
        String input;
        while ((input = br.readLine()) != null) {
            if (input.equals("")) break;
            a.add(Integer.parseInt(input));
        }

        // Input End
        br.close();

        // Solve
        // 첫 번째 노드를 중심으로 잡고, 작은 것들 왼쪽 큰 것들 오른쪽 분할
        // 이후 그래프 후위탐색
        solve(0, a.size() - 1);

        // Output Start
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        for (int i : ans) bw.write(i + "\n");
        bw.flush();

        // Output End
        bw.close();
    }

    public static void solve(int left, int right) {
        if (left > right) return;
        if (left < right) {
            int mid = left + 1;
            while (mid <= right && a.get(mid) < a.get(left)) mid += 1;

            solve(left + 1, mid - 1);
            solve(mid, right);
        }
        ans.add(a.get(left));
    }
}