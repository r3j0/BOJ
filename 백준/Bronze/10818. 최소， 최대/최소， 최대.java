import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int min_value = 1000001;
        int max_value = -1000001;

        int tmp;
        for (int i = 0; i < n; i++) {
            tmp = sc.nextInt();
            if (tmp < min_value) min_value = tmp;
            if (tmp > max_value) max_value = tmp;
        }

        System.out.println(min_value + " " + max_value);
    }
}