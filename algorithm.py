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
아이디어 : 계속전진하고 상황이 맞으면 나가는건 당연히 ! while문이다.
"""

# def findmid(a, b, c):
#     if (a - b) * (a - c) <= 0:
#         return a
#     elif (b - a) * (b - c) <= 0:
#         return b
#     else:
#         return c

# def partition(arr, low, high):
    
#     return i + 1

# def quick_sort_helper(arr, low, high):
#     if len(arr) <= 1:
#         return arr
#     mid = ((low + high) // 2)
#     mid_value = findmid(arr[low], arr[mid], arr[high])
#     if mid_value == arr[low]:
#         pivot = low
#     elif mid_value == arr[mid]:
#         pivot = mid
#     else:
#         pivot = high
#     tmp = arr[pivot]
#     arr[pivot] = arr[mid]
#     arr[mid] = tmp
#     pivot = mid
#     left = low
#     right = high
#     leftswitch = 0
#     rightswitch = 0
#     for i in range(len(arr)):
#         if left > right:
#             break
#         if (leftswitch == 1) and (rightswitch == 1):
#             tmp = arr[left]
#             arr[left] = arr[right]
#             arr[right] = tmp
#             leftswitch = 0
#             rightswitch = 0

#         if (left == pivot):
#             left = left + 1
#             continue
#         if (right == pivot):
#             right = right - 1
#             continue
#         if arr[left] > arr[pivot]:
#             leftswitch = 1
#         if arr[right] < arr[pivot]:
#             rightswitch = 1
#         if not leftswitch:
#             left = left + 1
#         if not rightswitch:
#             right = right - 1
#         if left==right:
#             tmp = arr[left]
#             arr[left] = arr[right]
#             arr[right] = tmp
#     return quick_sort_helper(arr[:mid],0,mid-1) + [arr[mid]] + quick_sort_helper(arr[mid+1:],0,len(arr[mid+1:])-1)

# 호어 방식

def findmid(a, b, c):
    if (a - b) * (a - c) <= 0:
        return a
    elif (b - a) * (b - c) <= 0:
        return b
    else:
        return c

def partition(arr, low, high):
    mid = (low+high)//2
    mid_value = findmid(arr[low],arr[mid],arr[high])
    right = high
    left = low
    while True:
        while arr[right] > mid_value:
            right -= 1
        while arr[left] < mid_value:
            left += 1
        if right <= left:
            return right
        arr[left], arr[right] = arr[right], arr[left]
        right -= 1
        left += 1

# 로모토 방식
def partition(arr, low, high):
    pivot = arr[high]
    count = low -1
    for i in range(low,high):
        if arr[i] <= pivot:
            count +=1
            tmp = arr[i]
            arr[i] = arr[count]
            arr[count] = tmp
    arr[count+1], arr[high] = arr[high], arr[count+1]
    return count + 1
        

def quick_sort_helper(arr, low, high):
    if low >= high:
        return
    split = partition(arr, low, high)
    quick_sort_helper(arr, low, split-1)
    quick_sort_helper(arr, split+1, high)
    

 

def quick_sort(arr):
    quick_sort_helper(arr, 0, len(arr) - 1)
    return arr