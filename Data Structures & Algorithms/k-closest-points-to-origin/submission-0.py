class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        results = []
        heapq.heapify(results)
        returnVal = []
        index = 0
        for point in points:
            distance = math.sqrt((point[0] * point[0]) + (point[1] * point[1]))
            heapq.heappush(results, (distance, index))
            index += 1

        while k != 0:
            k -= 1
            val, ind = heapq.heappop(results)
            returnVal.append(points[ind])

        return returnVal


        