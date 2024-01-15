class Solution(object):
    def carFleet(self, target, position, speed):
        time = []
        for p,s in sorted(zip(position,speed)):
            time.append(float(target-p)/s)
        
        fleet = 0
        slow_car = 0
        time = time[::-1]
    
        for t in time:
            if t > slow_car:
                fleet += 1
                slow_car = t
        return fleet
           
        