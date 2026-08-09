class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        results = []
        returnVal = []
        index = 0
        for point in points:
            distance = math.sqrt((point[0] * point[0]) + (point[1] * point[1]))
            results.append((distance, index))
            index += 1
        heapq.heapify(results)
        while k != 0:
            k -= 1
            val, ind = heapq.heappop(results)
            returnVal.append(points[ind])

        return returnVal


        