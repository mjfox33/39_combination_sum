from code_39_combination_sum import Solution

def test_example_1():
    s = Solution()
    candidates = [2,3,5,7]
    target = 8
    assert s.combinationSum(candidates, target) == 0