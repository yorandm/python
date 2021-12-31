# https://dodona.ugent.be/nl/courses/399/series/8795/activities/277529356/
def bubble_sort(a):
    n = len(a)
    count = 0
    for i in range(n-1):
        for j in range(n-1, i, -1):
            count += 1
            if a[j-1] > a[j]:
                een = a[j-1]
                twee = a[j]
                a[j-1] = twee
                a[j] = een
        print(a)
    print(
        f"Voor een rij van lengte {n} werd het if-statement {count} keer uitgevoerd")


a = [int(_) for _ in input().split()]
bubble_sort(a)
