// 1806 : 부분합
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException{
        // Input Start
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        long s = Long.parseLong(st.nextToken());

        st = new StringTokenizer(br.readLine());
        long[] arr = new long[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Long.parseLong(st.nextToken());
        }

        // Input End
        br.close();

        // Solve

        ArrayList<Long> sarr = new ArrayList<>();
        sarr.add(0L);

        for (int i = 0; i < n; i++) {
            sarr.add(sarr.get(sarr.size() - 1) + arr[i]);
        }

        // sarr[i] - s 의 upper-bound
        int result = 0;
        for (int i = 1; i <= n; i++) {
            if (sarr.get(i) < s) continue;

            long key = sarr.get(i) - s;
            int start = 0;
            int end = i - 1;
            int ans = i;
            while (start <= end) {
                int mid = (start + end) / 2;
                if (key >= sarr.get(mid)) {
                    ans = mid;
                    start = mid + 1;
                }
                else {
                    end = mid - 1;
                }
            }

            if (ans != i && (result == 0 || result > i - ans)) {
                result = i - ans;
            }
        }

        // Output Start
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(result + "\n");
        bw.flush();

        // Output End
        bw.close();
    }
}