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
		
		long a = Long.parseLong(st.nextToken());
		long b = Long.parseLong(st.nextToken());
		long c = Long.parseLong(st.nextToken());
		
		// Input End
		br.close();
		
		// Solve
		long result = mul(a, b, c);
		
		// Output Start
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		bw.write(result + "\n");
		bw.flush();
		
		// Output End
		bw.close();
	}
	
	public static long mul(long a, long b, long c) {
		if (b == 1) return a % c;
		long x = mul(a, b/2, c);
		
		if (b % 2 == 0) return (x * x) % c;
		return (((x * x) % c) * a) % c;
		
	}
}