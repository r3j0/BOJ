// 1253 : 좋다
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
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

        // Solve : Two Pointer
        int answer = 0;

        Arrays.sort(arr);
        for (int i = 0; i < n; i++) {
            int left = 0;
            int right = n - 1;

            while (left < right) {
                if (left == i) {
                    left += 1;
                    continue;
                }
                if (right == i) {
                    right -= 1;
                    continue;
                }
                
                int now = arr[left] + arr[right];
                if (now == arr[i]) {
                    answer += 1;
                    break;
                }

                if (now < arr[i]) left += 1;
                else if (now > arr[i]) right -= 1;
            }
        }

        // Output Start
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(answer + "\n");
        bw.flush();

        // Output End
        bw.close();
    }
}