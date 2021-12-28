from prob import prob


def get_mistakes(num, p1, p2):
    result = []
    mistake = False
    for i in range(num):
        if mistake and prob(p2) or (not mistake) and prob(p1):
            mistake = True
            result.append(1)
        else:
            result.append(0)
            mistake = False
    return result
