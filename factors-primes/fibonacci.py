def fib_nums_list(top_end):
    a, b, x, y = 0, 1, 0, top_end
    fib_list = []
    while x < y:
        fib_list.append(a)
        c = a + b
        a = b
        b = c
        x += 1
    print(fib_list)

fib_nums_list(int(input()))