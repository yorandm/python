# https://dodona.ugent.be/nl/courses/399/series/8796/activities/1458138173/
def evalueer_postfix(expressie):
    stapel = []
    for symbool in expressie:
        if symbool.isnumeric():
            stapel.append(symbool)
        else:  # operator of haakje
            op1 = stapel.pop()
            op2 = stapel.pop()
            uitkomst = voerBewerkingUit(float(op1), float(op2), symbool)
            stapel.append(uitkomst)
    return stapel.pop()


def voerBewerkingUit(op1, op2, bewerking):
    if bewerking == '+':
        return op1 + op2
    elif bewerking == "-":
        return op2 - op1
    elif bewerking == '*':
        return op1 * op2
    elif bewerking == '/':
        return op2 / op1


def infix_naar_postfix(expressie):
    stapel = []
    uitvoer = []
    for symbool in expressie:
        if symbool.isnumeric():
            uitvoer.append(symbool)
        else:  # operator of haakje
            if symbool == ')':  # sluitend haakje --> stapel kan niet leeg zijn, open haakje sws
                bovenste = stapel.pop()
                while(bovenste != "("):
                    uitvoer.append(bovenste)
                    bovenste = stapel.pop()
                # Openend haakje hier

            elif len(stapel) == 0 or symbool == '(' or prioriteit(symbool) > prioriteit(stapel[-1]):
                stapel.append(symbool)
            else:  # operator met lage prioriteit of sluitend haakje
                while len(stapel) > 0 and (prioriteit(stapel[-1]) >= prioriteit(symbool)):
                    uitvoer.append(stapel.pop())
                stapel.append(symbool)
    while len(stapel) > 0:
        uitvoer.append(stapel.pop())
    return uitvoer


def prioriteit(operator):
    if operator == '*' or operator == '/':
        return 2
    elif operator == "+" or operator == '-':
        return 1
    else:
        return 0


def rekenmachine(infix_string):
    infix_tokens = infix_string.split()
    postfix = infix_naar_postfix(infix_tokens)
    return evalueer_postfix(postfix)


infix = ["3", "*", "5"]
print(infix_naar_postfix(infix))
