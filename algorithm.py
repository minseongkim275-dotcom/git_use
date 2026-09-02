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

"""

분할정렬
분할 정렬의 아이디어는 원자값까지 쪼개는 거지만 arr 실제 배열은 쪼개지 않고 left와 right로 나눈다는 것이다.
재귀는 base case가 중요한데 재귀가 2개가 있고 아래에 merge가 있다면 
그거를 쓰는 것이다. 원자값까지 쪼갠다 => 배열에서 left와 right를 범위로 쪼갠다.



"""
def merge(arr, left, mid, right):
    """
    두 개의 정렬된 부분 배열을 병합하는 함수
    
    Args:
        arr: 원본 배열
        left: 왼쪽 부분의 시작 인덱스
        mid: 왼쪽 부분의 끝 인덱스
        right: 오른쪽 부분의 끝 인덱스
    """
    # TODO: 왼쪽과 오른쪽 부분 배열을 임시 배열로 복사
    leftarr = arr[left:mid+1]
    rightarr = arr[mid+1:right+1]
    pass
    
    # TODO: 두 배열을 병합
    sorted = []
    pass
    
    leftarrcount = 0
    rightarrcount = 0
    while leftarrcount < len(leftarr) and rightarrcount < len(rightarr):
        if leftarr[leftarrcount] < rightarr[rightarrcount]:
            sorted.append(leftarr[leftarrcount])
            leftarrcount += 1
        else:
            sorted.append(rightarr[rightarrcount])
            rightarrcount += 1
          
        
    sorted.extend(leftarr[leftarrcount:])
    sorted.extend(rightarr[rightarrcount:])
    arr[left:right+1] = sorted

    # TODO: left_arr와 right_arr를 비교하며 작은 값을 arr에 복사

    pass
    
    # TODO: 남은 원소들을 복사
    # left_arr에 남은 원소가 있으면 복사
    # right_arr에 남은 원소가 있으면 복사
    pass

