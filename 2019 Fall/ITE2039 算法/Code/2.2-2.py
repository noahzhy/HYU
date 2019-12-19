def selection_sort(a):
    for i in range(0,len(a)-1):
        min_idex = i
        for j in range(i+1,len(a)):
            if (a[j]<a[min_idex]):
                min_idex = j
        # swap a[min_idex] and a[i]
        a[min_idex], a[i] = a[i], a[min_idex]
    return a


if __name__ == '__main__':
    a = [31, 41, 59, 26, 41, 58]
    print(selection_sort(a))
