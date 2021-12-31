# https://dodona.ugent.be/nl/courses/399/series/8800/activities/369146716/
# from typing import Sequence

import heapq


class AchtPuzzel:

    BUREN = {0: {("R", 1), ("O", 3)},   1: {("L", 0), ("R", 2), ("O", 4)},   2: {("L", 1), ("O", 5)},
             3: {("B", 0), ("R", 4), ("O", 6)}, 4: {("B", 1), ("L", 3), ("R", 5), ("O", 7)}, 5: {("B", 2), ("L", 4), ("O", 8)},
             6: {("B", 3), ("R", 7)},   7: {("B", 4), ("L", 6), ("R", 8)},   8: {("B", 5), ("L", 7)}
             }

    def __init__(self, bord="123456780"):
        assert set(bord) == set("012345678"), "geen correct bord"
        self.bord = bord

    def __str__(self):
        return self.bord[:3] + "\n" + self.bord[3:6] + "\n" + self.bord[6:]

    def __repr__(self):
        return f"AchtPuzzel(bord='{self.bord}')"

    def __eq__(self, other):
        if isinstance(other, AchtPuzzel):
            return self.bord == other.bord
        return False

    def __hash__(self):
        return hash(self.bord)

    def opvolgers(self):
        result = set()
        positieGat = self.bord.find("0")
        actiesMetNieuwePositiesLijst = self.BUREN.get(positieGat)
        for tuppleActie in actiesMetNieuwePositiesLijst:
            actie = tuppleActie[0]
            nieuwbord = list(self.bord)
            nieuwbord[positieGat], nieuwbord[tuppleActie[1]
                                             ] = nieuwbord[tuppleActie[1]], nieuwbord[positieGat]
            nieuwbord = ''.join(nieuwbord)
            nieuwePuzzel = AchtPuzzel(nieuwbord)
            result.add((actie, nieuwePuzzel))
        return result

    def aantal_verkeerd(self, other):
        count = 0
        for i, getal in enumerate(self.bord):
            if getal not in (other.bord[i], "0"):
                count += 1
        return count

    def manhattan_heuristiek(self, other):
        count = 0
        for i, getal in enumerate(self.bord):
            if getal != "0":
                pos = other.bord.find(getal)
                r = i//3
                k = i % 3
                row = pos//3
                col = pos % 3
                count += abs(r-row) + abs(k-col)
        return count


class Plan:

    def __init__(self, toestand, voorganger=None, actie=None, kost=0, h_waarde=float("inf")):
        self.toestand = toestand
        self.voorganger = voorganger
        self.actie = actie
        self.kost = kost
        self.h_waarde = h_waarde

    # Vergelijk op basis van cost + heuristic
    def __lt__(self, other):
        return (self.kost+self.h_waarde) < (other.kost+self.h_waarde)

    def geef_actie_sequentie(self):
        result = []
        huidige = self
        while huidige.voorganger is not None:
            result.append(huidige.actie)
            huidige = huidige.voorganger
        result.reverse()
        return result


def a_ster_zoeken(start_toestand, is_doel, heuristiek, kost=lambda s, a: 1):
    wachtrij = []
    closed = set()
    heapq.heappush(wachtrij, Plan(start_toestand))
    while len(wachtrij) > 0:
        # is altijd kleinste gebruikt _lt_ om te vgl
        plan = heapq.heappop(wachtrij)
        toestand = plan.toestand
        if is_doel(toestand):
            # idk wtf hier mis mee was maar zonder dit faalde dodona testen
            resultje = plan.geef_actie_sequentie()
            resultje.reverse()
            return (resultje, plan.kost)

        if toestand not in closed:  # deze
            closed.add(toestand)  # en deze weg = boomgebaseerde A*
            for (actie, nieuweToestand) in sorted(toestand.opvolgers()):
                heapq.heappush(wachtrij, Plan(
                    nieuweToestand, plan, actie, plan.kost + kost(toestand, actie), heuristiek(nieuweToestand)))
    return None
