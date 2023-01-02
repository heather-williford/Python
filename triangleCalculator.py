import math

def calcS2A2(AA, AB, AC, SA, SB, SC, s, s1, s2):
    print('side ' + s1 + ': ',end='')
    SA = float(input(''))
    print('side ' + s2 + ': ',end='')
    SB = float(input(''))
    #AC = (180 - (AA + AB))
    AB = AB*(math.pi/180)
    AC = AC*(math.pi/180) 
    ratio = (SB/math.sin(AB))
    SC = (ratio*math.sin(AC))
    AC = AC*(180/math.pi)
    AC = round(AC, 2)
    SC = round(SC, 2)
    print('The missing side ' + s + ' is ', SC)
    return SC

def calcS1A2(AA, AB, AC, SA, SB, SC, s, s1, s2):
    print('side ' + s + ': ',end='')
    SC = float(input(''))
    AC = AC*(math.pi/180)
    AB = AB*(math.pi/180)
    AA = AA*(math.pi/180)
    SA = ((SC*math.sin(AA))/math.sin(AC))
    SB = ((SC*math.sin(AB))/math.sin(AC))
    SA = round(SA, 2)
    SB = round(SB, 2)
    print('The missing side ' + s1 + ' is ', SA)
    print('The missing side ' + s2 + ' is ', SB)

def calcS2A1(AB, AC, SB, SC, s):
    AB = AB*(math.pi/180)
    AC = AC*(math.pi/180) 
    ratio = (SB/math.sin(AB))
    SC = (ratio*math.sin(AC))
    AC = AC*(180/math.pi)
    AC = round(AC, 2)
    SC = round(SC, 2)
    print('The missing side ' + s + ' is ', SC)
    return SC

answer = input('Are you missing a side or an angle (or both)? ')

if answer == 'angle':
    many = int(input('How many of the angles do you know? '))
    if many == 2:
        angleA = float(input('angle A: '))
        angleB = float(input('angle B: '))
        angleC = 180 - (angleA + angleB)
        print('The missing angle C is ', angleC)
    if many == 1:
        angleA = float(input('angle A: '))
        sideA = float(input('side A: '))
        sideB = float(input('side B: '))
        sideC = float(input('side C: '))
        rad = math.acos(((sideA*sideA)+(sideC*sideC)-(sideB*sideB))/(2*sideA*sideC))
        angleB = (rad*(180/math.pi))
        angleC = (180 - (angleB + angleA))
        print('The missing angle B is ', angleB)
        print('The missing angle C is ', angleC)  
    if many == 0:
        sideA = float(input('side A: '))
        sideB = float(input('side B: '))
        sideC = float(input('side C: '))
        rad = math.acos(((sideB*sideB)+(sideC*sideC)-(sideA*sideA))/(2*sideB*sideC))
        angleA = (rad*(180/math.pi))
        rad = math.acos(((sideA*sideA)+(sideC*sideC)-(sideB*sideB))/(2*sideA*sideC))
        angleB = (rad*(180/math.pi))
        angleC = (180 - (angleA + angleB))
        print('The missing angle A is ', angleA)
        print('The missing angle B is ', angleB)
        print('The missing angle C is ', angleC)

if answer == 'side':
    many = int(input('How many of the sides do you know? '))
    if many == 2:
        sideA = float(input('side A: '))
        sideB = float(input('side B: '))
        angleA = float(input('angle A: '))
        angleB = float(input('angle B: '))
        angleC = float(input('angle C: '))
        angleA = angleA*(math.pi/180)
        angleC = angleC*(math.pi/180) 
        ratio = (sideA/math.sin(angleA))
        sideC = (ratio*math.sin(angleC))
        print('The missing side C is ', sideC)   
    if many == 1:
        sideA = float(input('side A: '))
        angleA = float(input('angle A: '))
        angleB = float(input('angle B: '))
        angleC = float(input('angle C: '))
        angleA = angleA*(math.pi/180)
        angleB = angleB*(math.pi/180)
        angleC = angleC*(math.pi/180)
        ratio = (sideA/math.sin(angleA))
        sideB = (ratio*math.sin(angleB))
        sideC = (ratio*math.sin(angleC))
        print('The missing side B is ', sideB)
        print('The missing side C is ', sideC)
    if many == 0:
        print('Triangle sides cannot be calculated')

