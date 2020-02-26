class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == len(arr):
            return arr
        return sorted(arr)[:k]

