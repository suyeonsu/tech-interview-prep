# 정렬 알고리즘

- [Insertion Sort (삽입 정렬)](#insertion-sort-삽입-정렬)
- [Selection Sort (선택 정렬)](#selection-sort-선택-정렬)
- [Bubble Sort (거품 정렬)](#bubble-sort-거품-정렬)
- [Quick Sort (퀵 정렬)](#quick-sort-퀵-정렬)
- [Merge Sort (병합 정렬)](#merge-sort-병합-정렬)
- [Heap Sort (힙 정렬)](#heap-sort-힙-정렬)
- [Sorting Algorithm's Complexity 정리](#sorting-algorithms-complexity-정리)

<br>

## Insertion Sort (삽입 정렬)
n 개의 원소를 가진 배열을 정렬할 때, 정렬하려는 i번째 원소를, (0 부터 i-1 까지의 원소들은 정렬되어있다는 가정하에) 배열의 i-1번째 원소부터 0번째 원소까지 비교하며 적절한 위치를 찾아 삽입하여 정렬하는 알고리즘이다. i번째 원소가 더 클 경우 위치를 바꾼다.

```py
def insertionSort(a, n):
    for i in range(1, n):
        pos = i-1
        while pos > 0 and a[pos] > a[i]:
            a[pos], a[i] = a[i], a[i - 1]
            i -= 1
```
**공간 복잡도 : O(n)**  (배열이 차지하고 있는 공간 내에서 값들의 위치만 바꾸기 때문)  
**시간 복잡도 : O(n^2)**  

<br>

## Selection Sort (선택 정렬) 
n 개의 원소를 가진 배열을 정렬할 때, i번째 이후의 원소들 중 최솟값을 찾아 i번째 원소와 교체하는 알고리즘으로, 원소를 넣을 위치는 이미 정해져있고 그 위치에 어떤 원소를 넣을지 선택하는 정렬 알고리즘이다.

```py
def selectionSort(a, n):
    for i in range(n):
        minidx = i
        for j in range(i+1, n):
            if a[minidx] > a[j]: minidx = j
        a[i], a[minidx] = a[minidx], a[i]
```
**공간 복잡도 : O(n)**  
**시간 복잡도 : O(n^2)**  

<br>

## Bubble Sort (거품 정렬) 
n 개의 원소를 가진 배열을 정렬할 때, 인접한 두 개의 원소를 비교하며 정렬해 나가는 알고리즘이다. 첫 번째 패스를 수행하면 배열의 가장 큰 원소가 맨 끝에 위치하게 되고, 정렬된 원소는 다음 패스에서 제외된다.

```py
def bubbleSort(a, n):
    for i in ragne(n-1):    # i는 다음 패스에서 제외될 원소의 개수
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
```
**공간 복잡도 : O(n)**  
**시간 복잡도 : O(n^2)**  

<br>

## Quick Sort (퀵 정렬) 
Divide and Conquer 전략을 사용하여 Sorting 이 이루어진다. Divide 과정에서 pivot이라는 개념이 사용된다. pivot 을 기준으로 좌측은 pivot 으로 설정된 값보다 작은 값이 위치하고, 우측은 큰 값이 위치하도록 partition된다. 이렇게 나뉜 좌, 우측 각각의 배열을 다시 재귀적으로 Quick Sort 시키면 또 partition 과정이 적용된다.이 때 한 가지 주의할 점은 partition 과정에서 pivot 으로 설정된 값은 다음 재귀과정에 포함시키지 않아야 한다. 이미 partition 과정에서 정렬된 자신의 위치를 찾았기 때문이다.

```py
def quickSort(a, start, end):
    if start >= end: return
    pivot = start
    l, r = start+1, end
    while l <= r:
        while a[l] < a[pivot]: l += 1
        while a[r] > a[pivot]: r -= 1
        if l < r: a[l], a[r] = a[r], a[l]
        else: break
    a[pivot], a[r] = a[r], a[pivot]
    quickSort(a, 0, r-1)
    quickSort(a, r+1, end)
```
**공간 복잡도 : O(log(n))**  
**시간 복잡도 : O(nlogn)**  

<br>

## Merge Sort (병합 정렬) 
복잡한 문제를 복잡하지 않은 문제로 분할하여 정복하는 방법이다. 더이상 나누어지지 않을 때까지 반 씩(1/2) 분할하다가 더 이상 나누어지지 않은 경우(원소가 하나인 배열일 때)에는 자기 자신, 즉 원소 하나를 반환한다. 반환한 값끼리 combine될 때, 비교가 이뤄지며 비교 결과를 기반으로 정렬되어 임시 배열에 저장되고 이 임시 배열에 저장된 순서를 합쳐진 값으로 반환한다.

```py
def mergeSort(a, start, end):
    if len(a) <= 1: return a
    mid = (start + end) // 2
    mergeSort(a, start, mid)
    mergeSort(a, mid+1, end)
    return merge(a, start, mid, end)

def merge(a, start, mid, end):
    i = start   # 왼쪽 배열의 시작
    j = mid+1   # 오른쪽 배열의 시작

    tmp = []
    while i < mid and j < end:
        if a[i] < a[j]:
            tmp.append(a[i])
            i += 1
        else:
            tmp.append(a[j])
            j += 1

    if i < mid: tmp += a[i:mid+1]
    if j < end: tmp += a[j:]
    return tmp
```
**공간 복잡도 : O(n)**  
**시간 복잡도 : O(nlogn)**  

<br>

## Quick Sort vs Merge Sort  

> 두 정렬 알고리즘 다 average case formula 이고 심지어 Quick Sort는 worst case formula이다. 하지만 보통 일반적으로 퀵소트가 빠른것으로 알고 있다.
>
>일단 Quick Sort 의 worst case는 (맨앞의 수를 pivot으로 가정) 아이러니 하게 정렬이 잘 되어 있는 배열에서 나온다.
>
>이렇게 Quick Sort의 worst case 와 평균적인 Merge Sort 를 비교해도 Quick Sort가 더 빠르게 나온다. 그 이유는 실제 시간 정렬 되는 중 Merge Sort는 분할 과정에서 추가적인 배열을 생성해야 한다는 문제가 있다. 이러한 과정에서 계속적으로 Delay 가 생기다 보니 결과적으로 Quick Sort가 더욱 빠르게 정렬이 되는 것이다.

<br>

## Heap Sort (힙 정렬) 
완전 이진 트리를 기본으로 하는 힙 자료구조를 기반으로 한 정렬 방식이다. 
1. 배열의 모든 원소를 힙에 넣는다. (최대 힙)
2. 가장 큰 값이 존재하는 힙의 루트 원소의 값을 빼며 마지막 자식을 루트로 옮긴다. 힙의 사이즈를 하나 줄인다.
3. 힙의 사이즈가 1보다 크면 2를 반복하여 빠진 원소를 차례로 정렬한다.

```py
def heapSort(a, n):
    for i in range(n//2-1, -1, -1):
        heapify(a, n, i)
    for i in range(n-1, 0, -1):
        a[0], a[i] = a[i], a[0]
        heapify(a, i, 0)

def heapify(a, n, i):
    p = i   # 부모 노드
    l = i * 2 + 1   # 왼쪽 자식 노드
    r = i * 2 + 2   # 오른쪽 자식 노드

    # 왼쪽 자식 노드와 부모 노드를 비교해 큰 값을 부모 노드로 올림
    if l < n and a[p] < a[l]: p = l
    
    # 오른쪽 자식 노드와 부모 노드를 비교해 큰 값을 부모 노드로 올림
    if r < n and a[p] < a[r]: p = r
    
    # 부모 노드를 가리키는 p 값이 바뀌면 위치를 교환하고 heapify()를 호출해 과정을 반복
    if (i != p):
        a[p], a[i] = a[i], a[p]
        heapify(a, n, p)
```

>#### heapSort(a, n)
>- 1번째 heapify  
일반 배열을 힙으로 구성하는 역할을 한다.
자식노드로부터 부모 노드를 비교한다.  
(n/2)-1부터 0까지 인덱스를 돌리는 이유는?  
부모 노드의 인덱스를 기준으로 왼쪽 자식 노드 : ix2+1, 오른쪽 자식 노드 : ix2+2이기 때문이다.  
>
>- 2번째 heapify  
요소 하나가 제거된 이후에 다시 최대 힙을 구성하기 위함이다.
루트를 기준으로 진행한다.  
>
>#### heapify(a, n, i)
>- 다시 최대 힙을 구성할 때까지 부모 노드와 자식 노드를 swap 하며 재귀 호출한다.


퀵 정렬과 합병 정렬의 성능이 좋기 때문에 힙 정렬의 사용 빈도가 높지는 않다.
하지만, 힙 자료구조가 많이 활용되고 있으며, 이 때 함께 따라오는 개념이 Heap Sort이다.

#### _Heap Sort가 유용한 경우?_
- 가장 크거나 가장 작은 값을 구할 때  
최소 힙 or 최대 힙의 루트 값이기 때문에 한 번의 힙 구성을 통해 구하는 것이 가능하다.  
- 최대 k 만큼 떨어진 요소들을 정렬할 때  
삽입 정렬보다 더욱 개선된 결과를 얻어낼 수 있다.

**공간 복잡도 : O(1)**  
**시간 복잡도 : O(nlogn)**  

<br>

## Sorting Algorithm's Complexity 정리

|   Algorithm    | Space Complexity | (average) Time Complexity | (worst) Time Complexity |
| :------------: | :--------------: | :-----------------------: | :---------------------: |
|  Bubble sort   |       O(1)       |          O(n^2)           |         O(n^2)          |
| Selection sort |       O(1)       |          O(n^2)           |         O(n^2)          |
| Insertion sort |       O(1)       |          O(n^2)           |         O(n^2)          |
|   Merge sort   |       O(n)       |         O(nlogn)          |        O(nlogn)         |
|   Heap sort    |       O(1)       |         O(nlogn)          |        O(nlogn)         |
|   Quick sort   |       O(1)       |         O(nlogn)          |         O(n^2)          |
|   Count sort   |       O(n)       |           O(n)            |          O(n)           |
|   Radix sort   |       O(n)       |           O(n)            |          O(n)           |
