class Solution(object):
    def convert(self, s, numRows):

        if numRows == 1:
            return s

        row = [[]for _ in range(numRows) ]

        cur_row = 0
        step = 1

        for ch in s :
            row[cur_row].append(ch)
            if cur_row == 0 :
                step = 1
            elif cur_row == numRows -1 :
                step = -1
            
            cur_row += step
        
        return "".join("".join(r) for r in row)

