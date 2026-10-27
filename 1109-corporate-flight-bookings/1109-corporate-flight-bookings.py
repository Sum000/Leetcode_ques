class Solution:
    def corpFlightBookings(self, bookings: list[list[int]], n: int) -> list[int]:

        # brute force approach

        # res = [0] * n

        # for i in range(len(bookings)):
        #     for j in range(bookings[i][0] - 1, bookings[i][1]):
        #         res[j] += bookings[i][2]

        # return res

        # optimal approach

        res = [0] * (n + 1)

        for i in range(len(bookings)):
            res[bookings[i][0] - 1] += bookings[i][2]
            res[bookings[i][1]] -= bookings[i][2]

        total = 0
        for i in range(len(res)):
            total += res[i]
            res[i] = total

        return res[0:n]
            

        