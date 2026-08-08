from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        edges = defaultdict(list)
        #we are making an adjacency list of u and it's neighbours with the edge distance
        for u, v, w in times:
            edges[u].append((v, w))

        #initialising minHeap with first 0 because to go from 2 to 2 node the distance edge is 0, and start node is k so it's basically minHeap = [(edge, node)]

        minHeap = [(0, k)]

        visit = set() #so we don't visit the same node twice

        result = 0 # this is gonna store the max value of distance travelled to reach a node

        while minHeap:
            #start edge and node, we will pop it first 
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue

            visit.add(n1)

            result = max(result, w1)

            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1+w2, n2))

        return result if len(visit) == n else -1









