arr = [8, 3, 2, 5, 9, 7, 1]
# arr = [8,2,3,5,7,1,9]
n = len(arr)

def bubble_sort_v1(arr):
    n = len(arr)
    counter = 0
    for i in range(n):
        m = n - 1 - i
        print(arr, m)
        for j in range(m):
            if arr[j] > arr[j + 1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
                counter += 1
    print(counter)

def bubble_sort_v2(arr):
    n = len(arr)
    for i in range(n):
        j = i + 1;

        while j < n:
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            j += 1
        print(arr)

def bubble_sort_v3(arr):
    n = len(arr)
    for i in range(n):
        j = n - 1
        print(arr)
        while j > i:
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            j -= 1


bubble_sort_v3(arr[:])
print("v3")
bubble_sort_v2(arr[:])
print("v2")
bubble_sort_v1(arr[:])

