# 정렬 알고리즘

- [Insertion Sort (삽입 정렬)](#Insertion-Sort-(삽입-정렬))
- [Selection Sort (선택 정렬)](#Selection-Sort-(선택-정렬))
- [Bubble Sort (거품 정렬)](#Bubble-Sort-(거품-정렬))
- [Quick Sort (퀵 정렬)](#Quick-Sort-(퀵-정렬))
- [Merge Sort (병합 정렬)](#Merge-Sort-(병합-정렬))
- [Heap Sort (힙 정렬)](#Heap-Sort-(힙-정렬))

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
**공간 복잡도 : O(1)**  (배열이 차지하고 있는 공간 내에서 값들의 위치만 바꾸기 때문)  
**시간 복잡도 : O(n^2)**  



<br>

## Selection Sort (선택 정렬) 

<br>
<br>

## Bubble Sort (거품 정렬) 
