"""
알고리즘을 구현시 for문 사용시 범위를 적용하는 법이 필요

"""

def combinations(n, k):
    result = []
    def backtrack(start, current_combination):
        if len(current_combination) == k:
            result.append(current_combination[:])
            return
        for num in range(start, n+1):
            current_combination.append(num)
            backtrack(num+1,current_combination)
            current_combination.pop()
    backtrack(1, [])
    return result
