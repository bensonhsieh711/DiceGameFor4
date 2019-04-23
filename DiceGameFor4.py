import random

def score_count(point):
    score = 0
    check = len([i for i in set(point)])
    if check == 1:
        score = 19
    elif check == 2:
        if point.count(max(point)) == 2:
            score = max(point) * 2
        else:
            score = 0
    elif check == 3:
        for i in point:
            if point.count(i) == 1:
                score += i
    else:
        score = 0
    return score

def rand_dice(name):
    i = 1
    score = 0
    while not score:
        point = [random.choice(dice) for c in range(4)]
        score = -1
        score = score_count(point)
        print("%s第 %s 次，擲出:" % (name, i), point)
        if score == 19:
            print("一色")
        else:
            print(score, "點")
        i += 1
    return score

print("***擲骰子遊戲***")
win, lose = 0, 0
dice = [i for i in range(1,7)]

while 1:
    c_score = rand_dice('電腦')
    play = input('請按Enter擲骰子')
    u_score = rand_dice('玩家')
    if c_score > u_score:
        print('你輸了!')
        lose += 1
    elif c_score < u_score:
        print('你贏了!')
        win += 1
    else:
        print('平手！')
    print('目前戰績%s勝%s負' % (win, lose))
    play = input('是否繼續(y/n)?')
    if play in ('n', 'N'):
        print('目前戰績%s勝%s負' % (win, lose))
        print('Good Bye!')
        break
    else:
        pass