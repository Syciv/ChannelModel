from prob import prob


def get_mistakes(num, p):
    e = []
    for i in range(num):
        if prob(p):
            e.append(1)
        else:
            e.append(0)
    return e


def generate_mistake(stream, e):
    result = []
    for i in range(len(stream)):
        result.append(str(int(stream[i])+int(e[i]) % 2))
    return result


