import java.io.*;

public class Main {
    static int N;
    static char[][] grid;
    static boolean[][] vis;
    static int[] dy = {-1, 1, 0, 0}, dx = {0, 0, -1, 1};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        grid = new char[N][N];
        for(int i = 0; i < N; i++) grid[i] = br.readLine().toCharArray();

        int normal = 0, blind = 0;
        vis = new boolean[N][N];
        for(int i = 0; i < N; i++) {
            for(int j = 0; j < N; j++) {
                if(!vis[i][j]) { dfs(i, j, false); normal++; }
            }
        }

        vis = new boolean[N][N];
        for(int i = 0; i < N; i++) {
            for(int j = 0; j < N; j++) {
                if(!vis[i][j]) { dfs(i, j, true); blind++; }
            }
        }

        System.out.println(normal + " " + blind);
    }

    static void dfs(int y, int x, boolean isBlind) {
        vis[y][x] = true;
        char c = grid[y][x];
        for(int i = 0; i < 4; i++) {
            int ny = y + dy[i], nx = x + dx[i];
            if(ny >= 0 && ny < N && nx >= 0 && nx < N && !vis[ny][nx]) {
                boolean match = isBlind ? (c == 'B' ? grid[ny][nx] == 'B' : grid[ny][nx] != 'B') : grid[ny][nx] == c;
                if(match) dfs(ny, nx, isBlind);
            }
        }
    }
}