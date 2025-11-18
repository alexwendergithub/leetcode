class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        num_cols = len(strs[0])
        num_rows = len(strs)
        columns_to_delete = 0
        for col_idx in range(num_cols):
            for row_idx in range(1, num_rows):
                if strs[row_idx][col_idx] < strs[row_idx - 1][col_idx]:
                    columns_to_delete += 1
                    break
        return columns_to_delete