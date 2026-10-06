public class LongestCommonSubsequence {

    
    public static int[][] lcsLength(String X, String Y) {
        int m = X.length();
        int n = Y.length();
        int[][] dp = new int[m + 1][n + 1];

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (X.charAt(i - 1) == Y.charAt(j - 1)) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }

        return dp;
    }

    /**
     * Backtracks through the DP table to reconstruct the actual LCS string.
     */
    public static String buildLcs(String X, String Y, int[][] dp) {
        int i = X.length();
        int j = Y.length();
        StringBuilder result = new StringBuilder();

        while (i > 0 && j > 0) {
            if (X.charAt(i - 1) == Y.charAt(j - 1)) {
                result.append(X.charAt(i - 1));
                i--;
                j--;
            } else if (dp[i - 1][j] >= dp[i][j - 1]) {
                i--;
            } else {
                j--;
            }
        }

        // The characters were collected in reverse order during backtracking
        return result.reverse().toString();
    }

    public static void main(String[] args) {
        String X = "ABCBDAB";
        String Y = "BDCAB";

        int[][] dp = lcsLength(X, Y);
        int length = dp[X.length()][Y.length()];
        String lcs = buildLcs(X, Y, dp);

        System.out.println("LCS Length: " + length);
        System.out.println("Actual LCS: " + lcs);
    }
}