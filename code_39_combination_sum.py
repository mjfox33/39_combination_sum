class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort() # just to ensure they are in order
        result = []

        def combination(target, current_index, current_path):
            if  target<0:
                return
            
            if target==0:
                result.append(current_path)
                return
            
            for i in range(current_index, len(candidates)):
                combination(target-candidates[i], i, current_path+[candidates[i]])
                
        combination(target,0,[])
        return result
