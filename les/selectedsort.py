
def selectionSort(l):
    i = len(l)-1
    while(1 <= i):
        positie = i
        max = l[i]
        j = i - 1
        while(0 <= j):
            if(l[j] > max):
                positie = j
                max = l[j]
            j = j - 1
        l[positie] = l[i]
        l[i] = max
        i = i-1
    return l


l = [3, 1, 19, 8, -4, 8, 8]
print('pre: ', l)
print('post: ', selectionSort(l))
