class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visit=set()
        completed=set()
        res=[]

        premap={i:[] for i in range(numCourses)}

        for crs,pre in prerequisites:
            premap[crs].append(pre)

        def dfs(crs):
            if crs in visit:
                return False
            

            if crs in completed:
                return True

            visit.add(crs)
            

            for pre in premap[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)

            completed.add(crs)
            res.append(crs)
                
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return res
                


