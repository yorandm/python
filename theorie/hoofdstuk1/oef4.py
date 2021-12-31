# geen dodona


def selection_sort_vooraan(a):
    for i in range(len(a)):
        x = a[i]
        j = i
        while j > 0 and x > a[j-1]:
            a[j] = a[j-1]
            j = j-1
        a[j] = x
        print(a)


a = [int(_) for _ in input().split()]
selection_sort_vooraan(a)
