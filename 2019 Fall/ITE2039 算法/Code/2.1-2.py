def insertion_sort(array):
    for j in range(1,len(array)):
        key = array[j]
        i = j-1
        while i >= 0 and array[i]>key:
            array[i+1] = array[i]
            i-=1
        array[i+1] = key
    return array


def noninsertion_sort(array):
    for j in range(1,len(array)):
        key = array[j]
        i = j-1
        while i >= 0 and array[i]<key:
            array[i+1] = array[i]
            i-=1
        array[i+1] = key
    return array


if __name__ == '__main__':
    a = [31, 41, 59, 26, 41, 58]
    print(insertion_sort(a))
    print(noninsertion_sort(a))
