class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        """
        :type moves: str
        :rtype: int
        """

        L = moves.count('L')
        R = moves.count('R')
        U = moves.count('_')

        left_dist = L + U - R
        right_dist = R + U - L

        return max(left_dist,right_dist)