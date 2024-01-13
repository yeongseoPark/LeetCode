class Solution(object):
    def threeSum(self, nums):
        res = set()
        
        # negative, positive, zero
        n, p, z = [], [], []
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0:
                n.append(num)
            else:
                z.append(num)
        
        # negative, positive O(1) lookup
        N, P = set(n), set(p)
        
        # 0이 리스트에 있는경우  
        if z:
            for num in P:
                if -num in N:
                    res.add((-1*num, 0, num))
            if len(z) >= 3:
                res.add((0,0,0))
                    
        for i in range(len(n)):
            for j in range(i+1, len(n)):
                target = -1*(n[i]+n[j])
                if target in P:
                    res.add(tuple(sorted([n[i],n[j],target])))
        
        for i in range(len(p)):
            for j in range(i+1, len(p)):
                target = -1*(p[i]+p[j])
                if target in N:
                    res.add(tuple(sorted([p[i],p[j],target])))
                
        return res