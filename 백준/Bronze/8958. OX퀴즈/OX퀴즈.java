import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            String s = br.readLine();
            int result = 0, temp = 0;

            for (char c : s.toCharArray()) {
                if (c == 'O') {
                    temp++;
                    result += temp;
                } else {
                    temp = 0;
                }
            }

            System.out.println(result);
        }
    }
}