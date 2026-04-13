// 12738 : 가장 긴 증가하는 부분 수열 3
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        // Input Start
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        // Input End
        br.close();

        // Solve : LIS Binary Search
        int[] ans = new int[n];
        int top = 0;

        for (int i = 0; i < n; i++) {
            // lower_bound
            int start = 0;
            int end = top;
            while (start < end) {
                int mid = (start + end) / 2;
                if (ans[mid] >= arr[i]) {
                    end = mid;
                }
                else {
                    start = mid + 1;
                }
            }

            if (top == start) ans[top++] = arr[i];
            else ans[start] = arr[i];
        }

        // Output Start
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(top + "\n");
        bw.flush();

        // Output End
        bw.close();
    }
}