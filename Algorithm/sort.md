# 정렬 알고리즘

- [Insertion Sort (삽입 정렬)](#insertion-sort-삽입-정렬)
- [Selection Sort (선택 정렬)](#selection-sort-선택-정렬)
- [Bubble Sort (거품 정렬)](#bubble-sort-거품-정렬)
- [Quick Sort (퀵 정렬)](#quick-sort-퀵-정렬)
- [Merge Sort (합병 정렬)](#merge-sort-합병-정렬)
- [Heap Sort (힙 정렬)](#heap-sort-힙-정렬)

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
