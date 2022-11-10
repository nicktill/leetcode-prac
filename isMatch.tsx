function isMatch(s: string, p: string): boolean {
      const sLen = s.length;
  const pLen = p.length;

  const dp = Array.from({ length: sLen + 1 }, () =>
    Array.from({ length: pLen + 1 }, () => false)
  );

  dp[0][0] = true;

  for (let i = 0; i <= sLen; i++) {
    for (let j = 1; j <= pLen; j++) {
      if (p[j - 1] === '*') {
        dp[i][j] = dp[i][j - 2];
        if (matches(s, p, i, j - 1)) {
          dp[i][j] = dp[i][j] || dp[i - 1][j];
        }
      } else {
        if (matches(s, p, i, j)) {
          dp[i][j] = dp[i - 1][j - 1];
        }
      }
    }
  }

  return dp[sLen][pLen];

};