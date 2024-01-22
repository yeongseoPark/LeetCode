
    
class Solution(object):
    def minEatingSpeed(self, piles, h):
        def eat(k, h, piles):
            time = 0
            for pile in piles:
                time += -(-pile // k)  # Equivalent to ceil(pile / k)
            return time <= h

        lo = 1
        hi = max(piles)
        
        while lo < hi:
            mid = (lo + hi) // 2
            if eat(mid, h, piles):
                hi = mid
            else:
                lo = mid + 1
        
        return lo
