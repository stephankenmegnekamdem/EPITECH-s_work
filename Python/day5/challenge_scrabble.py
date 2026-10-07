points = {
    1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'],
    2: ['D', 'G'],
    3: ['B', 'C', 'M', 'P'],
    4: ['F', 'H', 'V', 'W', 'Y'],
    5: ['K'],
    8: ['J', 'X'],
    10: ['Q', 'Z']

}

def points_calculator(sen, points):
        sen.upper()
        score=0
        for letter in sen:
            for i in points:
                if letter in points[i]:
                    score=score+i
        print(score)


points_calculator('HELLO', points)