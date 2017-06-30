
# from https://stackoverflow.com/a/8337140
def nth_item(n, item, iterable):
    i = -1
    for j in range(n):
        i = iterable.index(item, i + 1)
    return i

def chooseIceCream(m,n,a):
    for i1 in range(n):
        one_flavor=a[i1]
        if one_flavor >= m:
            continue
        remaining=m-one_flavor
        if remaining in a:
            if remaining==one_flavor:
                if a.count(remaining)>1:
                    i2=nth_item(2, remaining, a)
                    break
                else:
                    continue
            else:
                i2=a.index(remaining)
                break
    print ("{} {}".format(i1+1,i2+1))


t = int(input().strip())
for a0 in range(t):
    m = int(input().strip())
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    chooseIceCream(m,n,a)
