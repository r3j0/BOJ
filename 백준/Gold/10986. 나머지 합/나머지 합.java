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
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		int[] arr = new int[n];
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < n; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		// Input End 
		br.close();
		
		// Solve : prefix sum
		
		// 1. 누적합 배열을 만든다.
		int[] sarr = new int[n+1];
		for (int i = 1; i <= n; i++) {
			sarr[i] = (sarr[i-1] + arr[i-1]) % m;
		}
		
		// 2. 누적합들을 M으로 나눈 나머지를 기록할 수 있는 배열을 만든다.
		int[] rmd = new int[m];
		rmd[0] = 1;
		
		// 3. 	(i, j) 쌍이 M으로 나누어 떨어지려면,
		//		sarr[j] - sarr[i] 가 M으로 나누어 떨어지면 되고,
		//		즉, sarr[j] % M 과 sarr[i] % M 가 같으면 된다.
		//		rmd 배열을 이용해 같은 나머지를 가진 누적합들이 있다면
		//		그 개수를 정답에 카운트하면 된다.
		long result = 0;
		for (int i = 1; i <= n; i++) {
			result += rmd[sarr[i]];
			rmd[sarr[i]] += 1;
		}
		
		// Output Start
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		bw.write(result + "\n");
		bw.flush();
		
		// Output End
		bw.close();
	}
}