with open('input.txt', "r") as f:
    a, h, z, n = [int(x) for x in next(f).split()] # read first line

print(a, h, z, n)

edge = max(a, h, z)

w = open("output.txt", "w")
if n != 0:
    def f(n, edge):
        #print("f", n)

        if n == 0: return 1
        if n < 0:
            return 0

        count = 0

        if edge >= a:
            count = f(n - a, a)
        if edge >= h:
            count = count + f(n - h, h)
        if edge >= z:
            count = count + f(n - z, z)

        return count

    print(f(n, edge))

    w.write(str(f(n, edge)))
else:
    w.write(str(0))
w.close()