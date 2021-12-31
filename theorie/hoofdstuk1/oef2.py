# https://dodona.ugent.be/nl/courses/399/series/8795/activities/875119571/
def zoekBinair(rij, zoekItem):
    l = 0
    r = len(rij)-1
    while l != r:
        print(f"{l}, {r}")
        m = int((l+r)/2)
        if rij[m] < zoekItem:
            l = m+1
        else:
            r = m
    if rij[l] == zoekItem:
        return l
    return -1
