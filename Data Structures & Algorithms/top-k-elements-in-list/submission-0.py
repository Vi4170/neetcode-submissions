class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequency = {}

        for i in nums:
            frequency[i] = frequency.get(i, 0) + 1

        result = []

        for i in range(k):
            most_frequent = max(frequency, key=frequency.get)

            result.append(most_frequent)

            del frequency[most_frequent]

        return result