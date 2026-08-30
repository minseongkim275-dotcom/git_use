"""
알고리즘을 구현시 for문 사용시 범위를 적용하는 법이 필요

"""

def combinations(n, k):
    result = []
    def backtrack(start, current_combination):

    backtrack(1, []) 
    return result

"""

- advanced
퀵정렬 알고리즘의 경우 pivot을 선택하는 것이 중요하며
1. 무작위
2. low or high 
3. low mid high 중에 중간값을 선택
또한 선택한 값에서 low+1 high-1 의 형태로 왔다갔다를 진행을 하며 
피벗보다 큰 arr[low] 와 피벗보다 작은 arr[high]를
서로 교환하며 low와 high가 교차할경우 다음 피벗을 분할으로 골라 재귀하며 알고리즘을 구현한다
pivot을 선택하는 것이 중요한 이유는 최악의 경우 버블정렬과 같은 O(N^2)의 시간 복잡도를 가지기 때문에
pivot을 통해 최악의 경우를 막는 방법을 고안하는 것이 중요하다
하지만 퀵정렬이 지금도 가장 빠른 정렬 알고리즘인 이유는 바로 애초에 정렬된 리스트를 정렬하려고 하지않기 때문이라고
할수도 있다!

"""
