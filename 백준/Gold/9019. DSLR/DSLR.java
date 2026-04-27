import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        while(T-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());
            boolean[] vis = new boolean[10000];
            String[] path = new String[10000];
            Arrays.fill(path, "");
            Queue<Integer> q = new LinkedList<>();
            q.add(A);
            vis[A] = true;
            while(!q.isEmpty()) {
                int cur = q.poll();
                if(cur == B) {
                    sb.append(path[cur]).append("\n");
                    break;
                }
                int d = (cur * 2) % 10000;
                int s = cur == 0 ? 9999 : cur - 1;
                int l = (cur % 1000) * 10 + cur / 1000;
                int r = (cur % 10) * 1000 + cur / 10;
                
                if(!vis[d]) { vis[d] = true; path[d] = path[cur] + "D"; q.add(d); }
                if(!vis[s]) { vis[s] = true; path[s] = path[cur] + "S"; q.add(s); }
                if(!vis[l]) { vis[l] = true; path[l] = path[cur] + "L"; q.add(l); }
                if(!vis[r]) { vis[r] = true; path[r] = path[cur] + "R"; q.add(r); }
            }
        }
        System.out.print(sb);
    }
}