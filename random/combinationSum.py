'''
 Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T. The same repeated number may be chosen from C unlimited number of times.  All numbers (including target) will be positive integers. The solution set must not contain duplicate combinations. For example, given candidate set [2, 3, 6, 7] and target 7, A solution set is: [[7], [2, 2, 3]]
'''

def combinationSumRec(candidates, target, i, rlist, chosen):
    if target == 0:
        if list(chosen) not in rlist:
            rlist.append(list(chosen))
        return
    if i >= len(candidates):
        return
    if target < 0:
        return
    chosen.append(candidates[i])
    combinationSumRec(candidates, target-candidates[i], i, rlist, chosen)
    combinationSumRec(candidates, target-candidates[i], i+1, rlist, chosen)
    chosen.pop(-1)
    combinationSumRec(candidates, target, i+1, rlist, chosen)
    return
    
def combinationSum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    rlist = []
    chosen = []
    combinationSumRec(candidates, target, 0, rlist, chosen)
    return rlist

print(combinationSum([2, 3, 6, 7], 7))