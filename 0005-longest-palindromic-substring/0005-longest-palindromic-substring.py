class Solution(object):
    def longestPalindrome(self, s):
        # Step 1: Transform string
        t = '#' + '#'.join(s) + '#'
        n = len(t)
        
        P = [0] * n
        center = 0
        right = 0
        max_len = 0
        center_index = 0

        for i in range(n):
            mirror = 2 * center - i

            if i < right:
                P[i] = min(right - i, P[mirror])

            # Expand around center i
            a = i + P[i] + 1
            b = i - P[i] - 1

            while a < n and b >= 0 and t[a] == t[b]:
                P[i] += 1
                a += 1
                b -= 1

            # Update center and right boundary
            if i + P[i] > right:
                center = i
                right = i + P[i]

            # Track max palindrome
            if P[i] > max_len:
                max_len = P[i]
                center_index = i

        # Extract result
        start = (center_index - max_len) // 2
        return s[start:start + max_len]