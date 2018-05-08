# http://codingdojang.com/scode/266?answer_mode=hide
def p266():
    X, Y = (int(x) for x in input("input 2 number: ").split(" "))
    # X, Y = int(a), int(b)
    print(X, Y)
    matrix = [[-1 for i in range(Y)] for j in range(X)]

    x = y = 0
    dx = 0
    dy = 1
    seq = 0
    while matrix[x][y] == -1:
        matrix[x][y] = seq
        seq += 1

        x, y = x+dx, y+dy
        if x in [-1, X] or y in [-1, Y] or matrix[x][y] != -1:
            x, y = x - dx, y - dy # prev xy
            dx, dy = dy, -dx      # new clock-wise
            x, y = x+dx, y+dy     # new xy

    for a in matrix:
        print(a)


# http://codingdojang.com/scode/365?answer_mode=hide
def p365_fn(n):
    return n + sum(int(x) for x in str(n))

def p365():
    d_list = set()
    for i in range(1,5000):
        d_list.add(p365_fn(i))

    n_list = set(range(1,5000))
    print(sum(n_list-d_list))


#####################################
if __name__ == "__main__":
    p266()
    p365()
