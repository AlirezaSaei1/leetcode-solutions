class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hash_map = {arr2[i]: i for i in range(len(arr2))}

        arr1.sort(key=lambda x: (hash_map.get(x, len(arr2)), x))
        return arr1