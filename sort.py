import random

n = 50
a = [random.randint(-100, 100) for _ in range(n)]

# 버블정렬: 서로 인접한 두 원소를 비교해 정렬하는 알고리즘
# 평균 시간복잡도는 O(n^2)
def bubbleSort():
    for i in range(n-1):
        for j in range(1, n):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]


# 삽입정렬: 두 번째 값부터 시작해 앞의 원소들과 비교해 삽입할 위치를 찾아 정렬하는 알고리즘
# 평균 시간복잡도는 O(n^2)
def insertionSort():
    for i in range(1, n):
        pos = i-1
        while a[pos] > a[i] and pos > 0: pos -= 1
        a[pos], a[i] = a[i], a[pos]


# 선택정렬: 정렬이 안된 구간에서 가장 작은 원소를 선택해 앞의 인덱스와 바꿔 정렬하는 알고리즘
# 평균 시간복잡도는 O(n^2)
def selectionSort():
    for i in range(n):
        minidx = i
        for j in range(i+1, n):
            if a[minidx] > a[j]: minidx = j
        a[i], a[minidx] = a[minidx], a[i]



if __name__ == '__main__':
    print(a)
    bubbleSort()
    selectionSort()
    print(a)
