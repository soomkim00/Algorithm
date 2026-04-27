import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int M = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());
        int H = Integer.parseInt(st.nextToken());
        int[][][] board = new int[H][N][M];
        Queue<int[]> q = new LinkedList<>();
        int unriped = 0;
        for(int i = 0; i < H; i++) {
            for(int j = 0; j < N; j++) {
                st = new StringTokenizer(br.readLine());
                for(int k = 0; k < M; k++) {
                    board[i][j][k] = Integer.parseInt(st.nextToken());
                    if(board[i][j][k] == 1) q.add(new int[]{i, j, k, 0});
                    else if(board[i][j][k] == 0) unriped++;
                }
            }
        }
        if(unriped == 0) { System.out.println(0); return; }
        int[] dz = {1, -1, 0, 0, 0, 0};
        int[] dy = {0, 0, 1, -1, 0, 0};
        int[] dx = {0, 0, 0, 0, 1, -1};
        int ans = 0;
        while(!q.isEmpty()) {
            int[] cur = q.poll();
            ans = cur[3];
            for(int i = 0; i < 6; i++) {
                int nz = cur[0] + dz[i], ny = cur[1] + dy[i], nx = cur[2] + dx[i];
                if(nz >= 0 && nz < H && ny >= 0 && ny < N && nx >= 0 && nx < M && board[nz][ny][nx] == 0) {
                    board[nz][ny][nx] = 1;
                    unriped--;
                    q.add(new int[]{nz, ny, nx, cur[3] + 1});
                }
            }
        }
        System.out.println(unriped == 0 ? ans : -1);
    }
}