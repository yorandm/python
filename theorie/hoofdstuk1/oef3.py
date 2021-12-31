# https://dodona.ugent.be/nl/courses/399/series/8795/activities/928829692/

def selection_sort_vooraan(a):
    for i in range(len(a)-1):
        positie = i
        min = a[i]
        for j in range(i+1, len(a)):
            if a[j] < min:
                positie = j
                min = a[j]
        a[positie] = a[i]
        a[i] = min
        print(a)


a = [int(_) for _ in input().split()]
selection_sort_vooraan(a)
