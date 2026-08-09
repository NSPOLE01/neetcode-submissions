class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        map = {}
        for task in tasks:
            if task not in map:
                map[task] = 1
            else:
                map[task] += 1
        heap = []
        for item in map.values():
            heap.append(item * -1)
        heapq.heapify(heap)
        time = 0
        q = deque()
        while heap or q:
            time += 1

            if heap:
                count = 1+ heapq.heappop(heap)
                if count:
                    q.append([count, time+n])
            if q and q[0][1]== time:
                heapq.heappush(heap, q.popleft()[0])

        return time
