import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int arr[] = new int[42];
        int tmp;
        for (int i = 0; i < 10; i++) {
            tmp = sc.nextInt();
            arr[tmp % 42] += 1;
        }

        int cnt = 0;
        for (int i = 0; i < 42; i++) {
            if (arr[i] > 0) cnt += 1;
        }

        System.out.println(cnt);
    }
}