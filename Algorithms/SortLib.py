def merge( iterable, first, middle, last):
    n1 = middle - first + 1 # number of elements in first subarray
    n2 = last - middle      # number of elements in first subarray
    L = []
    R = []
    for i in range(0, n1):
        L.append(iterable[first + i])
    for j in range(0, n2):
        R.append(iterable[middle + j + 1])
    L.append(float('inf'))
    R.append(float('inf'))
    i = 0
    j = 0
    for k in range(first, last + 1):
        if L[i] <= R[j]:
            iterable[k] = L[i]
            i += 1
        else:
            iterable[k] = R[j]
            j += 1


def MergeSort(iterable, first, last):
    if(first < last):
        mid = (first + last)//2
        MergeSort(iterable, first, mid)
        MergeSort(iterable, mid + 1, last)
        merge(iterable, first, mid, last)

if __name__ == "__main__":
    test = [20, 23,25, 1, 4, 5]
    merge(test, 0, 2, 5)
    print(test)

    test2 = [2,5,1,9,10,6,98,43,56,88,33,22,11]
    MergeSort(test2, 0 , len(test2) - 1)
    print(test2)
