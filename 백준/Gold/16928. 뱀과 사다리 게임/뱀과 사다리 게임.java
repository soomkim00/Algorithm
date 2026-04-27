import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken()), M = Integer.parseInt(st.nextToken());
        int[] jump = new int[101];
        for(int i = 1; i <= 100; i++) jump[i] = i;
        for(int i = 0; i < N + M; i++) {
            st = new StringTokenizer(br.readLine());
            jump[Integer.parseInt(st.nextToken())] = Integer.parseInt(st.nextToken());
        }
        int[] dist = new int[101];
        Arrays.fill(dist, -1);
        Queue<Integer> q = new LinkedList<>();
        q.add(1);
        dist[1] = 0;
        while(!q.isEmpty()) {
            int cur = q.poll();
            if(cur == 100) break;
            for(int i = 1; i <= 6; i++) {
                int next = cur + i;
                if(next <= 100) {
                    next = jump[next];
                    if(dist[next] == -1) {
                        dist[next] = dist[cur] + 1;
                        q.add(next);
                    }
                }
            }
        }
        System.out.println(dist[100]);
    }
}