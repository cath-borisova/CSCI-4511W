import sat_interface

def tt1():
    '''Propositions:
        A: Amy is a truth-teller
        B: Bob is a truth-teller
        C: Cal is a truth-teller

    return a list containing all entailed propositions or negated propositions
    '''
    print("Truth-tellers and liars I")
    print("-------------------------")
    ttprob = sat_interface.KB(["~A ~B",
                                "B A",
                                "~B ~C",
                                "C B",
                                "~C ~A",
                                "~C ~B",
                                "A B C"])

    entailed = []
    if ttprob.test_literal("A") == False:
        entailed.append('~A')
        print("Amy is a liar")
    if ttprob.test_literal("~A") == False:
        entailed.append('A')
        print("Amy is a truth-teller")
    if ttprob.test_literal("B") == False:
        entailed.append('~B')
        print("Bob is a liar")
    if ttprob.test_literal("~B") == False:
        entailed.append('B')
        print("Bob is a truth-teller")
    if ttprob.test_literal("C") == False:
        entailed.append('~C')
        print("Cal is a liar")
    if ttprob.test_literal("~C") == False:
        entailed.append('C')
        print("Cal is a truth-teller")
    print("-------------------------")
    return entailed

def tt2():
    '''Propositions:
        A: Amy is a truth-teller
        B: Bob is a truth-teller
        C: Cal is a truth-teller
    '''
    print("Truth-tellers and liars II")
    ttprob = sat_interface.KB(["~A C",
                               "~A A",
                               "~C ~A A",
                               "~B ~C",
                               "C B",
                               "~C B ~A",
                               "~B A C"])
    entailed = []
    if ttprob.test_literal("A") == False:
        entailed.append('~A')
        print("Amy is a liar")
    if ttprob.test_literal("~A") == False:
        entailed.append('A')
        print("Amy is a truth-teller")
    if ttprob.test_literal("B") == False:
        entailed.append('~B')
        print("Bob is a liar")
    if ttprob.test_literal("~B") == False:
        entailed.append('B')
        print("Bob is a truth-teller")
    if ttprob.test_literal("C") == False:
        entailed.append('~C')
        print("Cal is a liar")
    if ttprob.test_literal("~C") == False:
        entailed.append('C')
        print("Cal is a truth-teller")
    print("-------------------------")
    return entailed

def tt3():
    '''Propositions:
        A: Amy is a truth-teller
        B: Bob is a truth-teller
        C: Cal is a truth-teller
    '''
    print("Truth-tellers and liars III")
    entailed = []

    ttprob = sat_interface.KB(["~A ~C",
                               "C A",
                               "~B C",
                               "~B A",
                               "~C ~A B",
                               "~C C",
                               "~C A",
                               "~C ~A C"])

    entailed = []
    if ttprob.test_literal("A") == False:
        entailed.append('~A')
        print("Amy is a liar")
    if ttprob.test_literal("~A") == False:
        entailed.append('A')
        print("Amy is a truth-teller")
    if ttprob.test_literal("B") == False:
        entailed.append('~B')
        print("Bob is a liar")
    if ttprob.test_literal("~B") == False:
        entailed.append('B')
        print("Bob is a truth-teller")
    if ttprob.test_literal("C") == False:
        entailed.append('~C')
        print("Cal is a liar")
    if ttprob.test_literal("~C") == False:
        entailed.append('C')
        print("Cal is a truth-teller")
    print("-------------------------")
    return entailed

def salt():
    '''Propositions:
        A: Caterpillar is telling the truth
        B: Bill the lizard is telling the truth
        C: the Cheshire Cat is telling the truth
        SA: Caterpillar stole the salt
        SB: Bill stole the salt
        SC: Cat stole the salt
    '''
    print("A salt and battery")

    ttprob = sat_interface.KB([
                               "~A SB",
                               "~SB A",
                               "~B SB",
                               "~SB B",
                               "~C ~SC",
                               "SC C",
                               "~SA ~SB",
                               "~SA ~SC",
                               "~SB ~SC",
                               "SB SC SA",
                               "~A ~B ~C",
                               "A B C"
                               ])
    entailed = []

    if ttprob.test_literal("A") == False:
        entailed.append('~A')
        print("Caterpillar is a liar")
    if ttprob.test_literal("~A") == False:
        entailed.append('A')
        print("Caterpillar is a truth-teller")
    if ttprob.test_literal("B") == False:
        entailed.append('~B')
        print("Lizard is a liar")
    if ttprob.test_literal("~B") == False:
        entailed.append('B')
        print("Lizard is a truth-teller")
    if ttprob.test_literal("C") == False:
        entailed.append('~C')
        print("Cat is a liar")
    if ttprob.test_literal("~C") == False:
        entailed.append('C')
        print("Cat is a truth-teller")

    if ttprob.test_literal("SA") == False:
        entailed.append('~SA')
        print("Caterpillar did not the salt")
    if ttprob.test_literal("~SA") == False:
        entailed.append('SA')
        print("Caterpillar stole the salt")
    if ttprob.test_literal("SB") == False:
        entailed.append('~SB')
        print("Lizard did not steal the salt")
    if ttprob.test_literal("~SB") == False:
        entailed.append('SB')
        print("Lizard stole the salt")
    if ttprob.test_literal("SC") == False:
        entailed.append('~SC')
        print("Cat did not steal the salt")
    if ttprob.test_literal("~SC") == False:
        entailed.append('SC')
        print("Cat stole the salt")
    print("-------------------------")
    return entailed

def main():
    tt1()
    tt2()
    tt3()
    salt()

if __name__ == '__main__':
    main()
