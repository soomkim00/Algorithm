import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int H = Integer.parseInt(st.nextToken());
            int W = Integer.parseInt(st.nextToken());
            int N = Integer.parseInt(st.nextToken());

            // 수정된 부분 시작
            int floor = N % H;
            int line;
            if (floor == 0) {
                floor = H;          // 꼭대기층
                line  = N / H;      // 몫 그대로
            } else {
                line  = N / H + 1;  // 나머지 있으면 몫+1
            }
            String yy = Integer.toString(floor);
            String xx = (line >= 10) ? Integer.toString(line) : "0" + line;
            String s = yy + xx;
            // 수정된 부분 끝

            System.out.println(s);
        }
    }
}
