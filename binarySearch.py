#Recursive
def binary_search_rec(a, key, low, high):
    if low > high:
        return -1

    mid = (low + int((high - low)/2))
    if a[mid] == key:
        return mid
    elif key < a[mid]:
        return binary_search_rec(a, key, low, mid - 1)
    else:
        return binary_search_rec(a, key, mid + 1, high)

def binary_search(a, key):
    return binary_search_rec(a, key, 0, len(a)-1)

#iterative
def binary_search_iterative(a, key):
    low = 0
    high = len(a) - 1

    while low <= high:
        mid = int(low + (high - low)/2)

        if key == a[mid]:
            return mid

        if key < a[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
b = binary_search(a, 100)
print(b)
c = binary_search(a, 3)
print(c)

d = binary_search_iterative(a, 70)
print(d)
e = binary_search_iterative(a, 3)
print(e)

