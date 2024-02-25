import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine().toUpperCase();	//str : 입력받은 문자를 대문자로 저장
		int[] count = new int[26];	//count[] : 사용한 문자 갯수를 담을 배열
		Arrays.fill(count, 0);
		int Max = 0;	//Max : 가장 많은 문자를 쓴 갯수
		
		for (int i = 0; i < str.length(); i++) {
            count[((int)(str.charAt(i)) - 65) % 32]++;
            Max = Math.max(Max, count[((int)(str.charAt(i)) - 65) % 32]);
        }

		int sum = 0;	//가장 많이 사용한 문자 종류 수
		int index = 0;	//가장 많이 사용한 문자 인덱스
		for (int i = 0; i < 26; i++) {
			if (Max==count[i]) {
				sum++;
				index = i;
			}	//sum, index 완성
        }
		
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		if (sum == 1)	//sum이 1이면 가장 많이 사용한 알파벳을, 2 이상이면 ?출력
			bw.write(index + 'A');
		else
			bw.write("?");
		bw.close();
	}
}