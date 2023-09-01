import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int h = sc.nextInt();
        int m = sc.nextInt();

        int result = h * 60 + m - 45;
        if (result < 0) result += 1440;

        System.out.println((result / 60) + " " + (result % 60));
    }
}