if answer == 'both':
    manyA = int(input('How many angles do you know? '))
    manyS = int(input('How many sides do you know? '))
    if manyA == 2 and manyS == 2:
        angleA = float(input('angle A: '))
        angleB = float(input('angle B: '))
        angleC = (180 - (angleA + angleB))
        sideA = 0
        sideB = 0
        sideC = 0
        s = input('Which side are you missing (A, B, C) ? ')
        if (s == 'C'):
            s1 = 'A'
            s2 = 'B'
            calcS2A2(angleA, angleB, angleC, sideA, sideB, sideC, s, s1, s2)
            print('The missing angle C is ', angleC)
        if (s == 'B'):
            s1 = 'A'
            s2 = 'C'
            calcS2A2(angleA, angleC, angleB, sideA, sideC, sideB, s, s1, s2)
            print('The missing angle C is ', angleC)
        if (s == 'A'):
            s1 = 'B'
            s2 = 'C'
            calcS2A2(angleB, angleC, angleA, sideB, sideC, sideA, s, s1, s2)
            print('The missing angle C is ', angleC)
    if manyA == 2 and manyS == 1:
        angleA = float(input('angle A: '))
        angleB = float(input('angle B: '))
        angleC = (180 - (angleA + angleB))
        sideA = 0
        sideB = 0
        sideC = 0
        s = input('Which side do you know (A, B, C) ? ')
        if (s == 'C'):
            s1 = 'A'
            s2 = 'B'
            calcS1A2(angleA, angleB, angleC, sideA, sideB, sideC, s, s1, s2)
            angelC = round(angleC, 2)
            print('The missing angle C is ', angleC)
        if (s == 'B'):
            s1 = 'A'
            s2 = 'C'
            calcS1A2(angleA, angleC, angleB, sideA, sideC, sideB, s, s1, s2)
            angelC = round(angleC, 2)
            print('The missing angle C is ', angleC)
        if (s == 'A'):
            s1 = 'C'
            s2 = 'B'
            calcS1A2(angleC, angleB, angleA, sideC, sideB, sideA, s, s1, s2)
            angelC = round(angleC, 2)
            print('The missing angle C is ', angleC)
    if manyA == 2 and manyS == 0:
        angleA = float(input('angle A: '))
        angleB = float(input('angle B: '))
        angleC = (180 - (angleA + angleB))
        print('The missing angle C is ', angleC)
        print('The missing triangle sides cannot be found based on the given information')
    if manyA == 1 and manyS == 2:
        angleA = float(input('angle A: '))
        sideA = 0
        sideB = 0
        sideC = 0
        s = input('Which side are you missing (A, B, C) ? ')
        if (s == 'C'):
            s1 = 'A'
            s2 = 'B'
            print('side ' + s1 + ': ',end='')
            sideA = float(input(''))
            print('side ' + s2 + ': ',end='')
            sideB = float(input(''))
            angleA = angleA*(math.pi/180)
            angleB = (math.asin((sideB*math.sin(angleA))/sideA))
            angleB = angleB/(math.pi/180)
            angleA = angleA/(math.pi/180)
            print('angle B is', round(angleB, 2))
            angleC = (180 - (angleA + angleB))
            print('angle C is', round(angleC, 2))
            calcS2A1(angleB, angleC, sideB, sideC, s)
        if (s == 'B'):
            s1 = 'A'
            s2 = 'C'
            print('side ' + s1 + ': ',end='')
            sideA = float(input(''))
            print('side ' + s2 + ': ',end='')
            sideB = float(input(''))
            angleA = angleA*(math.pi/180)
            angleB = (math.asin((sideB*math.sin(angleA))/sideA))
            angleB = angleB/(math.pi/180)
            angleA = angleA/(math.pi/180)
            print('angle B is', round(angleB, 2))
            angleC = (180 - (angleA + angleB))
            print('angle C is', round(angleC, 2))
            calcS2A1(angleB, angleC, sideB, sideC, s)
        if (s == 'A'):
            s1 = 'B'
            s2 = 'C'
            print('side ' + s1 + ': ',end='')
            sideB = float(input(''))
            print('side ' + s2 + ': ',end='')
            sideC = float(input(''))
            angleA = angleA*(math.pi/180)
            sideA = math.sqrt((-1)*(((math.cos(angleA)*(2*sideB*sideC))-(sideB*sideB))-(sideC*sideC)))
            angleB = (math.asin((sideB*math.sin(angleA))/sideA))
            angleB = angleB/(math.pi/180)
            angleA = angleA/(math.pi/180)
            print('angle B is', round(angleB, 2))
            angleC = (180 - (angleA + angleB))
            print('angle C is', round(angleC, 2))
            calcS2A1(angleB, angleC, sideB, sideC, s)
    else:
        print('The triangle cannot be calculated')