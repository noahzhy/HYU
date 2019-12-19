def ITERATIVE_BINARY_SEARCH(A, v, low, high):
    while low <= high:
        mid = int((low + high) / 2)
        if v == A[mid]:
            return mid
        elif v > A[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1


if __name__ == '__main__':
    a = [1,5,8,9,14,16,25,35,47,55,62,71]
    print(ITERATIVE_BINARY_SEARCH(a,16,0,len(a)))
