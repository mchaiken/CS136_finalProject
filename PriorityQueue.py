# Wrapper class implementing a priority queue interface
# using a Python list as the base data structure and
# algorithms provided by Python's heapq package.
# Not a complete implementation of a priority queue.
# Implements a sufficiently functional priority queue for
# our purposes in Dijkstra's algorithm.

from heapq import heappush, heappop

class PriorityQueue:

    def __init__(self, other=None):
        self._data = []
        if other:
            self.extend(other)

    def push(self, val):
        heappush(self._data, val)

    def pop(self):
        return heappop(self._data)

    def peek(self):
        return self._data[0]

    def extend(self, list):
        for elem in list:
            heappush(self._data, elem)

    # Extend the Priority Queue with the contents
    # provided by a passed iterator. Eliminates the need to
    # create a list of elements from a graph to add to the queue.
    def extendIter(self, iter):
        for elem in iter:
            heappush(self._data, elem)
