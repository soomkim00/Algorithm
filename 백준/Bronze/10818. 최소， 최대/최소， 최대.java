import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int min_val = Integer.MAX_VALUE;
        int max_val = Integer.MIN_VALUE;

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            int temp = Integer.parseInt(st.nextToken());
            if (temp < min_val) {
                min_val = temp;
            }
            if (temp > max_val) {
                max_val = temp;
            }
        }

        System.out.printf("%d %d", min_val, max_val);

    }
}
