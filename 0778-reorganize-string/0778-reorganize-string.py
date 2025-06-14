import heapq
from collections import Counter
class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = Counter(s)

        max_freq = max(count.values())
        if max_freq > (len(s) + 1)// 2:
            return ""

        #create a max heap based on frequency
        max_heap = [(-freq, char) for char, freq in count.items()]
        heapq.heapify(max_heap)

        result = []

        while len(max_heap) >= 2:
            freq1, char1 = heapq.heappop(max_heap)
            freq2, char2 = heapq.heappop(max_heap)

            result.extend([char1, char2])

            if -freq1 > 1:
                heapq.heappush(max_heap, (freq1 + 1, char1))
            if -freq2 > 1:
                heapq.heappush(max_heap, (freq2 + 1, char2))

        if max_heap:
            freq, char = heapq.heappop(max_heap)
            if -freq > 1:
                return ""
            result.append(char)
        return "".join(result)