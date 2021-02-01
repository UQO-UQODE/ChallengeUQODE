def question1():
    """
    Auteur : Charlotte Foucard
    Description de la fonction : program which will find all such numbers which are divisible by 7
    but are not a multiple of 5, between 2000 and 3200 (both included).
    :return: None
    """
    l = []
    for i in range(2000, 3201):
        if (i % 7 == 0) and (i % 5 != 0):
            l.append(str(i))

    print(','.join(l))


# Test question 1 
# ce test est a titre d'exemple
# On ne devrais pas garder ca, car ca va faire beaucoup de print si tout le monde en fait.
question1()
