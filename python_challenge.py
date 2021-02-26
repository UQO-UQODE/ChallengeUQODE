import math

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

def question21():
    """
    Auteur: Marc-Antoine Ricard
    Description: This program can get command like UP 5, DOWN 3, LEFT 3, RIGHT 2 and calculate optimale distance between the starting point and the ending point 
    and there is a robot somewhere too, not sur where, but i'm pretty sur the question was about a robot.
    Test:
    UP 5
    DOWN 3
    LEFT 3
    RIGHT 2

    should give:
    2
    """
    pos = {'x':0, 'y':0}
    while True:
        dir = input()
        try:
            dir = dir.split()
            commande = dir[0]
            movement = int(dir[1])

            if commande == "UP":
                pos['y'] += movement
            if commande == "DOWN":
                pos['y'] -= movement
            if commande == "LEFT":
                pos['x'] += movement
            if commande == "RIGHT":
                pos['x'] -= movement
        except:
            #its not a real command, finish the algorythm
            break

    #distance btw 2 points: √((x2−x1)^2 + (y2−y1)^2)
    print( round(math.sqrt( (pos['x']**2) + (pos['y']**2))))

def question22():
    """
    Auteur: Marc-Antoine Ricard
    Description:
    Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.
    Suppose the following input is supplied to the program:
    New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
    Then, the output should be:
    2:2
    3.:1
    3?:1
    New:1
    Python:5
    Read:1
    and:1
    between:1
    choosing:1
    or:2
    to:1
    """
    inp = sorted(str(input()).split())
    answer = dict()
    for word in inp:
        if word in answer:
            answer[word] += 1
        else:
            answer[word] = 1
    for key, value in answer.items():
        print(f'{key}:{value}')

# Test question 1 
# ce test est a titre d'exemple
# On ne devrais pas garder ca, car ca va faire beaucoup de print si tout le monde en fait.
question22()
