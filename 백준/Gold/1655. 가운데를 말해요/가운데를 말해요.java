import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) throws IOException {
        // Input Start
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) 
            arr[i] = Integer.parseInt(br.readLine());

        // Input End
        br.close();

        // Solve
        int[] ans = new int[n];
        ans[0] = arr[0];
        
        PriorityQueue<Integer> leftq = new PriorityQueue<>();
        PriorityQueue<Integer> rightq = new PriorityQueue<>();
        rightq.add(arr[0]);

        for (int i = 1; i < n; i++) {
            if (rightq.peek() < arr[i]) {
                rightq.add(arr[i]);
                if (i % 2 == 1) leftq.add(-rightq.poll());
            }
            else {
                leftq.add(-arr[i]);
                if (i % 2 == 0) rightq.add(-leftq.poll());
            }

            if (i % 2 == 1) ans[i] = Math.min(-leftq.peek(), rightq.peek());
            else ans[i] = rightq.peek();
        }

        // Output Start
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        for (int a : ans) bw.write(a + "\n");
        bw.flush();
        bw.close();
    }
}