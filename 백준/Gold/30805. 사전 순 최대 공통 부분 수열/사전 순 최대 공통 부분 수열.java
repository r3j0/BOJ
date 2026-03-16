import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        // Input Start
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] arrA = new int[n];
        for (int i = 0; i < n; i++) {
            arrA[i] = Integer.parseInt(st.nextToken());
        }

        int m = Integer.parseInt(br.readLine());

        st = new StringTokenizer(br.readLine());
        int[] arrB = new int[m];
        for (int i = 0 ; i < m; i++) {
            arrB[i] = Integer.parseInt(st.nextToken());
        }

        // Input End
        br.close();

        // Solve : Greedy
        // 판별 기준은 "숫자가 더 큼" 이 남아야 한다.
        ArrayList<int[]> now = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (arrA[i] == arrB[j]) {
                    // 숫자가 더 큰게 있다면 무조건 그걸로 밀어버린다.
                    // 같은 숫자면, 좌측을 남겨야 한다.
                    int backIdx = now.size() - 1;
                    while (backIdx >= 0 && now.get(backIdx)[0] < arrA[i]) {
                        backIdx -= 1;
                    }

                    if (backIdx < 0 || (now.get(backIdx)[1] < i && now.get(backIdx)[2] < j)) {
                        for (int k = now.size() - 1; k > backIdx; k--) {
                            now.remove(k);
                        }
                        now.add(new int[]{arrA[i], i, j});
                    }
                }
            }
        }

        // Output Start
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(now.size() + "\n");
        for (int[] e : now) {
            bw.write(e[0] + " ");
        }
        bw.flush();

        // Output End
        bw.close();
    }
}