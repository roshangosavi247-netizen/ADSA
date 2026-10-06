import java.util.Arrays;

public class PrimMatrix {

    private static int minKey(int[] key, boolean[] mstSet, int vCount) {
        int min = Integer.MAX_VALUE;
        int minIndex = -1;

        for (int v = 0; v < vCount; v++) {
            if (!mstSet[v] && key[v] < min) {
                min = key[v];
                minIndex = v;
            }
        }
        return minIndex;
    }

    public static void primMST(int[][] graph) {
        int vCount = graph.length;
        int[] parent = new int[vCount];
        int[] key = new int[vCount];
        boolean[] mstSet = new boolean[vCount];

        Arrays.fill(key, Integer.MAX_VALUE);
        Arrays.fill(mstSet, false);

        // Start from vertex 0
        key[0] = 0;
        parent[0] = -1;

        for (int count = 0; count < vCount - 1; count++) {
            int u = minKey(key, mstSet, vCount);
            if (u == -1) break; // Disconnected graph safeguard

            mstSet[u] = true;

            for (int v = 0; v < vCount; v++) {
                if (graph[u][v] != 0 && !mstSet[v] && graph[u][v] < key[v]) {
                    parent[v] = u;
                    key[v] = graph[u][v];
                }
            }
        }

        // Print MST
        System.out.println("Edge \tWeight");
        int totalWeight = 0;
        for (int i = 1; i < vCount; i++) {
            if (parent[i] != -1) {
                System.out.println(parent[i] + " - " + i + " \t" + graph[i][parent[i]]);
                totalWeight += graph[i][parent[i]];
            }
        }
        System.out.println("Total Weight: " + totalWeight);
    }

    public static void main(String[] args) {
        int[][] graph = {
            {0, 2, 0, 6, 0},
            {2, 0, 3, 8, 5},
            {0, 3, 0, 0, 7},
            {6, 8, 0, 0, 9},
            {0, 5, 7, 9, 0}
        };

        primMST(graph);
    }
}
