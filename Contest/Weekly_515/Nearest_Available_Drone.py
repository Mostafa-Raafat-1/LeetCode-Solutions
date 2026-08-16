class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        nearest_distance = float("inf")
        index = -1

        for i, drone in enumerate(drones):
            distance = abs(drone[0] - target[0]) + abs(drone[1] - target[1])
            if distance < nearest_distance and drone[2] >= distance:
                nearest_distance = distance
                index = i

        return index


print(Solution().nearestDrone(drones=[[4, 4, 5]], target=[8, 6]))
