# https://dodona.ugent.be/nl/courses/399/series/8799/activities/1200279845/
def precies_een_verschillend(eerste, tweede):
    if len(eerste) != len(tweede):
        return False
    aantal = 0
    for (c1, c2) in zip(eerste, tweede):
        if c1 != c2:
            aantal += 1
    return aantal == 1


def maak_graaf(woorden):
    graaf = {woord: set() for woord in woorden}
    for i, woord1 in enumerate(woorden):
        for j in range(i+1, len(woorden)):
            woord2 = woorden[j]
            if precies_een_verschillend(woord1, woord2):
                graaf[woord1].add(woord2)
                graaf[woord2].add(woord1)
    return graaf


def kortste_pad(graaf, startWoord):
    # d = [-1]*n
    p = {w: None for w in graaf}  # kan geen [] zijn maar moet dict zijn
    # d[startWoord]=0
    p[startWoord] = startWoord
    q = []
    q.append(startWoord)
    while len(q) > 0:
        v = q.pop(0)
        for w in sorted(graaf[v]):
            if p[w] is None:
                # if d[w] == -1:
                # d[w] = d[v] +1
                p[w] = v
                q.append(w)
    return p


def geef_pad(voorgangers, doelWoord):
    pad = [doelWoord]
    huidigWoord = doelWoord
    voorganger = voorgangers[huidigWoord]
    while huidigWoord != voorganger:
        pad.insert(0, voorganger)
        huidigWoord = voorgangers[huidigWoord]
        voorganger = voorgangers[huidigWoord]
    return pad
