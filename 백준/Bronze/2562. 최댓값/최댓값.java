import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int result = 0;
        int idx = 0;
        for (int i=0; i<9; i++) {
            int temp = Integer.parseInt(br.readLine());
            if (temp > result) {
                result = temp;
                idx = i+1;
            }
        }
        System.out.println(result);
        System.out.println(idx);
    }
}