def merge_sort_helper(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort_helper(arr, left, mid)      # 왼쪽 절반 재귀 정렬
        merge_sort_helper(arr, mid + 1, right) # 오른쪽 절반 재귀 정렬
        merge(arr, left, mid, right)           # 정렬된 두 절반 병합

def merge_sort(arr):
    """
    머지 정렬 메인 함수
    
    Args:
        arr: 정렬할 배열
    
    Returns:
        정렬된 배열
    """
    if len(arr) > 1:
        merge_sort_helper(arr, 0, len(arr) - 1)
    return arr

"""
하드웨어 프로세서 접근

### ① Disk → Memory (프로그램 적재)
1. 쉘에 `./hello` 입력 → OS의 **로더(loader)**가 실행 요청 처리
2. 디스크에 있던 hello 바이너리를 **I/O 버스**를 거쳐 **메인 메모리**로 복사
3. 이 복사는 보통 **DMA(Direct Memory Access)** 방식으로 이루어짐 → **디스크 컨트롤러가 CPU 개입 없이 직접 메모리에 데이터를 써 넣음**, 끝나면 CPU에 인터럽트로 완료 알림

### ② Memory → CPU (실행 준비)
- OS가 **PC(Program Counter)**를 hello 프로그램의 시작 주소로 설정
- 이제부터 CPU가 Fetch-Decode-Execute 사이클 시작

### ③ Fetch: 메모리 → CPU로 인스트럭션 읽어오기
- CPU가 **PC가 가리키는 주소**를 **시스템(메모리) 버스**를 통해 메모리에 요청
- 메모리는 해당 주소의 데이터를 **워드(word) 단위**로 CPU에 전송
- CPU는 이를 받아 내부 레지스터에 저장

### ④ Decode + Execute: 인스트럭션 종류별로 다른 부품 조합 사용

| 인스트럭션 종류 | 사용되는 부품 조합 |
|---|---|
| 산술/논리 연산 (`add`, `sub` 등) | 제어유닛 + 레지스터 파일 + **ALU** |
| 메모리 읽기 (`load`) | 제어유닛 + 레지스터 파일 + **메모리 버스** (메모리→레지스터) |
| 메모리 쓰기 (`store`) | 제어유닛 + 레지스터 파일 + **메모리 버스** (레지스터→메모리) |
| 분기/함수호출 (`jmp`, `call`, `ret`) | 제어유닛 + **PC 직접 변경** (+ call/ret은 스택에 store/load로 복귀주소 관리) |

→ CPU는 고정된 소수의 부품(PC, 레지스터 파일, ALU, 메모리 인터페이스)을 갖고 있고, **인스트럭션마다 그 부품들을 다른 조합·순서로 연결해서 사용**하는 기계. 이 조합을 결정하는 게 **제어유닛(Control Unit)**.

### ⑤ Load / Store 상세 흐름

**적재(Load) — 메모리 → 레지스터**
```
1. 제어유닛: load 명령 해석
2. 가져올 메모리 주소 계산
3. CPU → 메모리버스: "이 주소 값을 달라" 요청
4. 메모리: 데이터를 워드 단위로 버스에 전송
5. CPU: 받은 데이터를 레지스터에 저장
```

**저장(Store) — 레지스터 → 메모리**
```
1. 제어유닛: store 명령 해석
2. 저장할 목적지 주소 계산
3. 레지스터 값을 꺼냄
4. CPU → 메모리버스: 주소+값 전송
5. 메모리: 해당 주소에 값을 씀
```

### ⑥ 점프(Jump) — 실행 흐름 자체를 바꾸는 동작

- load/store와 달리 **데이터 이동이 아니라 PC 레지스터 자체를 변경**하는 동작
- 기본적으로 PC는 fetch마다 자동 증가(+1) → 순서대로 진행
- if문/반복문/함수호출을 구현하려면 순서를 벗어나 다른 위치로 건너뛰어야 함 → 점프 필요

| 종류 | 설명 |
|---|---|
| 무조건 점프 (`jmp`) | 조건 없이 PC를 지정 주소로 변경 |
| 조건 점프 (`je`, `jne` 등) | 상태 레지스터(직전 연산 결과 플래그) 확인 후 조건 맞을 때만 PC 변경 → if/while 구현 기반 |
| 함수 호출 (`call`) | 복귀주소를 스택(메모리)에 store → PC를 호출 함수 주소로 변경 |
| 함수 복귀 (`ret`) | 스택에서 복귀주소를 load → PC를 그 주소로 복원 |

### I/O 흐름 (입출력 버스)
- **I/O 버스**에는 여러 **컨트롤러/어댑터**가 연결되어 디스크, 그래픽, USB 등 각 장치와 시스템 버스 사이를 중개함
- 디스크 → 메모리 전송은 CPU를 거치지 않는 **DMA**로 처리되어 효율적

---

## 2. 개념 정리

### 버스(Bus)란
- 시스템 내부를 관통하는 **전기적 배선군**. 컴포넌트 간에 **데이터를 옮기는 통로**.
- 전송 단위는 **고정된 바이트 크기의 워드(word)**.

### 버스의 종류

| 버스 종류 | 역할 |
|---|---|
| **시스템 버스 (System Bus)** | CPU ↔ 메인 메모리(그리고 I/O 브리지) 사이를 연결 |
| **메모리 버스 (Memory Bus)** | CPU가 메모리에 주소를 보내고 데이터를 주고받는 통로 |
| **I/O 버스 (I/O Bus)** | 디스크, 그래픽카드, USB 등 각종 I/O 장치와 시스템을 연결하는 통로 (예: USB는 I/O 버스의 한 종류/표준) |

### 컨트롤러 vs 어댑터 — 차이는 "패키징"
- 둘 다 **I/O 버스와 I/O 장치 사이에서 정보를 주고받는 칩셋**으로 기능은 동일함
- **패키징(Packaging)** = 물리적으로 어디에, 어떤 형태로 장착되어 있는가의 차이
  - **컨트롤러**: 마더보드나 장치 자체에 **내장된 칩셋** (붙박이)
  - **어댑터**: 마더보드의 **슬롯에 꽂는 카드 형태** (탈부착 가능)
- 비유: 컨트롤러 = 스마트폰 내장 카메라 / 어댑터 = 노트북에 꽂는 외장 웹캠
- 참고: USB는 컨트롤러/어댑터와 층위가 다름 → **USB는 버스(인터페이스 규격) 자체**이고, 그 버스에 물린 컨트롤러가 실제 전송을 관리

### 메인 메모리 (DRAM)
- 메인 메모리는 **연속적인 바이트들의 배열**로, 각 바이트는 0부터 시작하는 **고유 주소**를 가짐
- **DRAM (Dynamic RAM)**: 1비트를 **커패시터(축전기) + 트랜지스터**로 저장
  - **"Dynamic(동적)"의 의미**: 저장 내용이 바뀐다는 뜻이 아니라, **커패시터 전하가 시간이 지나면 누설(leak)되어 저절로 사라지기 때문에 주기적으로 재충전(refresh)해줘야 값이 유지**된다는 뜻
  - 대비 개념: **SRAM (Static RAM)** — 플립플롭 회로로 저장, 전원만 있으면 refresh 없이 값 유지 → CPU 캐시(L1/L2/L3)에 사용, 빠르지만 비쌈·저용량

| 구분 | DRAM | SRAM |
|---|---|---|
| 저장방식 | 커패시터 | 플립플롭 회로 |
| 유지방법 | 주기적 refresh 필요 | 전원만 있으면 유지 |
| 용도 | 메인 메모리 | CPU 캐시 |
| 속도/가격 | 느림/저렴 | 빠름/비쌈 |

- **"Random"의 의미**: 값이 무작위로 저장된다는 뜻이 아니라, **주소만 알면 순서에 상관없이 어느 위치든 거의 동일한 시간에 즉시 접근 가능**하다는 뜻 (Random Access = 임의 접근)
  - 대비 개념: 순차 접근(Sequential Access, 예: 테이프) — 원하는 위치까지 순서대로 다 거쳐야 함
  - 즉 "고유 주소를 갖는다"는 특성이 바로 Random Access를 가능하게 하는 이유 → 둘은 모순이 아니라 한 쌍의 개념

### 레지스터 (Register)
- **CPU 내부에 있는, 아주 작지만 극도로 빠른 임시 저장 공간**
- 메모리(느리지만 큼) vs 레지스터(빠르지만 작음) — ALU가 계산하려면 값이 레지스터에 있어야 빠르게 처리 가능

| 레지스터 | 역할 |
|---|---|
| PC (Program Counter) | 다음에 fetch할 인스트럭션의 메모리 주소 |
| 범용 레지스터 (`%rax` 등) | 계산 중간값, 함수 인자 등 다용도 저장 |
| 스택 포인터(SP) | 현재 스택 맨 위 주소 |
| 상태(플래그) 레지스터 | 직전 연산 결과 정보 (0인지, 음수인지, 오버플로우인지 등) → 조건 분기에 사용 |

---

## 3. 궁금했던 사항 (Q&A)

**Q. 컨트롤러랑 어댑터의 차이인 "패키징"이 뭐야?**
→ 기능은 동일한 칩셋이고, 차이는 물리적 장착 형태. 컨트롤러는 보드/장치에 내장, 어댑터는 슬롯에 꽂는 카드 형태.

**Q. DRAM이 동적으로 저장된다는 뜻이겠네?**
→ 아님. "동적(Dynamic)"은 저장 내용이 바뀐다는 뜻이 아니라, 커패시터의 전하가 시간이 지나면 누설되어 값이 사라지기 때문에 **주기적으로 refresh해야 값이 유지된다**는 뜻.

**Q. 배열에 저장되는데(고유 주소를 갖는데) 왜 Random이야, 랜덤이 아니라 주소를 갖잖아?**
→ 여기서 Random은 "무작위"가 아니라 "**임의 접근(Random Access)**" = 주소만 알면 순서 상관없이 어디든 즉시 접근 가능하다는 뜻. 테이프 같은 순차 접근과 대비되는 개념. 오히려 "주소를 갖는다"는 특성 덕분에 Random Access가 가능한 것.

**Q. 디스크 컨트롤러가 메모리에 걍 때려넣고 PC가 그걸 읽는다는 거고, 레지스터는 어떤 역할을 하지?**
→ 레지스터는 CPU 내부의 초고속 임시 저장 공간. 메모리는 크지만 느려서, 계산에 쓸 값을 레지스터로 잠깐 가져와(load) ALU로 처리하고, 결과를 다시 레지스터/메모리에 저장(store)하는 방식으로 동작. PC도 레지스터 중 하나로, "다음에 읽을 위치"를 담당.

**Q. 인스트럭션(hello 파일)에 따라서 동작하는 부품이 조합되어 처리되는 거야?**
→ 맞음. CPU는 PC, 레지스터 파일, ALU, 제어유닛 같은 고정된 부품들을 갖고 있고, 인스트럭션 종류(연산/load/store/분기)에 따라 그중 필요한 부품만 골라 다른 조합·순서로 사용. 이걸 판단하고 조율하는 게 제어유닛.

**Q. CPU에서 레지스터로의 적재/저장 작업을 설명해줘**
→ **적재(Load)**: 메모리 → 레지스터로 값을 복사해오는 것 (계산할 값을 CPU 가까이 끌어옴). **저장(Store)**: 레지스터 → 메모리로 값을 써넣는 것 (계산 결과를 오래 보관할 공간에 남김). CPU는 이 load/store 왕복으로 메모리와 데이터를 주고받음.

**Q. 작업 점프는?**
→ Load/Store가 데이터를 옮기는 동작이라면, **점프(Jump)는 PC 레지스터 자체를 바꿔서 실행 흐름을 바꾸는 동작**. 무조건 점프(`jmp`), 조건 점프(`je` 등, if/while의 기반), 함수호출(`call`, 복귀주소를 스택에 store 후 PC 변경), 함수복귀(`ret`, 스택에서 복귀주소 load 후 PC 복원)로 구성됨.

"""