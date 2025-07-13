import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String A = br.readLine();
        String B = br.readLine();
        int C = Integer.parseInt(br.readLine());

        int result1 = Integer.parseInt(A) + Integer.parseInt(B) - C;
        int result2 = Integer.parseInt(A + B) - C;
        System.out.println(result1);
        System.out.println(result2);
    }
}