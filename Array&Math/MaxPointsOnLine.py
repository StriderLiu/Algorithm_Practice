from copy import deepcopy

# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) < 3:
            return len(points)
        
        res = 2
        
        for i in range(len(points)):
            u = points[i]
            dict, same, vertical = {}, 1, 0
            
            for j in range(i + 1, len(points)):
                v = points[j]
                
                
                if u.x == v.x:
                    if u.y == u.y:
                        same += 1
                    else:
                        vertical += 1
                else:
                    k = float(v.y - u.y) / float(v.x - u.x)
                    b = u.y + u.x * (u.y - v.y) / (v.x - u.x)
                    dict[(k, b)] = dict.setdefault((k, b), 0) + 1
            
            try:
                kMax = max(dict.values())
            except:
                kMax = 0
            res = max(res, max(vertical, kMax) + same)
        
        return res
        
        # use (k, b) as key
        
#         # use (A, B, C) as key

#         maxNum = 2
#         d = {# keys must be immutable type
#                 (
#                  points[1].y - points[0].y,
#                  points[0].x - points[1].x,
#                  points[1].x * points[0].y - points[0].x * points[1].y
#                  ):
#                 set([points[0], points[1]])
#              }
#         
#         for i in range(len(points)):
#             for j in range(len(points[i+1:])):
#                 A = points[j].y - points[i].y
#                 B= points[i].x - points[j].x
#                 C = points[j].x * points[j].y - points[i].x * points[j].y
#                 
#                 keys = deepcopy(d)
#                 for (A_, B_, C_) in keys: # d.keys() will cause "dictionary changed size during iteration" error
#                     if A != 0 and A_ != 0 and (A / A_) * B_ == B and (A / A_) * C_ == C or \
#                        B != 0 and B_ != 0 and (B / B_) * A_ == A and (B / B_) * C_ == C or \
#                        C != 0 and C_ != 0 and (C / C_) * B_ == B and (C / C_) * A_ == A:
#                     # must consider ZeroDivisionError
#                         d[(A_, B_, C_)] |= set([points[i], points[j]])                        
#                         if len(d[(A_, B_, C_)]) > maxNum:
#                             maxNum = len(d[(A_, B_, C_)])
#                     else:
#                         d[(A, B, C)] = set([points[i], points[j]])
                        
#         return maxNum

points = [
            Point(-5, 3),
            Point(2, 3),
            Point(3, 3),
#             Point(4, 5),
#             Point(6, 6),
#             Point(5, 11)
          ]

print(Solution().maxPoints(points))