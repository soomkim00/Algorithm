import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        long[] prefix = new long[N];
        st = new StringTokenizer(br.readLine());
        prefix[0] = Long.parseLong(st.nextToken());
        for (int i = 1; i < N; i++) {
            prefix[i] = prefix[i - 1] + Long.parseLong(st.nextToken());
        }

        StringBuilder sb = new StringBuilder();
        for (int q = 0; q < M; q++) {
            st = new StringTokenizer(br.readLine());
            int i = Integer.parseInt(st.nextToken());
            int j = Integer.parseInt(st.nextToken());

            int leftIdx = i - 2;   // Python의 i-2
            int rightIdx = j - 1;  // Python의 j-1

            if (leftIdx < 0) {
                sb.append(prefix[rightIdx]).append('\n');
            } else {
                sb.append(prefix[rightIdx] - prefix[leftIdx]).append('\n');
            }
        }

        System.out.print(sb.toString());
    }
}
