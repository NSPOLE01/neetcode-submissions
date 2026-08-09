class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_map = Counter(nums)
        result = []
        num_list = list(num_map)
        num_list.sort(reverse=True)

        for i in range(k):
            result.append(num_list[i])
            i += 1
        return result


        