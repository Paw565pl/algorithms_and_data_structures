def heapify(A, heap_size, i):
    for _ in range(heap_size):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i

        if left < heap_size and A[left] > A[largest]:
            largest = left
        else:
            largest = i

        if right < heap_size and A[right] > A[largest]:
            largest = right

        A[i], A[largest] = A[largest], A[i]
        i = largest

    return A


def build_heap(A):
    heap_size = len(A)
    k = int((len(A) - 2) / 2)

    for i in range(k, -1, -1):
        heapify(A, heap_size, i)

    return A


def heap_sort(A):
    A = build_heap(A)
    heap_size = len(A)

    for i in range(len(A) - 1, 0, -1):
        A[0], A[heap_size - 1] = A[heap_size - 1], A[0]
        heap_size -= 1
        heapify(A, heap_size, 0)

    return A


with open("./input.txt", "r") as f:
    data = []
    for line in f.readlines():
        data.append(int(line.replace("\n", "")))

sorted_data = heap_sort(data)

with open("./output.txt", "w") as f:
    for item in sorted_data:
        f.write(f"{item}\n")
