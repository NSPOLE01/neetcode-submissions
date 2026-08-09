class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        results = []
        returnVal = []
        index = 0
        for point in points:
            distance = (math.sqrt((point[0] ** 2) + (point[1] ** 2))) * -1
            heapq.heappush(results, (distance, index))
            if len(results) > k:
                heapq.heappop(results)
            index += 1

        while results:
            val, ind = heapq.heappop(results)
            returnVal.append(points[ind])

        return returnVal


        