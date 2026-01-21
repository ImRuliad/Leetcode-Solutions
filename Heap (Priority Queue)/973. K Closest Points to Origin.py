"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k,
return the k closest points to the origin (0, 0).
The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
"""

import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        result = []
        counter = 1

        for index, (x, y) in enumerate(points):
            distance = sqrt(((x - 0) ** 2) + ((y - 0) ** 2))
            heapq.heappush(min_heap, (distance, (x, y)))

        while counter <= k:
            xy_coords = list(heapq.heappop(min_heap)[1])
            result.append(xy_coords)
            counter += 1
        return result