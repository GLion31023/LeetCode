from collections import deque


class RecentCounter:
    TIME_WINDOW = 3000

    def __init__(self):
        self.ping_requests = deque()

    def ping(self, t: int) -> int:
        self.ping_requests.append(t)
        while self.ping_requests and self.ping_requests[0] < t - RecentCounter.TIME_WINDOW:
            self.ping_requests.popleft()

        return len(self.ping_requests)


rec_counter = RecentCounter()
print(rec_counter.ping(1))
print(rec_counter.ping(100))
print(rec_counter.ping(3001))
print(rec_counter.ping(3002))
