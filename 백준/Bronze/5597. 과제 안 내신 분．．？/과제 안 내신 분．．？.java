import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int arr[] = new int[31];
        int num;
        for (int idx = 0; idx < 28; idx++) {
            num = sc.nextInt();
            arr[num] = 1;
        }

        for (int idx = 1; idx <= 30; idx++) {
            if (arr[idx] == 0) System.out.println(idx);
        }
    }
}